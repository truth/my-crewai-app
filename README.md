# CrewAI 软件开发全流程管理系统

🚀 基于AI智能体的软件开发项目管理工具，实现从需求分析到部署运维的完整自动化流程。

## ✨ 特性

- **🤖 智能化协作**：6个专业AI智能体协同工作
- **📋 全流程覆盖**：项目启动 → 需求分析 → 系统设计 → 开发实现 → 测试验证 → 部署运维
- **🔧 灵活配置**：支持自定义工作流和智能体配置
- **🎯 多种模式**：演示模式、交互模式、自定义模式
- **📚 完整文档**：详细的使用指南和最佳实践

## 🏗️ 系统架构

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   项目经理      │    │   需求分析师    │    │   系统架构师    │
│ Project Manager │    │Requirements     │    │System Architect │
│                 │    │Analyst          │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   开发工程师    │    │   测试工程师    │    │  DevOps工程师   │
│   Developer     │    │ Test Engineer   │    │DevOps Engineer  │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 快速开始

### 环境要求

- Python >= 3.11
- Google Gemini API密钥

### 安装

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd my-crewai-app
   ```

2. **安装依赖**
   ```bash
   pip install -e .
   ```

3. **配置API密钥**
   ```bash
   # Windows
   set GOOGLE_API_KEY=your-api-key-here
   
   # Linux/Mac
   export GOOGLE_API_KEY='your-api-key-here'
   ```

4. **运行系统**
   ```bash
   python main.py
   ```

### 快速体验

运行演示项目（个人博客系统需求分析）：

```bash
python main.py
# 选择选项 1: 运行演示项目
```

## 📖 使用指南

### 基本使用

1. **演示模式**：运行预设的个人博客系统项目
2. **交互模式**：输入自定义项目描述，选择执行阶段
3. **完整工作流**：执行从需求分析到部署的完整流程

### 工作流阶段

| 阶段 | 智能体 | 主要输出 |
|------|--------|----------|
| 项目启动 | 项目经理 | 项目计划、风险评估 |
| 需求分析 | 需求分析师 | 需求规格说明书 |
| 系统设计 | 系统架构师 | 架构设计文档 |
| 开发规划 | 开发工程师 | 开发计划、技术方案 |
| 测试规划 | 测试工程师 | 测试计划、测试用例 |
| 部署规划 | DevOps工程师 | 部署方案、CI/CD配置 |

### 高级用法

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from workflows import create_software_development_workflow

# 创建自定义工作流
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
workflow = create_software_development_workflow(llm)

# 执行特定阶段
requirements_crew = workflow.create_requirements_analysis_crew(
    "开发一个电商网站，支持商品管理、订单处理、用户管理等功能"
)
result = requirements_crew.kickoff()
```

## 📁 项目结构

```
my-crewai-app/
├── agents/                 # 智能体定义
│   ├── project_manager.py  # 项目经理
│   ├── requirements_analyst.py # 需求分析师
│   ├── system_architect.py # 系统架构师
│   ├── developer.py        # 开发工程师
│   ├── test_engineer.py    # 测试工程师
│   └── devops_engineer.py  # DevOps工程师
├── tasks/                  # 任务定义
│   ├── requirements_analysis.py
│   ├── system_design.py
│   ├── development.py
│   ├── testing.py
│   ├── deployment.py
│   └── project_management.py
├── workflows/              # 工作流定义
│   └── software_development_workflow.py
├── tools/                  # 自定义工具
├── examples/               # 使用示例
│   └── complete_workflow_example.py
├── docs/                   # 文档
│   └── user_guide.md       # 详细使用指南
├── tests/                  # 测试文件
├── config.py               # 系统配置
├── main.py                 # 主程序入口
└── requirements.txt        # 依赖列表
```

## 🎯 智能体介绍

### 项目经理 (Project Manager)
- **职责**：项目整体协调、进度管理、风险控制
- **特长**：项目规划、团队协调、沟通管理

### 需求分析师 (Requirements Analyst)
- **职责**：需求收集、分析、文档编写
- **特长**：业务分析、用户研究、需求建模

### 系统架构师 (System Architect)
- **职责**：系统架构设计、技术选型、性能规划
- **特长**：架构设计、技术评估、性能优化

### 开发工程师 (Developer)
- **职责**：代码实现、开发规划、代码审查
- **特长**：编程开发、代码优化、技术实现

### 测试工程师 (Test Engineer)
- **职责**：测试规划、用例设计、质量保证
- **特长**：测试设计、质量控制、缺陷管理

### DevOps工程师 (DevOps Engineer)
- **职责**：部署规划、CI/CD设计、运维监控
- **特长**：自动化部署、容器化、监控运维

## 📋 使用示例

### 示例1：电商网站项目

```python
project_description = """
开发一个B2C电商网站，主要功能包括：
1. 用户注册登录和个人中心
2. 商品展示和搜索
3. 购物车和订单管理
4. 支付集成
5. 后台管理系统

技术要求：
- 前端：React.js + TypeScript
- 后端：Node.js + Express
- 数据库：MongoDB
- 部署：Docker + AWS
"""

# 执行需求分析
requirements_crew = workflow.create_requirements_analysis_crew(project_description)
result = requirements_crew.kickoff()
```

### 示例2：移动应用项目

```python
project_description = """
开发一个健身追踪移动应用，功能包括：
1. 运动数据记录和分析
2. 健身计划制定
3. 社交分享功能
4. 营养建议
5. 可穿戴设备集成

技术要求：
- 移动端：React Native
- 后端：Python + Django
- 数据库：PostgreSQL
- 云服务：Google Cloud Platform
"""

# 执行完整工作流
full_crew = workflow.create_full_development_crew(project_description)
result = full_crew.kickoff()
```

## ⚙️ 配置说明

### 环境变量

- `GOOGLE_API_KEY`: Google Gemini API密钥（必需）
- `CREWAI_LOG_LEVEL`: 日志级别（可选，默认INFO）

### 系统配置

在 `config.py` 中可以调整：

- 模型参数（temperature、max_tokens等）
- 智能体配置（max_iter、memory等）
- 任务超时设置
- 输出格式配置

## 🔧 自定义扩展

### 添加新智能体

```python
from crewai import Agent

def create_custom_agent(llm):
    return Agent(
        role="自定义角色",
        goal="实现特定目标",
        backstory="角色背景故事",
        llm=llm,
        verbose=True
    )
```

### 添加新任务

```python
from crewai import Task

def create_custom_task(agent):
    return Task(
        description="任务描述",
        agent=agent,
        expected_output="期望输出格式"
    )
```

## 🐛 常见问题

### Q: API密钥配置问题
A: 确保正确设置环境变量，可以在代码中添加调试输出检查。

### Q: 执行速度慢
A: 可以调整temperature参数和max_iter设置来优化性能。

### Q: 输出质量不理想
A: 提供更详细的项目描述，调整智能体的backstory和expected_output。

详细的问题解决方案请参考 [使用指南](docs/user_guide.md)。

## 📚 文档

- [详细使用指南](docs/user_guide.md)
- [API文档](docs/api.md)
- [最佳实践](docs/best_practices.md)

## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License

## 🙏 致谢

感谢 [CrewAI](https://github.com/joaomdmoura/crewAI) 框架提供的强大基础。

---

**开始您的AI驱动软件开发之旅！** 🚀
