from crewai import Task
from agents import create_devops_engineer
from langchain_google_genai import ChatGoogleGenerativeAI

def create_deployment_planning_task(agent, architecture_doc: str, environment_requirements: str) -> Task:
    """
    创建部署规划任务
    """
    return Task(
        description=f'''
        基于系统架构和环境需求制定部署方案：
        
        系统架构：{architecture_doc}
        环境需求：{environment_requirements}
        
        请完成以下部署规划工作：
        1. 分析系统架构和部署需求
        2. 设计部署架构和环境拓扑
        3. 选择合适的部署平台和工具
        4. 制定容器化和编排策略
        5. 设计CI/CD流水线
        6. 规划监控和日志系统
        7. 制定安全和备份策略
        
        输出要求：
        - 提供详细的部署架构图
        - 考虑高可用和扩展性
        - 制定合理的资源配置
        ''',
        agent=agent,
        expected_output='''
        部署方案文档，包含：
        1. 部署架构设计
        2. 环境配置规范
        3. 容器化方案
        4. CI/CD流水线设计
        5. 监控和日志方案
        6. 安全配置
        7. 运维手册
        '''
    )

def create_cicd_setup_task(agent, deployment_plan: str, code_repository: str) -> Task:
    """
    创建CI/CD流水线搭建任务
    """
    return Task(
        description=f'''
        基于部署方案搭建CI/CD流水线：
        
        部署方案：{deployment_plan}
        代码仓库：{code_repository}
        
        请完成以下CI/CD搭建工作：
        1. 配置代码仓库和分支策略
        2. 设置自动化构建流程
        3. 配置自动化测试集成
        4. 设置代码质量检查
        5. 配置自动化部署流程
        6. 设置环境管理和配置
        7. 配置通知和报告机制
        
        CI/CD要求：
        - 支持多环境部署
        - 实现自动化测试集成
        - 提供回滚机制
        ''',
        agent=agent,
        expected_output='''
        CI/CD配置文件和文档，包含：
        1. 流水线配置文件
        2. 构建脚本
        3. 部署脚本
        4. 环境配置文件
        5. 质量门禁配置
        6. 监控和通知配置
        7. 操作手册
        '''
    )

def create_infrastructure_setup_task(agent, deployment_architecture: str) -> Task:
    """
    创建基础设施搭建任务
    """
    return Task(
        description=f'''
        基于部署架构搭建基础设施：
        
        部署架构：{deployment_architecture}
        
        请完成以下基础设施搭建工作：
        1. 配置云平台资源
        2. 设置网络和安全组
        3. 配置负载均衡器
        4. 设置数据库和存储
        5. 配置容器编排平台
        6. 设置监控和日志系统
        7. 配置备份和灾备
        
        基础设施要求：
        - 使用基础设施即代码（IaC）
        - 确保高可用性
        - 实现自动扩缩容
        ''',
        agent=agent,
        expected_output='''
        基础设施配置，包含：
        1. IaC配置文件（Terraform/CloudFormation）
        2. 容器编排配置（Kubernetes/Docker Compose）
        3. 网络和安全配置
        4. 监控配置文件
        5. 备份策略配置
        6. 运维脚本
        7. 部署文档
        '''
    )

def create_monitoring_setup_task(agent, system_architecture: str, performance_requirements: str) -> Task:
    """
    创建监控系统搭建任务
    """
    return Task(
        description=f'''
        搭建全面的系统监控和告警体系：
        
        系统架构：{system_architecture}
        性能需求：{performance_requirements}
        
        请完成以下监控系统搭建工作：
        1. 设计监控架构和指标体系
        2. 配置应用性能监控（APM）
        3. 设置基础设施监控
        4. 配置日志收集和分析
        5. 设置告警规则和通知
        6. 创建监控仪表板
        7. 制定故障响应流程
        
        监控要求：
        - 覆盖应用和基础设施
        - 提供实时告警
        - 支持故障排查
        ''',
        agent=agent,
        expected_output='''
        监控系统配置，包含：
        1. 监控架构设计
        2. 监控工具配置
        3. 告警规则配置
        4. 仪表板配置
        5. 日志配置
        6. 故障响应手册
        7. 运维指南
        '''
    )

def create_security_hardening_task(agent, security_requirements: str, deployment_config: str) -> Task:
    """
    创建安全加固任务
    """
    return Task(
        description=f'''
        对部署环境进行安全加固：
        
        安全需求：{security_requirements}
        部署配置：{deployment_config}
        
        请完成以下安全加固工作：
        1. 配置网络安全策略
        2. 设置身份认证和授权
        3. 配置数据加密
        4. 设置安全扫描和检测
        5. 配置访问控制和审计
        6. 设置安全备份和恢复
        7. 制定安全应急响应计划
        
        安全要求：
        - 遵循安全最佳实践
        - 实现纵深防御
        - 支持合规审计
        ''',
        agent=agent,
        expected_output='''
        安全配置文档，包含：
        1. 安全策略配置
        2. 认证授权配置
        3. 加密配置
        4. 安全扫描配置
        5. 审计日志配置
        6. 应急响应计划
        7. 安全运维手册
        '''
    )

def create_production_deployment_task(agent, deployment_package: str, environment_config: str) -> Task:
    """
    创建生产环境部署任务
    """
    return Task(
        description=f'''
        执行生产环境部署：
        
        部署包：{deployment_package}
        环境配置：{environment_config}
        
        请完成以下生产部署工作：
        1. 验证部署前置条件
        2. 执行数据库迁移
        3. 部署应用服务
        4. 配置负载均衡
        5. 执行部署后验证
        6. 配置监控和告警
        7. 准备回滚方案
        
        部署要求：
        - 确保零停机部署
        - 验证所有功能正常
        - 准备应急预案
        ''',
        agent=agent,
        expected_output='''
        部署执行报告，包含：
        1. 部署执行日志
        2. 验证测试结果
        3. 性能基准测试
        4. 监控配置确认
        5. 回滚方案
        6. 运维交接文档
        7. 上线检查清单
        '''
    )