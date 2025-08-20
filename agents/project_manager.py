from crewai import Agent
from typing import List, Optional

# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理

def create_project_manager(llm) -> Agent:
    """
    创建项目经理智能体
    负责整体项目协调、进度管理和任务分配
    """
    return Agent(
        role='项目经理',
        goal='协调整个软件开发项目，确保各个阶段按时高质量完成，管理团队协作和项目进度',
        backstory='''
        你是一位经验丰富的软件项目经理，拥有10年以上的项目管理经验。
        你擅长敏捷开发方法，熟悉软件开发生命周期的各个阶段。
        你具有出色的沟通协调能力，能够有效地管理跨职能团队。
        你注重质量控制和风险管理，确保项目按时交付。
        ''',
        verbose=True,
        allow_delegation=True,  # 允许委派任务给其他智能体
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_project_manager_with_tools(llm, tools: list = None) -> Agent:
    """
    创建带有自定义工具的项目经理智能体
    """
    agent = create_project_manager(llm)
    if tools:
        agent.tools = tools
    return agent