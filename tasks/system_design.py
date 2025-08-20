from crewai import Task
from agents import create_system_architect
from langchain_google_genai import ChatGoogleGenerativeAI

def create_system_design_task(agent, requirements_doc: str) -> Task:
    """
    创建系统架构设计任务
    """
    return Task(
        description=f'''
        基于以下需求文档设计系统架构：
        
        需求文档：{requirements_doc}
        
        请完成以下架构设计工作：
        1. 分析需求并确定系统边界
        2. 设计系统的整体架构和模块划分
        3. 选择合适的技术栈和框架
        4. 设计数据库结构和数据流
        5. 定义API接口和服务契约
        6. 考虑系统的可扩展性和性能要求
        7. 设计安全架构和部署方案
        
        输出要求：
        - 提供清晰的架构图和设计文档
        - 说明技术选型的理由
        - 考虑系统的非功能性需求
        ''',
        agent=agent,
        expected_output='''
        完整的系统架构设计文档，包含：
        1. 系统架构概述和设计原则
        2. 系统架构图（整体架构、模块架构、部署架构）
        3. 技术栈选型和说明
        4. 数据库设计（ER图、表结构）
        5. API设计规范
        6. 安全架构设计
        7. 性能和扩展性考虑
        8. 部署和运维方案
        '''
    )

def create_architecture_review_task(agent, architecture_doc: str) -> Task:
    """
    创建架构评审任务
    """
    return Task(
        description=f'''
        对以下系统架构设计进行评审：
        
        架构文档：{architecture_doc}
        
        请完成以下评审工作：
        1. 评估架构的合理性和可行性
        2. 检查技术选型是否适合项目需求
        3. 分析架构的可扩展性和维护性
        4. 识别潜在的性能瓶颈和风险点
        5. 评估安全性和可靠性设计
        6. 提出优化建议
        ''',
        agent=agent,
        expected_output='''
        架构评审报告，包含：
        1. 架构质量评估
        2. 技术选型分析
        3. 风险识别和缓解方案
        4. 性能和扩展性评估
        5. 改进建议和最佳实践
        '''
    )

def create_technical_specification_task(agent, architecture_doc: str) -> Task:
    """
    创建技术规格说明任务
    """
    return Task(
        description=f'''
        基于架构设计编写详细的技术规格说明：
        
        架构文档：{architecture_doc}
        
        请完成以下工作：
        1. 详细定义各个模块的接口和职责
        2. 编写API文档和数据格式规范
        3. 定义编码规范和开发标准
        4. 制定数据库设计规范
        5. 定义测试策略和质量标准
        ''',
        agent=agent,
        expected_output='''
        技术规格说明书，包含：
        1. 模块设计规范
        2. API接口文档
        3. 数据库设计文档
        4. 编码规范和标准
        5. 测试规范
        6. 部署和配置说明
        '''
    )