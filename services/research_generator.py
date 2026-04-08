"""
Research Copilot - 研究方案生成服务
"""
import os
import json
import time
from typing import Optional
import httpx
from backend.prompts.system_prompt import SYSTEM_PROMPT, get_research_plan_prompt


def _load_config() -> dict:
    """从config.json加载配置"""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {"api_key": "", "model": "minimax"}


def _save_config(api_key: str, model: str) -> None:
    """保存配置到config.json"""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, 'w') as f:
        json.dump({"api_key": api_key, "model": model}, f)


class ResearchGenerator:
    """用户研究方案生成器"""

    # API配置映射
    API_CONFIGS = {
        # MiniMax
        "minimax": {
            "base_url": "https://api.minimaxi.com/v1",
            "model": "MiniMax-M2.7",
            "endpoint": "/text/chatcompletion_v2"
        },
        # DeepSeek
        "deepseek": {
            "base_url": "https://api.deepseek.com/v1",
            "model": "deepseek-chat",
            "endpoint": "/chat/completions"
        },
        # 豆包/Doubao (Douyin)
        "doubao": {
            "base_url": "https://ark.cn-beijing.volces.com/api/v3",
            "model": "doubao-pro-32k",
            "endpoint": "/chat/completions"
        },
        "火山引擎": {
            "base_url": "https://ark.cn-beijing.volces.com/api/v3",
            "model": "doubao-pro-32k",
            "endpoint": "/chat/completions"
        },
        # OpenAI (默认)
        "openai": {
            "base_url": "https://api.openai.com/v1",
            "model": "gpt-4",
            "endpoint": "/chat/completions"
        },
        "gpt-4": {
            "base_url": "https://api.openai.com/v1",
            "model": "gpt-4",
            "endpoint": "/chat/completions"
        }
    }

    def __init__(self, api_key: Optional[str] = None, model: str = "minimax"):
        config = _load_config()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or config.get("api_key", "")
        self.model = model if model != "gpt-4" else config.get("model", "minimax")
        self.base_url = "https://api.openai.com/v1/chat/completions"

    def _get_api_config(self) -> dict:
        """获取API配置"""
        # 查找匹配的API配置
        model_lower = self.model.lower()
        for key, config in self.API_CONFIGS.items():
            if key.lower() in model_lower or model_lower in key.lower():
                return config
        # 默认返回OpenAI格式
        return self.API_CONFIGS["openai"]

    async def generate_research_plan(
        self,
        product_name: str,
        product_type: str,
        scene_description: str,
        target_users: str,
        research_phase: str = "exploratory"
    ) -> dict:
        """
        生成完整用户研究方案

        Args:
            product_name: 产品名称
            product_type: 产品类型
            scene_description: 研究场景描述
            target_users: 目标用户描述
            research_phase: 研究阶段

        Returns:
            包含完整研究方案的字典
        """
        start_time = time.time()

        # 构建用户Prompt
        user_prompt = get_research_plan_prompt(
            product_name=product_name,
            product_type=product_type,
            scene_description=scene_description,
            target_users=target_users,
            research_phase=research_phase
        )

        # 调用LLM
        response = await self._call_llm(SYSTEM_PROMPT, user_prompt)

        generation_time = int((time.time() - start_time) * 1000)

        return {
            "status": "success",
            "data": {
                "content": response,
                "modules": self._extract_modules(response)
            },
            "meta": {
                "generation_time_ms": generation_time,
                "model": self.model,
                "product_name": product_name,
                "product_type": product_type,
                "research_phase": research_phase
            }
        }

    async def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        """调用LLM API（支持MiniMax/DeepSeek/豆包/OpenAI）"""
        if not self.api_key:
            return self._get_sample_output()

        config = self._get_api_config()
        base_url = config["base_url"]
        model_name = config["model"]
        endpoint = config["endpoint"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 8000
        }

        async with httpx.AsyncClient(timeout=300.0, proxy=None) as client:
            response = await client.post(
                f"{base_url}{endpoint}",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

    def _extract_modules(self, content: str) -> dict:
        """从Markdown内容中提取各模块"""
        modules = {}

        # 简单的模块分割逻辑
        module_names = [
            "研究目标", "研究方法设计", "访谈提纲", "问卷设计",
            "可用性测试", "用户旅程图", "Persona", "洞察分析",
            "优化建议"
        ]

        lines = content.split("\n")
        current_module = None
        current_content = []

        for line in lines:
            # 检测模块标题
            is_module_header = False
            for name in module_names:
                if name in line and ("#" in line or line.strip().startswith(name)):
                    is_module_header = True
                    break

            if is_module_header and current_module:
                modules[current_module] = "\n".join(current_content)
                current_content = []

            if is_module_header:
                for name in module_names:
                    if name in line:
                        current_module = name
                        break
            elif current_module:
                current_content.append(line)

        if current_module and current_content:
            modules[current_module] = "\n".join(current_content)

        return modules

    def _get_sample_output(self) -> str:
        """返回示例输出（无API Key时）"""
        return """# 用户研究方案

## 1. 研究目标

### 核心目标
[请配置API Key后生成完整内容]

---
*提示：此为占位输出，请设置OPENAI_API_KEY环境变量或通过配置接口设置API Key*

**配置方式**：
```bash
export OPENAI_API_KEY="your-api-key"
```

或通过API配置：
```bash
curl -X POST http://localhost:8000/configure \
  -H "Content-Type: application/json" \
  -d '{"api_key": "your-api-key"}'
```
"""


# 全局实例
_generator: Optional[ResearchGenerator] = None


def get_research_generator() -> ResearchGenerator:
    """获取生成器实例"""
    global _generator
    if _generator is None:
        _generator = ResearchGenerator()
    return _generator


def init_research_generator(api_key: str, model: str = "minimax") -> None:
    """初始化生成器"""
    global _generator
    _generator = ResearchGenerator(api_key=api_key, model=model)
    _save_config(api_key, model)
