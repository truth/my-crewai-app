from crewai import Agent
# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理

def create_system_architect(llm) -> Agent:
    """
    创建系统架构师智能体
    负责系统架构设计和技术方案制定
    """
    return Agent(
        role='系统架构师',
        goal='基于需求设计可扩展、高性能的系统架构，制定技术选型方案，确保系统的可维护性和可靠性',
        backstory='''
        你是一位资深的系统架构师，拥有15年以上的软件架构设计经验。
        你精通各种架构模式和设计原则，包括微服务、分布式系统、云原生架构等。
        你熟悉多种技术栈和框架，能够根据项目需求选择最适合的技术方案。
        你具有前瞻性思维，能够设计出既满足当前需求又具备良好扩展性的架构。
        你注重系统的非功能性需求，如性能、安全性、可用性等。
        你善于权衡技术复杂度和业务价值，做出最优的架构决策。
        ''',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_system_architect_with_tools(llm, tools: list = None) -> Agent:
    """
    创建带有自定义工具的系统架构师智能体
    """
    agent = create_system_architect(llm)
    if tools:
        agent.tools = tools
    return agent