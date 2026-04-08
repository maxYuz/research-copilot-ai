# 用户研究辅助Agent - PRD

**版本**：v0.2
**日期**：2026-04-08
**状态**：草稿 → 待评审

---

## 1. 产品概述

### 1.1 产品定义

**Research Copilot** — 一款基于LLM的用户研究方案生成工具，通过结构化的Prompt工程，将专业用户研究方法论封装为可操作的工具输出。

**核心能力**：输入产品场景 → 输出可直接执行的研究方案

### 1.2 专业性标准

本工具产出的研究方案须满足以下专业标准：

| 标准 | 定义 |
|------|------|
| **方法论严谨性** | 符合User Research主流方法论体系（York University Guidelines、NN/g标准） |
| **方案可执行性** | 输出的访谈提纲可直接用于真实访谈，问卷可直接发放 |
| **洞察可落地性** | 洞察产出符合"证据→模式→insight→建议"的推导逻辑 |
| **行业通用性** | 不绑定特定产品类型，可覆盖2C/2B/平台型/工具型等产品 |

### 1.3 目标用户

| 用户类型 | 特征 | 核心需求 |
|----------|------|----------|
| 转行者 | UX/用研零基础，有其他领域经验 | 建立方法论框架，形成项目作品 |
| 初级从业者 | 0-2年经验，执行力强 | 提高工作效率，减少重复劳动 |
| 产品经理 | 有一定经验，缺乏系统训练 | 快速输出专业方案，用于汇报 |

---

## 2. 用户研究方法论体系

### 2.1 方法论框架

工具内置以下主流用户研究方法论：

#### 2.1.1 研究类型分类

```
用户研究方法谱系
├── 按知识类型
│   ├── 定性研究（Exploratory）— 回答"Why"
│   │   ├── 用户深度访谈（In-depth Interview）
│   │   ├── 民族志研究（Ethnographic Study）
│   │   └── 可用性测试（Think-aloud Protocol）
│   │
│   └── 定量研究（Confirmatory）— 回答"What/How much"
│       ├── 问卷调查（Survey）
│       ├── A/B测试（A/B Test）
│       └── 行为数据分析（Analytics）
│
├── 按研究阶段
│   ├── 探索期（Discover）— 理解用户、发现问题
│   ├── 定义期（Define）— 聚焦问题、形成假设
│   └── 验证期（Validate）— 测试方案、评估效果
│
└── 按研究目的
    ├── 需求研究（Needs Research）
    ├── 可用性研究（Usability Research）
    ├── 体验研究（Experience Research）
    └── 概念测试（Concept Testing）
```

#### 2.1.2 方法选择决策矩阵

工具内置方法选择逻辑，输出时自动说明选择依据：

| 研究问题类型 | 推荐方法组合 | 理由 |
|--------------|--------------|------|
| 用户动机与障碍 | 深度访谈 + 问卷 | 定性探索 + 定量验证 |
| 流程可用性问题 | 可用性测试 + 访谈 | 行为观察 + 原因挖掘 |
| 满意度与偏好 | 问卷 +  NPS | 大样本量化 |
| 新概念验证 | 概念测试 + 焦点小组 | 快速验证市场反应 |

### 2.2 研究设计模型

#### 2.2.1 混合研究设计（Mixed Methods）

工具采用**解释性序贯设计（Explanatory Sequential Design）**：

```
Phase 1: 定性研究（30%资源）
    ↓ 发现模式
Phase 2: 定量验证（50%资源）
    ↓ 验证假设
Phase 3: 可用性测试（20%资源）
    ↓ 方案迭代
```

#### 2.2.2 样本量决策

工具输出时自动包含样本量说明：

| 方法 | 行业标准 | 工具输出 |
|------|----------|----------|
| 用户访谈 | 5-8人（定性饱和） | 5人 |
| 问卷调查 | 30-100人（统计效力） | 30份 |
| 可用性测试 | 5人（发现85%问题） | 3-5人 |

### 2.3 数据分析方法

#### 2.3.1 定性分析：主题归类法（Thematic Analysis）

工具内置Braun & Clarke (2006) 六步分析框架：

```
1. 数据熟悉（Familiarization）
    → 访谈录音转录，反复阅读

2. 生成初始编码（Initial Coding）
    → 系统性地为数据打标签

3. 搜索主题（Theme Search）
    → 将编码聚类为潜在主题

4. 主题审视（Theme Review）
    → 检验主题与数据、主题与整体的拟合度

5. 主题定义（Theme Definition）
    → 明确每个主题的边界和内涵

6. 报告撰写（Report Writing）
    → 选择证据，撰写洞察
```

#### 2.3.2 定量分析：描述统计

工具输出的定量分析包含：

| 指标类型 | 内容 |
|----------|------|
| 集中趋势 | 平均值、中位数、众数 |
| 离散程度 | 标准差、方差、极值 |
| 分布形态 | 正态分布检验、偏度 |
| 交叉分析 | 维度间关联（如：使用频率 × 满意度） |

#### 2.3.3 可用性指标

工具输出的可用性测试结果包含：

| 指标 | 计算方式 | 行业基准 |
|------|----------|----------|
| 任务完成率 | 成功人数 / 总人数 | > 78% |
| 任务时间 | 均值 + 标准差 | 对比竞品 |
| 错误数 | 总操作错误次数 | 越低越好 |
| 严重度评分 | 问题等级（致命/严重/一般/cosmetic） | 无致命问题 |

### 2.4 洞察输出标准

工具输出的洞察须符合以下结构：

| 层级 | 定义 | 示例 |
|------|------|------|
| **事实（Fact）** | 客观观察到的行为或陈述 | 68%用户在注册环节放弃 |
| **模式（Pattern）** | 跨用户的重复行为 | 中途放弃的用户都提到"步骤太多" |
| **洞察（Insight）** | 对用户需求的深层理解 | 用户在决策压力下需要更清晰的引导 |
| **影响（Impact）** | 对业务指标的影响 | 预计优化后可提升转化率15% |
| **建议（Recommendation）** | 具体可执行的行动 | 增加进度指示器，减少注册步骤至3步 |

---

## 3. 功能需求

### 3.1 核心功能：研究方案生成

#### 3.1.1 输入参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| product_name | string | ✓ | 产品名称 |
| product_type | enum | ✓ | 产品类型（见3.1.2） |
| scene_description | string | ✓ | 研究场景/要解决的问题 |
| target_users | string | ○ | 目标用户描述 |
| research_phase | enum | ○ | 研究阶段（探索/定义/验证） |

#### 3.1.2 产品类型分类

| 类型 | 特点 | 推荐方法组合 |
|------|------|--------------|
| 消费级App | 2C、高频、体验敏感 | 访谈 + 问卷 + 可用性测试 |
| 企业级产品 | 2B、流程复杂、决策链长 | 访谈 + 可用性测试 |
| 电商平台 | 转化导向、多角色 | 问卷 + 可用性测试 + 访谈 |
| 工具类产品 | 功能导向、效率敏感 | 可用性测试 + 访谈 |
| 平台型产品 | 双边市场、体验复杂 | 深度访谈 + 民族志 |

#### 3.1.3 输出模块

| 模块 | 内容规格 | 方法论依据 |
|------|----------|------------|
| **研究目标** | 1个核心目标 + 3-5个研究问题 + 2-4个假设 | SMART目标原则 |
| **研究方法** | 方法组合 + 样本量 + 招募标准 | York方法论指南 |
| **访谈提纲** | 6-8个核心问题，每个问题含：目的、追问提示、时长预估 | 半结构化访谈设计 |
| **问卷设计** | 8-10题，含：题目、题型、选项逻辑、跳填规则 | Survey Design指南 |
| **可用性测试** | 2-3个任务卡，含：任务描述、成功标准、观察指标 | Nielsen Norman Group |
| **旅程图框架** | 4-6阶段，含：行为、触点、情绪、痛点、机会点 | Service Design方法 |
| **Persona模板** | 3个用户画像，含：人口统计、目标、动机、障碍 | Pruitt & Gruman模型 |
| **洞察分析框架** | Insight输出模板，含：证据→模式→洞察→建议 | Insight Pyramid |
| **优化建议框架** | 3-5条建议，含：优先级、预期效果、验证方式 | ICE评分矩阵 |

### 3.2 进阶功能：研究材料优化

| 输入类型 | 优化内容 |
|----------|----------|
| 访谈提纲 | 追问技巧优化、逻辑结构优化、敏感问题处理 |
| 问卷 | 题目措辞优化、选项平衡、逻辑跳转修复 |
| 调研报告 | 结构优化、洞察深度提升、数据呈现优化 |

### 3.3 进阶功能：数据分析辅助

| 输入 | 工具输出 |
|------|----------|
| 访谈转录文字 | 编码表（Bulid Codes）、主题归类结果 |
| 问卷数据（JSON/CSV） | 描述统计、交叉分析、可视化建议 |
| 可用性测试观察笔记 | 问题清单（带严重度）、优先级排序 |

---

## 4. 用户流程

### 4.1 主流程

```
用户输入
    │
    ▼
┌─────────────────┐
│  场景定义         │
│  • 产品/场景描述   │
│  • 研究目的       │
│  • 目标用户       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI方案生成       │
│  • 研究目标       │
│  • 方法设计       │
│  • 工具设计       │
│  • 框架输出       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  结果展示         │
│  • 分模块预览     │
│  • 一键复制       │
│  • Markdown导出   │
└─────────────────┘
```

### 4.2 场景示例

#### 输入示例 1

```
产品名称：觉心（心理健康App）
产品类型：消费级App
场景描述：用户首次使用后的次周留存率很低，想研究原因
目标用户：22-35岁城市白领
```

#### 输出示例 1（研究目标模块）

```markdown
## 研究目标

### 核心目标
识别导致用户首次使用后留存率低的关键体验障碍，分析其根因并提出优化方向。

### 研究问题
1. 用户首次使用的核心动机是什么？
2. 用户在首次使用过程中遇到哪些障碍？
3. 哪些因素会导致用户中断或放弃？
4. 用户的隐私顾虑如何影响使用行为？

### 研究假设
- H1：首次使用缺乏正向反馈，导致用户感知价值不足
- H2：隐私顾虑使用户不敢深入表达，影响AI服务质量
- H3：缺乏"正常化"引导，使用户不确定如何使用产品
```

---

## 5. 技术方案

### 5.1 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                      用户界面层                          │
│                   (HTML + Vanilla JS)                    │
└─────────────────────────┬───────────────────────────────┘
                          │ HTTP / SSE
┌─────────────────────────▼───────────────────────────────┐
│                      API网关层                          │
│                   (FastAPI Router)                       │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                      服务层                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │ResearchPlan  │  │  Optimizer  │  │ DataAnalyzer│    │
│  │  Generator   │  │             │  │             │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                      模型层                             │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Prompt Engineering                   │   │
│  │  • System Prompt（角色定义+方法论）                 │   │
│  │  • User Prompt（场景输入）                         │   │
│  │  • Output Schema（结构化输出格式）                  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                      LLM层                             │
│              (OpenAI GPT-4 / Claude Opus)              │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Prompt工程设计

#### 5.2.1 System Prompt结构

```markdown
# Role: Senior User Researcher

## Expertise
- 10+ years experience in UX research
- Mastery of qualitative and quantitative methods
- Published researcher with academic background

## Methodology Framework
你遵循以下用户研究方法论体系：

### 研究设计原则
1. 目的导向：每个方法都服务于研究目标
2. 三角验证：定性+定量交叉验证
3. 样本饱和：样本量以信息饱和为准

### 方法论依据
- York University User Research Guidelines
- Nielsen Norman Group Usability heuristics
- Braun & Clarke Thematic Analysis (2006)
- Pruitt & Gruman Persona methodology

## Output Format
所有输出必须：
1. 包含"为什么这样设计"的解释
2. 引用方法论依据
3. 提供可直接执行的操作指引
```

#### 5.2.2 Output Schema示例

```json
{
  "research_objectives": {
    "core_objective": "string",
    "research_questions": ["string"],
    "hypotheses": [
      {
        "id": "H1",
        "statement": "string",
        "validation_method": "string"
      }
    ],
    "methodology_rationale": "string"
  },
  "interview_guide": {
    "total_duration": "string",
    "questions": [
      {
        "id": "Q1",
        "question": "string",
        "purpose": "string",
        "probing_techniques": ["string"],
        "estimated_time": "string"
      }
    ]
  },
  "questionnaire": {
    "total_duration": "string",
    "questions": [
      {
        "id": "Q1",
        "type": "single_choice | multiple_choice | rating | open",
        "question": "string",
        "options": ["string"],
        "logic": "string | null",
        "design_rationale": "string"
      }
    ]
  }
}
```

### 5.3 API设计

#### 5.3.1 POST /api/generate

生成完整研究方案

```json
// Request
{
  "product_name": "觉心",
  "product_type": "consumer_app",
  "scene_description": "用户首次使用后的次周留存率很低，想研究原因",
  "target_users": "22-35岁城市白领",
  "research_phase": "exploratory"
}

// Response
{
  "status": "success",
  "data": {
    "research_objectives": {...},
    "methods": {...},
    "interview_guide": {...},
    "questionnaire": {...},
    "usability_test": {...},
    "journey_map": {...},
    "personas": {...},
    "insight_framework": {...},
    "recommendations": {...}
  },
  "meta": {
    "generation_time_ms": 12500,
    "model": "gpt-4",
    "methodology_notes": ["..."]
  }
}
```

#### 5.3.2 POST /api/optimize

优化已有研究材料

```json
// Request
{
  "material_type": "interview_guide",
  "content": "用户访谈提纲内容...",
  "optimization_goal": "提升追问深度"
}

// Response
{
  "status": "success",
  "data": {
    "optimized_content": "...",
    "improvements": [
      "增加情境假设类追问",
      "增加情感验证类追问"
    ],
    "rationale": "..."
  }
}
```

#### 5.3.3 POST /api/analyze

辅助数据分析

```json
// Request
{
  "analysis_type": "thematic",
  "raw_data": "访谈转录文字..."
}

// Response
{
  "status": "success",
  "data": {
    "codes": [...],
    "themes": [...],
    "insights": [...]
  }
}
```

### 5.4 技术选型

| 组件 | 选型 | 理由 |
|------|------|------|
| 后端框架 | FastAPI | 异步支持、类型安全、文档自动生成 |
| 前端 | HTML + Vanilla JS | 零依赖、部署简单 |
| LLM | OpenAI GPT-4 / Claude Opus | 推理能力强、输出稳定 |
| 存储 | 本地文件系统 | V1单用户模式 |
| 部署 | Docker | 环境一致性 |

---

## 6. 验收标准

### 6.1 功能验收

| 功能点 | 验收条件 | 测试方法 |
|--------|----------|----------|
| 方案生成 | 30秒内返回完整方案 | 计时测试 |
| 结构完整性 | 输出包含全部8个模块 | 逐项检查 |
| 格式正确性 | Markdown格式正确，无语法错误 | 渲染测试 |
| 内容可执行性 | 访谈提纲可直接用于实际访谈 | 专家评审 |

### 6.2 专业性验收

| 维度 | 验收条件 | 评估标准 |
|------|----------|----------|
| 方法论严谨性 | 研究设计有明确的方法论依据 | 专家评审 |
| 工具设计质量 | 访谈提纲、问卷符合设计规范 | Nielsen Norman检查清单 |
| 洞察推导逻辑 | 输出符合Fact→Pattern→Insight→Recommendation | 逻辑追溯 |

### 6.3 用户体验验收

| 指标 | 目标值 |
|------|--------|
| 首次使用成功率 | > 95% |
| 用户满意度（自评） | > 4.0/5 |
| 愿意推荐给同行 | NPS > 30 |

---

## 7. V1范围

### 7.1 In Scope

- [x] 研究方案生成（核心功能）
- [x] 研究材料优化（访谈提纲、问卷）
- [x] Markdown导出
- [x] 单用户本地模式

### 7.2 Out of Scope（V1不做）

- [ ] 用户招募
- [ ] 数据采集（问卷发布）
- [ ] 复杂统计分析（因子分析、回归）
- [ ] 团队协作
- [ ] 云端同步

---

## 8. 附录

### 8.1 参考文献

1. Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), 77-101.
2. Nielsen Norman Group. (2024). UX Research Methods and Best Practices.
3. Lazar, J., et al. (2017). Research Methods in Human-Computer Interaction (2nd ed.).
4. Pruitt, J., & Gruman, J. (2007). Sketching User Experiences: Getting the Design Right and the Right Design.
5. York University. (2022). User Research Guidelines.

### 8.2 术语表

| 术语 | 定义 |
|------|------|
| Thematic Analysis | 主题归类法，定性数据分析方法 |
| Triangulation | 三角验证，使用多种方法验证同一结论 |
| Information Saturation | 信息饱和，样本量确定的定性标准 |
| NPS | Net Promoter Score，净推荐值 |
| HEART | Google's UX metrics framework |

---

**评审状态**：待评审
**下一步**：确认后进入Phase 1开发
