from crewai import Task
from agents import create_developer
# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理

def create_development_planning_task(agent, technical_spec: str) -> Task:
    """
    创建开发计划任务
    """
    return Task(
        description=f'''
        基于技术规格说明制定详细的开发计划：
        
        技术规格：{technical_spec}
        
        请完成以下开发规划工作：
        1. 分析技术规格并识别开发任务
        2. 将功能模块分解为具体的开发任务
        3. 评估各任务的开发工作量和复杂度
        4. 确定任务之间的依赖关系
        5. 制定开发时间表和里程碑
        6. 识别技术风险和解决方案
        7. 定义代码结构和组织方式
        
        输出要求：
        - 提供详细的任务分解和时间估算
        - 考虑代码复用和模块化设计
        - 制定合理的开发优先级
        ''',
        agent=agent,
        expected_output='''
        开发计划文档，包含：
        1. 任务分解结构（WBS）
        2. 开发时间表和里程碑
        3. 任务依赖关系图
        4. 技术风险评估
        5. 代码结构设计
        6. 开发环境和工具配置
        7. 质量保证计划
        '''
    )

def create_code_implementation_task(agent, module_spec: str, task_description: str) -> Task:
    """
    创建代码实现任务
    """
    return Task(
        description=f'''
        实现指定模块的功能代码：
        
        模块规格：{module_spec}
        任务描述：{task_description}
        
        请完成以下开发工作：
        1. 根据规格设计模块的类和接口
        2. 实现核心业务逻辑
        3. 添加适当的错误处理和日志记录
        4. 编写单元测试用例
        5. 添加必要的文档和注释
        6. 进行代码自测和优化
        
        代码要求：
        - 遵循编码规范和最佳实践
        - 确保代码的可读性和可维护性
        - 实现适当的错误处理机制
        - 包含完整的单元测试
        ''',
        agent=agent,
        expected_output='''
        完整的代码实现，包含：
        1. 功能代码文件
        2. 单元测试代码
        3. 代码文档和注释
        4. 配置文件（如需要）
        5. 依赖说明
        6. 使用示例
        '''
    )

def create_code_review_task(agent, code_files: str) -> Task:
    """
    创建代码审查任务
    """
    return Task(
        description=f'''
        对以下代码进行全面审查：
        
        代码文件：{code_files}
        
        请完成以下代码审查工作：
        1. 检查代码质量和编码规范
        2. 评估代码的可读性和可维护性
        3. 识别潜在的bug和安全问题
        4. 检查错误处理和边界条件
        5. 评估性能和优化机会
        6. 验证单元测试的覆盖率和质量
        7. 提出改进建议
        
        审查标准：
        - 代码符合项目编码规范
        - 逻辑清晰，结构合理
        - 适当的错误处理和日志
        - 充分的测试覆盖
        ''',
        agent=agent,
        expected_output='''
        代码审查报告，包含：
        1. 代码质量评估
        2. 发现的问题和建议
        3. 安全性分析
        4. 性能优化建议
        5. 测试覆盖率分析
        6. 改进后的代码（如需要）
        '''
    )

def create_integration_task(agent, modules_info: str) -> Task:
    """
    创建模块集成任务
    """
    return Task(
        description=f'''
        集成各个开发模块并进行联调：
        
        模块信息：{modules_info}
        
        请完成以下集成工作：
        1. 分析模块间的接口和依赖关系
        2. 编写集成代码和配置
        3. 解决模块间的兼容性问题
        4. 进行集成测试
        5. 优化系统性能
        6. 编写集成文档
        
        集成要求：
        - 确保模块间接口的一致性
        - 处理数据格式转换
        - 实现适当的错误传播机制
        ''',
        agent=agent,
        expected_output='''
        集成结果，包含：
        1. 集成代码和配置
        2. 集成测试报告
        3. 性能测试结果
        4. 问题解决方案
        5. 集成文档
        6. 部署说明
        '''
    )