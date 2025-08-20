from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

def create_test_engineer(llm: ChatGoogleGenerativeAI) -> Agent:
    """
    创建测试工程师智能体
    负责测试计划制定、测试用例设计和质量保证
    """
    return Agent(
        role='测试工程师',
        goal='制定全面的测试策略，设计和执行测试用例，确保软件质量，发现和跟踪缺陷，保证产品交付质量',
        backstory='''
        你是一位专业的测试工程师，拥有6年以上的软件测试经验。
        你熟悉各种测试方法和技术，包括功能测试、性能测试、安全测试、自动化测试等。
        你精通测试工具和框架，如Selenium、JUnit、pytest、Postman等。
        你具有敏锐的质量意识，能够从用户角度思考问题，发现潜在的缺陷和风险。
        你善于设计测试用例，能够覆盖各种边界条件和异常场景。
        你注重测试效率，能够合理安排测试优先级，平衡测试覆盖率和时间成本。
        你具有良好的沟通能力，能够清晰地描述缺陷和测试结果。
        ''',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_test_engineer_with_tools(llm: ChatGoogleGenerativeAI, tools: list = None) -> Agent:
    """
    创建带有自定义工具的测试工程师智能体
    """
    agent = create_test_engineer(llm)
    if tools:
        agent.tools = tools
    return agent