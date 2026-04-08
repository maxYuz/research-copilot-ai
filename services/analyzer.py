"""
Research Copilot - 研究分析服务
"""
import os
import json
from typing import Optional
import httpx

from backend.prompts.analysis_prompts import (
    INTERVIEW_CODING_PROMPT, get_interview_coding_prompt,
    QUESTIONNAIRE_ANALYSIS_PROMPT, get_questionnaire_analysis_prompt,
    USABILITY_ANALYSIS_PROMPT, get_usability_analysis_prompt,
    INSIGHT_GENERATION_PROMPT, get_insight_generation_prompt
)


def _load_config() -> dict:
    """从config.json加载配置"""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {"api_key": "", "model": "minimax"}


class ResearchAnalyzer:
    """用户研究分析器"""

    # API配置映射
    API_CONFIGS = {
        "minimax": {
            "base_url": "https://api.minimaxi.com/v1",
            "model": "MiniMax-M2.7",
            "endpoint": "/text/chatcompletion_v2"
        },
        "deepseek": {
            "base_url": "https://api.deepseek.com/v1",
            "model": "deepseek-chat",
            "endpoint": "/chat/completions"
        },
        "doubao": {
            "base_url": "https://ark.cn-beijing.volces.com/api/v3",
            "model": "doubao-pro-32k",
            "endpoint": "/chat/completions"
        },
        "openai": {
            "base_url": "https://api.openai.com/v1",
            "model": "gpt-4",
            "endpoint": "/chat/completions"
        }
    }

    def __init__(self, api_key: Optional[str] = None, model: str = "minimax"):
        config = _load_config()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or config.get("api_key", "")
        self.model = model if model != "gpt-4" else config.get("model", "minimax")

    def _get_api_config(self) -> dict:
        """获取API配置"""
        model_lower = self.model.lower()
        for key, config in self.API_CONFIGS.items():
            if key.lower() in model_lower or model_lower in key.lower():
                return config
        return self.API_CONFIGS["openai"]

    async def analyze_interview(self, interview_text: str) -> dict:
        """
        访谈编码与主题归类分析

        Args:
            interview_text: 访谈记录文本

        Returns:
            编码表、主题归类结果
        """
        return await self._analyze(
            prompt_template=INTERVIEW_CODING_PROMPT,
            user_prompt=get_interview_coding_prompt(interview_text),
            analysis_type="访谈分析"
        )

    async def analyze_questionnaire(self, questionnaire_data: str) -> dict:
        """
        问卷统计分析

        Args:
            questionnaire_data: 问卷数据

        Returns:
            描述统计、交叉分析结果
        """
        return await self._analyze(
            prompt_template=QUESTIONNAIRE_ANALYSIS_PROMPT,
            user_prompt=get_questionnaire_analysis_prompt(questionnaire_data),
            analysis_type="问卷分析"
        )

    async def analyze_usability(self, usability_data: str) -> dict:
        """
        可用性问题归类分析

        Args:
            usability_data: 可用性测试观察记录

        Returns:
            问题清单、严重度评级
        """
        return await self._analyze(
            prompt_template=USABILITY_ANALYSIS_PROMPT,
            user_prompt=get_usability_analysis_prompt(usability_data),
            analysis_type="可用性分析"
        )

    async def generate_insights(self, raw_data: str, data_type: str = "研究数据") -> dict:
        """
        洞察提炼

        Args:
            raw_data: 原始数据
            data_type: 数据类型描述

        Returns:
            洞察列表
        """
        return await self._analyze(
            prompt_template=INSIGHT_GENERATION_PROMPT,
            user_prompt=get_insight_generation_prompt(raw_data, data_type),
            analysis_type="洞察提炼"
        )

    async def _analyze(self, prompt_template: str, user_prompt: str, analysis_type: str) -> dict:
        """通用分析调用"""
        if not self.api_key:
            return {
                "status": "error",
                "message": "请先配置API Key"
            }

        try:
            result = await self._call_llm(prompt_template, user_prompt)
            return {
                "status": "success",
                "data": {
                    "content": result,
                    "analysis_type": analysis_type
                }
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    async def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        """调用LLM API"""
        config = self._get_api_config()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": config["model"],
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 8000
        }

        async with httpx.AsyncClient(timeout=300.0, proxy=None) as client:
            response = await client.post(
                f"{config['base_url']}{config['endpoint']}",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]


# 全局实例
_analyzer: Optional[ResearchAnalyzer] = None


def get_analyzer() -> ResearchAnalyzer:
    """获取分析器实例"""
    global _analyzer
    if _analyzer is None:
        _analyzer = ResearchAnalyzer()
    return _analyzer


def init_analyzer(api_key: str, model: str = "minimax") -> None:
    """初始化分析器"""
    global _analyzer
    _analyzer = ResearchAnalyzer(api_key=api_key, model=model)
    # 保存到config.json
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, 'w') as f:
        json.dump({"api_key": api_key, "model": model}, f)
