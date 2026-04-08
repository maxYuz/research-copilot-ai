"""
Research Copilot - 研究方案生成API路由
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal

from backend.services.research_generator import get_research_generator


router = APIRouter(prefix="/api", tags=["research"])


class GenerateRequest(BaseModel):
    """生成研究方案请求"""
    product_name: str = Field(..., description="产品名称", examples=["觉心"])
    product_type: Literal[
        "consumer_app",
        "enterprise_product",
        "e_commerce",
        "tool_product",
        "platform"
    ] = Field(..., description="产品类型")
    scene_description: str = Field(..., description="研究场景描述")
    target_users: str = Field(default="通用用户群体", description="目标用户描述")
    research_phase: Literal[
        "exploratory",
        "definitional",
        "validational"
    ] = Field(default="exploratory", description="研究阶段")


class GenerateResponse(BaseModel):
    """生成研究方案响应"""
    status: str
    data: dict
    meta: dict


class ConfigureRequest(BaseModel):
    """配置请求"""
    api_key: str
    model: Optional[str] = "minimax"


class ConfigureResponse(BaseModel):
    """配置响应"""
    status: str
    message: str


@router.post("/configure", response_model=ConfigureResponse)
async def configure(request: ConfigureRequest):
    """配置API Key（同时初始化研究生成器和分析器）"""
    from backend.services.research_generator import init_research_generator
    from backend.services.analyzer import init_analyzer

    if not request.api_key.startswith("sk-"):
        raise HTTPException(status_code=400, detail="Invalid API Key format")

    init_research_generator(request.api_key, request.model)
    init_analyzer(request.api_key, request.model)
    return ConfigureResponse(
        status="success",
        message=f"配置成功，当前模型: {request.model}"
    )


@router.post("/generate", response_model=GenerateResponse)
async def generate_research_plan(request: GenerateRequest):
    """生成用户研究方案"""
    try:
        generator = get_research_generator()
        result = await generator.generate_research_plan(
            product_name=request.product_name,
            product_type=request.product_type,
            scene_description=request.scene_description,
            target_users=request.target_users,
            research_phase=request.research_phase
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "ok"}


# ============================================================
# 分析功能API
# ============================================================

class InterviewAnalysisRequest(BaseModel):
    """访谈分析请求"""
    interview_text: str = Field(..., description="访谈记录文本")


class QuestionnaireAnalysisRequest(BaseModel):
    """问卷分析请求"""
    questionnaire_data: str = Field(..., description="问卷数据")


class UsabilityAnalysisRequest(BaseModel):
    """可用性分析请求"""
    usability_data: str = Field(..., description="可用性测试观察记录")


class InsightRequest(BaseModel):
    """洞察提炼请求"""
    raw_data: str = Field(..., description="原始数据")
    data_type: str = Field(default="研究数据", description="数据类型描述")


@router.post("/analyze/interview")
async def analyze_interview(request: InterviewAnalysisRequest):
    """访谈编码与主题归类分析"""
    from backend.services.analyzer import get_analyzer

    try:
        analyzer = get_analyzer()
        result = await analyzer.analyze_interview(request.interview_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/questionnaire")
async def analyze_questionnaire(request: QuestionnaireAnalysisRequest):
    """问卷统计分析"""
    from backend.services.analyzer import get_analyzer

    try:
        analyzer = get_analyzer()
        result = await analyzer.analyze_questionnaire(request.questionnaire_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/usability")
async def analyze_usability(request: UsabilityAnalysisRequest):
    """可用性问题归类分析"""
    from backend.services.analyzer import get_analyzer

    try:
        analyzer = get_analyzer()
        result = await analyzer.analyze_usability(request.usability_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/insights")
async def generate_insights(request: InsightRequest):
    """洞察提炼"""
    from backend.services.analyzer import get_analyzer

    try:
        analyzer = get_analyzer()
        result = await analyzer.generate_insights(request.raw_data, request.data_type)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
