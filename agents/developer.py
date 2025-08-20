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

def create_developer(llm) -> Agent:
    """
    创建开发工程师智能体
    负责代码设计、实现和优化
    """
    return Agent(
        role='开发工程师',
        goal='根据架构设计和需求规格，编写高质量、可维护的代码，实现系统功能，并进行代码优化和重构',
        backstory='''
        你是一位经验丰富的全栈开发工程师，拥有8年以上的软件开发经验。
        你精通多种编程语言和开发框架，包括Python、JavaScript、Java、React、Django等。
        你熟悉软件工程最佳实践，包括设计模式、代码规范、单元测试等。
        你具有良好的问题解决能力，能够快速定位和修复技术问题。
        你注重代码质量，遵循SOLID原则，编写可读性强、可维护性好的代码。
        你具备持续学习的能力，能够快速掌握新技术和工具。
        你善于与团队协作，能够进行有效的代码审查和技术分享。
        ''',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_developer_with_tools(llm, tools: list = None) -> Agent:
    """
    创建带有自定义工具的开发工程师智能体
    """
    agent = create_developer(llm)
    if tools:
        agent.tools = tools
    return agent