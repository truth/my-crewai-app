from crewai import Task
from agents import create_test_engineer
# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理

def create_test_planning_task(agent, requirements_doc: str, architecture_doc: str) -> Task:
    """
    创建测试计划任务
    """
    return Task(
        description=f'''
        基于需求文档和架构设计制定全面的测试计划：
        
        需求文档：{requirements_doc}
        架构文档：{architecture_doc}
        
        请完成以下测试规划工作：
        1. 分析需求和架构，识别测试范围
        2. 制定测试策略和测试方法
        3. 设计测试用例结构和测试数据
        4. 规划各种测试类型（单元、集成、系统、验收）
        5. 确定测试环境和工具需求
        6. 制定测试时间表和里程碑
        7. 识别测试风险和缓解措施
        
        输出要求：
        - 覆盖所有功能和非功能需求
        - 考虑各种异常场景和边界条件
        - 制定合理的测试优先级
        ''',
        agent=agent,
        expected_output='''
        测试计划文档，包含：
        1. 测试策略和方法
        2. 测试范围和边界
        3. 测试用例设计规范
        4. 测试环境配置
        5. 测试工具和框架选择
        6. 测试时间表
        7. 风险评估和缓解计划
        '''
    )

def create_test_case_design_task(agent, test_plan: str, module_spec: str) -> Task:
    """
    创建测试用例设计任务
    """
    return Task(
        description=f'''
        基于测试计划和模块规格设计详细的测试用例：
        
        测试计划：{test_plan}
        模块规格：{module_spec}
        
        请完成以下测试用例设计工作：
        1. 设计功能测试用例
        2. 设计边界值和异常测试用例
        3. 设计性能测试用例
        4. 设计安全测试用例
        5. 设计兼容性测试用例
        6. 准备测试数据和测试环境
        7. 编写自动化测试脚本
        
        测试用例要求：
        - 包含清晰的前置条件和预期结果
        - 覆盖正常流程和异常流程
        - 可执行且可重复
        ''',
        agent=agent,
        expected_output='''
        测试用例文档，包含：
        1. 功能测试用例集
        2. 性能测试用例
        3. 安全测试用例
        4. 自动化测试脚本
        5. 测试数据准备
        6. 测试环境配置说明
        7. 执行指南
        '''
    )

def create_test_execution_task(agent, test_cases: str, code_version: str) -> Task:
    """
    创建测试执行任务
    """
    return Task(
        description=f'''
        执行测试用例并记录测试结果：
        
        测试用例：{test_cases}
        代码版本：{code_version}
        
        请完成以下测试执行工作：
        1. 搭建和配置测试环境
        2. 执行功能测试用例
        3. 执行性能和压力测试
        4. 执行安全测试
        5. 记录测试结果和缺陷
        6. 分析测试覆盖率
        7. 生成测试报告
        
        执行要求：
        - 严格按照测试用例步骤执行
        - 详细记录测试过程和结果
        - 及时报告发现的缺陷
        ''',
        agent=agent,
        expected_output='''
        测试执行报告，包含：
        1. 测试执行摘要
        2. 测试结果统计
        3. 缺陷报告和分析
        4. 测试覆盖率报告
        5. 性能测试结果
        6. 风险评估
        7. 改进建议
        '''
    )

def create_regression_testing_task(agent, previous_results: str, new_changes: str) -> Task:
    """
    创建回归测试任务
    """
    return Task(
        description=f'''
        对系统变更进行回归测试：
        
        之前测试结果：{previous_results}
        新的变更：{new_changes}
        
        请完成以下回归测试工作：
        1. 分析变更影响范围
        2. 选择相关的回归测试用例
        3. 执行回归测试
        4. 对比测试结果
        5. 验证缺陷修复情况
        6. 评估系统稳定性
        
        回归测试要求：
        - 重点关注变更相关功能
        - 验证核心功能未受影响
        - 确保修复的缺陷不再出现
        ''',
        agent=agent,
        expected_output='''
        回归测试报告，包含：
        1. 变更影响分析
        2. 回归测试结果
        3. 缺陷修复验证
        4. 系统稳定性评估
        5. 风险评估
        6. 发布建议
        '''
    )

def create_performance_testing_task(agent, performance_requirements: str, system_architecture: str) -> Task:
    """
    创建性能测试任务
    """
    return Task(
        description=f'''
        进行系统性能测试和优化：
        
        性能需求：{performance_requirements}
        系统架构：{system_architecture}
        
        请完成以下性能测试工作：
        1. 设计性能测试场景
        2. 配置性能测试环境
        3. 执行负载测试和压力测试
        4. 监控系统资源使用情况
        5. 分析性能瓶颈
        6. 提出性能优化建议
        7. 验证优化效果
        
        性能测试要求：
        - 模拟真实用户场景
        - 测试系统极限能力
        - 识别性能瓶颈点
        ''',
        agent=agent,
        expected_output='''
        性能测试报告，包含：
        1. 性能测试结果
        2. 系统资源分析
        3. 性能瓶颈识别
        4. 优化建议
        5. 容量规划建议
        6. 监控指标定义
        '''
    )