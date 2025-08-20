from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

def create_devops_engineer(llm: ChatGoogleGenerativeAI) -> Agent:
    """
    创建DevOps工程师智能体
    负责部署、运维和CI/CD流水线设计
    """
    return Agent(
        role='DevOps工程师',
        goal='设计和实施自动化部署流程，构建CI/CD流水线，确保系统的稳定运行和高效交付',
        backstory='''
        你是一位经验丰富的DevOps工程师，拥有7年以上的运维和自动化经验。
        你精通容器化技术（Docker、Kubernetes）和云平台服务（AWS、Azure、阿里云）。
        你熟悉各种CI/CD工具，如Jenkins、GitLab CI、GitHub Actions等。
        你具有丰富的基础设施即代码（IaC）经验，熟悉Terraform、Ansible等工具。
        你注重系统监控和日志管理，能够快速定位和解决生产环境问题。
        你具有安全意识，能够实施安全最佳实践，保护系统和数据安全。
        你善于自动化重复性工作，提高团队效率和系统可靠性。
        ''',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )

def create_devops_engineer_with_tools(llm: ChatGoogleGenerativeAI, tools: list = None) -> Agent:
    """
    创建带有自定义工具的DevOps工程师智能体
    """
    agent = create_devops_engineer(llm)
    if tools:
        agent.tools = tools
    return agent