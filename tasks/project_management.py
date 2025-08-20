from crewai import Task
from agents import create_project_manager
from langchain_google_genai import ChatGoogleGenerativeAI

def create_project_initiation_task(agent, project_description: str, stakeholder_info: str) -> Task:
    """
    创建项目启动任务
    """
    return Task(
        description=f'''
        启动软件开发项目并制定项目章程：
        
        项目描述：{project_description}
        干系人信息：{stakeholder_info}
        
        请完成以下项目启动工作：
        1. 分析项目背景和商业价值
        2. 识别项目干系人和角色
        3. 定义项目范围和边界
        4. 制定项目目标和成功标准
        5. 评估项目风险和约束
        6. 制定项目章程
        7. 组建项目团队
        
        输出要求：
        - 明确项目目标和范围
        - 识别关键风险和缓解措施
        - 建立项目治理结构
        ''',
        agent=agent,
        expected_output='''
        项目章程文档，包含：
        1. 项目概述和背景
        2. 项目目标和成功标准
        3. 项目范围说明
        4. 干系人分析
        5. 风险评估
        6. 项目组织架构
        7. 项目里程碑
        '''
    )

def create_project_planning_task(agent, project_charter: str, team_capacity: str) -> Task:
    """
    创建项目规划任务
    """
    return Task(
        description=f'''
        制定详细的项目执行计划：
        
        项目章程：{project_charter}
        团队能力：{team_capacity}
        
        请完成以下项目规划工作：
        1. 分解项目工作结构（WBS）
        2. 估算任务工作量和持续时间
        3. 制定项目进度计划
        4. 分配资源和责任
        5. 制定质量管理计划
        6. 制定沟通管理计划
        7. 制定风险管理计划
        
        规划要求：
        - 考虑团队能力和资源约束
        - 设置合理的缓冲时间
        - 建立清晰的里程碑
        ''',
        agent=agent,
        expected_output='''
        项目管理计划，包含：
        1. 工作分解结构（WBS）
        2. 项目进度计划
        3. 资源分配计划
        4. 质量管理计划
        5. 沟通计划
        6. 风险管理计划
        7. 变更管理流程
        '''
    )

def create_progress_monitoring_task(agent, project_plan: str, current_status: str) -> Task:
    """
    创建进度监控任务
    """
    return Task(
        description=f'''
        监控项目执行进度并进行状态分析：
        
        项目计划：{project_plan}
        当前状态：{current_status}
        
        请完成以下进度监控工作：
        1. 收集项目执行数据
        2. 分析进度偏差和原因
        3. 评估质量指标和风险状态
        4. 识别问题和障碍
        5. 制定纠正措施
        6. 更新项目预测
        7. 准备状态报告
        
        监控要求：
        - 提供准确的进度数据
        - 识别关键路径风险
        - 提出可行的改进建议
        ''',
        agent=agent,
        expected_output='''
        项目状态报告，包含：
        1. 进度执行情况
        2. 质量指标分析
        3. 风险状态更新
        4. 问题和障碍清单
        5. 纠正措施计划
        6. 项目预测更新
        7. 下阶段重点工作
        '''
    )

def create_risk_management_task(agent, risk_register: str, project_context: str) -> Task:
    """
    创建风险管理任务
    """
    return Task(
        description=f'''
        管理项目风险并制定应对策略：
        
        风险登记册：{risk_register}
        项目环境：{project_context}
        
        请完成以下风险管理工作：
        1. 识别新的项目风险
        2. 评估风险概率和影响
        3. 更新风险优先级
        4. 制定风险应对策略
        5. 监控风险触发条件
        6. 执行风险缓解措施
        7. 更新风险登记册
        
        风险管理要求：
        - 采用定量和定性分析
        - 制定主动和被动应对策略
        - 建立风险预警机制
        ''',
        agent=agent,
        expected_output='''
        风险管理报告，包含：
        1. 风险识别和评估
        2. 风险优先级矩阵
        3. 风险应对策略
        4. 风险监控计划
        5. 应急预案
        6. 风险登记册更新
        7. 风险管理建议
        '''
    )

def create_quality_assurance_task(agent, quality_plan: str, deliverables: str) -> Task:
    """
    创建质量保证任务
    """
    return Task(
        description=f'''
        执行质量保证活动并确保交付质量：
        
        质量计划：{quality_plan}
        项目交付物：{deliverables}
        
        请完成以下质量保证工作：
        1. 执行质量审查和检查
        2. 监控质量指标和趋势
        3. 识别质量问题和根因
        4. 制定质量改进措施
        5. 验证交付物质量
        6. 执行质量培训
        7. 更新质量流程
        
        质量要求：
        - 确保符合质量标准
        - 实施持续改进
        - 建立质量文化
        ''',
        agent=agent,
        expected_output='''
        质量保证报告，包含：
        1. 质量审查结果
        2. 质量指标分析
        3. 问题识别和分析
        4. 改进措施计划
        5. 交付物质量确认
        6. 质量流程优化
        7. 质量管理建议
        '''
    )

def create_stakeholder_communication_task(agent, communication_plan: str, project_updates: str) -> Task:
    """
    创建干系人沟通任务
    """
    return Task(
        description=f'''
        管理干系人沟通并维护项目关系：
        
        沟通计划：{communication_plan}
        项目更新：{project_updates}
        
        请完成以下沟通管理工作：
        1. 分析干系人需求和期望
        2. 准备项目沟通材料
        3. 组织项目会议和汇报
        4. 处理干系人反馈和关切
        5. 管理项目变更请求
        6. 维护项目文档和知识库
        7. 促进团队协作和沟通
        
        沟通要求：
        - 确保信息及时准确
        - 采用合适的沟通方式
        - 建立良好的项目关系
        ''',
        agent=agent,
        expected_output='''
        沟通管理报告，包含：
        1. 干系人满意度分析
        2. 沟通效果评估
        3. 反馈处理情况
        4. 变更请求状态
        5. 团队协作评估
        6. 沟通改进建议
        7. 下期沟通计划
        '''
    )

def create_project_closure_task(agent, project_deliverables: str, lessons_learned: str) -> Task:
    """
    创建项目收尾任务
    """
    return Task(
        description=f'''
        执行项目收尾活动并总结项目经验：
        
        项目交付物：{project_deliverables}
        经验教训：{lessons_learned}
        
        请完成以下项目收尾工作：
        1. 验证项目交付物完整性
        2. 获得客户验收确认
        3. 释放项目资源
        4. 归档项目文档
        5. 总结经验教训
        6. 评估项目成功度
        7. 制定后续支持计划
        
        收尾要求：
        - 确保所有交付物符合要求
        - 完成知识转移
        - 总结最佳实践
        ''',
        agent=agent,
        expected_output='''
        项目收尾报告，包含：
        1. 项目交付确认
        2. 客户验收报告
        3. 项目成功度评估
        4. 经验教训总结
        5. 最佳实践提取
        6. 项目文档归档
        7. 后续支持计划
        '''
    )