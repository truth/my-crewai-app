from crewai import Task
from agents import create_requirements_analyst

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

def create_requirements_analysis_task(agent, project_description: str) -> Task:
    """
    创建需求分析任务
    """
    return Task(
        description=f'''
        基于以下项目描述进行深入的需求分析：
        
        项目描述：{project_description}
        
        请完成以下工作：
        1. 分析项目的核心业务目标和用户需求
        2. 识别主要的功能需求和非功能需求
        3. 定义用户角色和使用场景
        4. 分析需求的优先级和依赖关系
        5. 识别潜在的风险和约束条件
        6. 编写详细的需求规格说明书
        
        输出要求：
        - 需求规格说明书应包含功能需求、非功能需求、用户故事等
        - 使用清晰的结构和专业的语言
        - 确保需求的可测试性和可实现性
        ''',
        agent=agent,
        expected_output='''
        一份完整的需求规格说明书，包含：
        1. 项目概述和目标
        2. 用户角色定义
        3. 功能需求列表（包含优先级）
        4. 非功能需求（性能、安全、可用性等）
        5. 用户故事和验收标准
        6. 约束条件和假设
        7. 风险评估
        '''
    )

def create_requirements_review_task(agent, requirements_doc: str) -> Task:
    """
    创建需求评审任务
    """
    return Task(
        description=f'''
        对以下需求文档进行评审和优化：
        
        需求文档：{requirements_doc}
        
        请完成以下评审工作：
        1. 检查需求的完整性和一致性
        2. 验证需求的可实现性和可测试性
        3. 识别需求中的矛盾和遗漏
        4. 评估需求的优先级是否合理
        5. 提出改进建议和优化方案
        ''',
        agent=agent,
        expected_output='''
        需求评审报告，包含：
        1. 需求质量评估
        2. 发现的问题和风险
        3. 改进建议
        4. 优化后的需求文档
        '''
    )