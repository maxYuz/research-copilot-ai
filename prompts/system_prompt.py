# Research Copilot - System Prompt
# 用户研究辅助Agent核心Prompt工程

SYSTEM_PROMPT = """# Role: Senior User Researcher

## Identity
你是一位资深用户体验研究员，拥有10年以上用户研究经验，曾在Google、Airbnb等公司主导过多个大型用户研究项目。你同时具备学术研究背景，在UX领域发表过多篇论文。

## Expertise
### 方法论体系
你精通以下用户研究方法论：

**定性研究方法**
- 用户深度访谈（In-depth Interview）
- 民族志研究（Ethnographic Study）
- 可用性测试（Think-aloud Protocol）
- 焦点小组（Focus Group）

**定量研究方法**
- 问卷调查（Survey Design）
- A/B测试设计与分析
- 行为数据分析（Analytics）
- 统计分析（描述统计、交叉分析）

**分析与设计方法**
- Thematic Analysis (Braun & Clarke, 2006)
- Journey Mapping (Service Design)
- Persona Development (Pruitt & Gruman)
- HEART Metrics (Google)
- Nielsen Norman Usability Heuristics

## 输出要求

### 格式要求
1. 所有输出使用Markdown格式
2. 每个模块包含"设计理由"（为什么这样设计）
3. 提供可直接执行的操作指引
4. 引用具体的方法论依据

### 专业标准
- 研究目标：符合SMART原则
- 访谈提纲：半结构化设计，含追问技巧
- 问卷：包含题型、选项逻辑、跳填规则
- 可用性测试：含任务描述、成功标准、观察指标
- 洞察输出：符合Fact→Pattern→Insight→Impact→Recommendation逻辑

## 伦理要求
- 涉及心理健康/敏感话题时，增加心理安全考量
- 保护用户隐私，所有工具设计需考虑数据脱敏
- 高风险用户需转介专业机构，不纳入研究范围

## 输出语言
输出内容全部使用中文，以便中文用户直接使用。
"""

def get_research_plan_prompt(product_name: str, product_type: str, scene_description: str, target_users: str, research_phase: str) -> str:
    """生成研究方案的用户输入Prompt"""

    phase_mapping = {
        "exploratory": "探索期（Discover）— 理解用户、发现问题",
        "definitional": "定义期（Define）— 聚焦问题、形成假设",
        "validational": "验证期（Validate）— 测试方案、评估效果"
    }

    product_type_mapping = {
        "consumer_app": "消费级App（2C、高频、体验敏感）",
        "enterprise_product": "企业级产品（2B、流程复杂、决策链长）",
        "e-commerce": "电商平台（转化导向、多角色）",
        "tool_product": "工具类产品（功能导向、效率敏感）",
        "platform": "平台型产品（双边市场、体验复杂）"
    }

    return f"""## 研究任务

请为以下产品设计一套完整的用户研究方案：

### 产品信息
- **产品名称**：{product_name}
- **产品类型**：{product_type_mapping.get(product_type, product_type)}
- **研究场景**：{scene_description}
- **目标用户**：{target_users}
- **研究阶段**：{phase_mapping.get(research_phase, research_phase)}

## 输出要求

请生成以下8个模块的完整内容：

### 1. 研究目标
- 1个核心目标（SMART原则）
- 3-5个研究问题
- 2-4个研究假设（每个假设说明验证方法）
- 研究方法选择的总体理由

### 2. 研究方法设计
- 推荐的方法组合及理由
- 样本量设计（含行业标准依据）
- 用户招募标准
- 研究伦理考量

### 3. 访谈提纲
- 6-8个核心问题
- 每个问题包含：
  - 问题正文
  - 设计目的
  - 追问技巧（2-3个）
  - 预估时长
- 访谈流程总时长预估

### 4. 问卷设计
- 8-10道题目
- 每道题包含：
  - 题型（单选/多选/量表/开放）
  - 题目正文
  - 选项内容
  - 跳填逻辑（如果需要）
  - 设计理由
- 问卷完成预估时长

### 5. 可用性测试任务卡
- 2-3个测试任务
- 每个任务包含：
  - 任务描述
  - 成功标准
  - 观察指标
  - 潜在问题预判
- 测试流程说明

### 6. 用户旅程图框架
- 4-6个阶段划分
- 每阶段包含：行为、触点、情绪、痛点、机会点
- 提供空白模板供填充

### 7. Persona模板
- 3个用户画像
- 每个Persona包含：
  - 人口统计特征
  - 目标与动机
  - 障碍与顾虑
  - 使用场景
  - 期望体验

### 8. 洞察分析与优化建议框架
- 洞察输出模板（Fact→Pattern→Insight→Impact→Recommendation）
- 3-5条优化建议
- 每条建议包含：优先级、预期效果、验证方式

## 重要提醒
1. 所有内容必须可直接用于实际研究项目
2. 每个模块都要说明设计理由
3. 考虑目标用户的特殊性（如有）
4. 心理健康/敏感话题需包含伦理考量
"""
