# Research Copilot

<div align="center">

[![Stars](https://img.shields.io/github/stars/your-username/research-copilot?style=social)](https://github.com/maxyuz/research-copilot)
[![License](https://img.shields.io/github/license/your-username/research-copilot)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)

**AI驱动的用户研究辅助工具** — 输入产品/场景，输出完整研究方案；粘贴数据，自动分析。

[English](README_EN.md) | 简体中文

</div>

---

## 产品简介

Research Copilot 是一款面向用户研究员、PM、UX设计师的 AI 辅助工具，基于专业用户研究方法论，帮助你：

- **快速生成完整研究方案** — 输入产品信息，输出包含研究目标、访谈提纲、问卷设计、可用性测试的完整方案
- **自动分析定性数据** — 粘贴访谈记录，自动完成主题编码与归类
- **自动分析定量数据** — 粘贴问卷数据，自动计算描述统计、NPS、交叉分析
- **可用性问题归类** — 粘贴测试观察记录，自动归类问题并输出严重度评级

> 特别适合：用研新人学习研究流程、独立开发者做产品前验证、快速构建用户研究作品集

---

## 功能特性

### 1. 研究方案生成

输入产品名称、类型、研究场景，输出完整用户研究方案。

**输出包含**：
- 研究目标（SMART原则）
- 研究问题与假设
- 研究方法设计（访谈/问卷/可用性测试）
- 访谈提纲（含追问技巧）
- 问卷设计（含跳填逻辑）
- 可用性测试任务卡
- 用户旅程图框架
- Persona模板
- 洞察分析框架

### 2. 访谈分析（定性）

粘贴访谈记录，自动进行主题归类分析（Thematic Analysis）。

**基于方法论**：[Braun & Clarke (2006)](https://www.researchgate.net/publication/247515610_Using_Thematic_Analysis_in_Psychology) 六步编码法

**输出包含**：
- 初始编码表
- 高阶类别整合
- 主题归类
- 主题关系图
- 关键洞察

### 3. 问卷统计（定量）

粘贴问卷数据，自动进行统计分析。

**分析方法**：
- 描述性统计（频次、占比、平均值）
- NPS计算（净推荐值）
- 交叉分析（维度间关联）
- 问题优先级矩阵

### 4. 可用性分析

粘贴可用性测试观察记录，自动归类问题并评级。

**基于方法论**：[Nielsen Norman](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) 可用性评估框架

**输出包含**：
- 问题清单（严重度评级 P0-P3）
- 修复优先级排序
- 效率评分
- 改进建议

---

## 支持的 AI API

| API | 模型示例 | 配置 model 值 |
|-----|---------|---------------|
| **MiniMax** | M2.7 | `minimax` |
| **DeepSeek** | deepseek-chat | `deepseek` |
| **豆包/火山引擎** | doubao-pro-32k | `doubao` |
| **OpenAI** | GPT-4 / GPT-4o | `openai` / `gpt-4` |
| **Claude** | Claude-3.5-Sonnet | `claude` |

> 你只需要准备其中任意一个 API Key 即可使用全部功能

---

## 快速开始

### 环境要求

- Python 3.8+
- 一个 AI API Key（MiniMax / DeepSeek / OpenAI / Claude 等）

### 1. 克隆项目

```bash
git clone https://github.com/maxyuz/research-copilot.git
cd research-copilot
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

**方式一：通过页面配置（推荐）**

启动服务后，在页面顶部输入 API Key 并保存，Key 会保存在 `backend/config.json` 中。

**方式二：通过配置文件**

```bash
cp backend/config.example.json backend/config.json
```

编辑 `backend/config.json`：
```json
{
  "api_key": "你的API Key",
  "model": "minimax"
}
```

**方式三：通过环境变量**

```bash
export OPENAI_API_KEY="your-api-key"
```

### 4. 启动服务

```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### 5. 打开页面

访问 http://localhost:8001/index.html

---

## 方法论说明

本工具内置专业用户研究方法论，确保输出结果具有方法论依据：

| 功能 | 方法论 | 来源 |
|------|--------|------|
| 访谈分析 | Thematic Analysis | Braun & Clarke (2006) |
| 问卷统计 | 描述统计 + 交叉分析 + NPS | 行业标准 |
| 可用性分析 | Nielsen Norman 可用性评估 | NN Group |
| 洞察提炼 | Insight Pyramid | 行业标准 |

### Thematic Analysis（六步编码法）

1. 熟悉数据（熟悉访谈内容）
2. 生成初始编码（Initial Coding）
3. 寻找主题（Searching for Themes）
4. 审视主题（Reviewing Themes）
5. 定义主题（Defining Themes）
6. 输出报告（Producing the Report）

### Nielsen Norman 可用性评估

问题严重度评级：
- **P0** — Usability Catastrophe（灾难性问题）
- **P1** — Serious Usability Problem（严重问题）
- **P2** — Minor Usability Problem（轻微问题）
- **P3** — Cosmetic Problem（ Cosmetic 问题）

---

## API 接口

如果你想通过 API 调用：

| 端点 | 方法 | 功能 |
|------|------|------|
| `POST /api/generate` | 生成研究方案 |
| `POST /api/analyze/interview` | 访谈主题归类分析 |
| `POST /api/analyze/questionnaire` | 问卷统计分析 |
| `POST /api/analyze/usability` | 可用性问题归类分析 |
| `POST /api/configure` | 配置 API Key |

### 配置 API

```bash
curl -X POST http://localhost:8001/api/configure \
  -H "Content-Type: application/json" \
  -d '{"api_key": "your-api-key", "model": "minimax"}'
```

### 生成研究方案

```bash
curl -X POST http://localhost:8001/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "你的产品名称",
    "product_type": "consumer_app",
    "scene_description": "用户首次使用后的次周留存率很低",
    "target_users": "22-35岁城市白领",
    "research_phase": "exploratory"
  }'
```

---

## 项目结构

```
research-copilot/
├── backend/
│   ├── main.py                 # FastAPI 入口
│   ├── config.example.json      # 配置模板
│   ├── prompts/
│   │   ├── system_prompt.py    # 研究方案 Prompt
│   │   └── analysis_prompts.py # 分析功能 Prompt
│   ├── routers/
│   │   └── research.py         # API 路由
│   └── services/
│       ├── research_generator.py # 研究方案生成
│       └── analyzer.py          # 数据分析服务
├── frontend/
│   └── index.html              # 前端页面（零依赖）
├── 示例_访谈分析输入.md         # 访谈分析示例
├── 示例_问卷统计输入.md         # 问卷统计示例
├── 示例_可用性分析输入.md       # 可用性分析示例
└── README.md
```

---

## 技术栈

- **后端**：FastAPI（异步支持、高性能）
- **前端**：HTML + Vanilla JS（零依赖、秒开）
- **AI 模型**：支持 MiniMax / DeepSeek / OpenAI / Claude
- **Prompt 工程**：内置专业用户研究方法论框架

---

## 适用场景

- PM / UX 设计师快速生成研究方案
- 用研新人学习用户研究流程
- 独立开发者做产品前验证
- 构建用户研究作品集
- 快速制作用户研究报告

---

## 常见问题

**Q: 需要自己提供 API Key 吗？**
A: 是的，你需要自己准备一个 AI API Key。工具支持 MiniMax、DeepSeek、OpenAI、Claude 等多种 API。

**Q: 数据会被保存在服务器上吗？**
A: 不会。所有数据处理都在本地完成，API Key 也保存在本地的 `config.json` 文件中（已加入 .gitignore，不会被提交到 GitHub）。

**Q: 支持哪些语言？**
A: 当前版本优化了中文输入体验，也支持英文。

**Q: 分析结果准确吗？**
A: 分析结果基于 AI 模型生成，建议结合专业判断使用。工具提供的是方法论框架和辅助分析，而非最终结论。

---

## Star History

如果你觉得有帮助，请给个 ⭐

[![Star History](https://api.star-history.com/svg?repos=your-username/research-copilot&type=Timeline)](https://star-history.com/#your-username/research-copilot&Timeline)

---

## License

MIT License

---

<div align="center">

**Made with ❤️ for User Researchers**

</div>
