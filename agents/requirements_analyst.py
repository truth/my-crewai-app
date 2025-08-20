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

def create_requirements_analyst(llm) -> Agent:
    """
    创建需求分析师智能体
    负责收集、分析和整理用户需求
    """
    return Agent(
        role='需求分析师',
        goal='深入理解和分析用户需求，编写清晰准确的需求规格说明书，确保需求的完整性和可实现性',
        backstory='''
        你是一位专业的需求分析师，拥有丰富的业务分析经验。
        你擅长与客户沟通，能够准确理解用户的真实需求和业务目标。
        你熟悉各种需求分析方法和工具，能够将复杂的业务需求转化为清晰的技术规格。
        你注重细节，善于发现需求中的矛盾和遗漏，确保需求的完整性和一致性。
        你具有良好的文档编写能力，能够产出高质量的需求文档。
        ''',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_requirements_analyst_with_tools(llm, tools: list = None) -> Agent:
    """
    创建带有自定义工具的需求分析师智能体
    """
    agent = create_requirements_analyst(llm)
    if tools:
        agent.tools = tools
    return agent