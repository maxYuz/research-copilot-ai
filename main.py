"""
Research Copilot - FastAPI 主入口
用户研究辅助Agent

功能：
- 输入产品/场景描述 → 输出完整用户研究方案
- 支持访谈提纲、问卷、可用性测试等工具设计
- 导出Markdown格式
"""
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.routers.research import router as research_router


# 创建 FastAPI 应用
app = FastAPI(
    title="Research Copilot",
    description="AI驱动的用户研究方案生成工具 - 输入产品/场景，输出可执行的研究方案",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 注册路由
app.include_router(research_router)


@app.on_event("startup")
async def startup_event():
    """启动时检查配置"""
    # 尝试从config.json加载配置
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    api_key = os.getenv("OPENAI_API_KEY", "")
    model = "minimax"

    if os.path.exists(config_path):
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
            if config.get("api_key"):
                api_key = config.get("api_key", "")
                model = config.get("model", "minimax")

    if not api_key:
        print("=" * 60)
        print("Research Copilot 服务已启动")
        print("请在页面顶部配置API Key，或设置环境变量 OPENAI_API_KEY")
        print("=" * 60)
    else:
        # 初始化服务
        from backend.services.research_generator import init_research_generator
        from backend.services.analyzer import init_analyzer
        init_research_generator(api_key, model)
        init_analyzer(api_key, model)
        print(f"Research Copilot 服务已启动 (模型: {model})")


@app.get("/")
async def root():
    """根路径"""
    return {
        "name": "Research Copilot",
        "version": "1.0.0",
        "description": "AI驱动的用户研究方案生成工具",
        "endpoints": {
            "generate": "POST /api/generate",
            "configure": "POST /api/configure",
            "docs": "GET /docs"
        },
        "usage": {
            "step1": "配置API Key: POST /api/configure",
            "step2": "生成方案: POST /api/generate",
            "example_request": {
                "product_name": "觉心",
                "product_type": "consumer_app",
                "scene_description": "用户首次使用后的次周留存率很低",
                "target_users": "22-35岁城市白领",
                "research_phase": "exploratory"
            }
        }
    }


@app.get("/index.html")
async def get_frontend():
    """提供前端页面"""
    return FileResponse("frontend/index.html")


# 启动命令
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
