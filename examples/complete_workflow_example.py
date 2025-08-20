#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整软件开发工作流示例

本示例展示如何使用CrewAI软件开发全流程管理系统
从项目启动到部署的完整流程。
"""

import os
# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理
from workflows import create_software_development_workflow

def main():
    """
    运行完整的软件开发工作流示例
    """
    # 创建LLM实例（支持多种提供商）
    llm = None
    try:
        if os.getenv("GOOGLE_API_KEY"):
            llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                temperature=0.7,
                google_api_key=os.getenv("GOOGLE_API_KEY")
            )
    except:
        pass
    
    if llm is None:
        try:
            if os.getenv("OPENAI_API_KEY"):
                llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.7,
                    openai_api_key=os.getenv("OPENAI_API_KEY")
                )
        except:
            pass
    
    if llm is None:
        print("⚠️  未找到可用的LLM提供商，使用模拟模式")
        # 这里可以使用模拟LLM或退出
        return
    
    # 创建工作流实例
    workflow = create_software_development_workflow(llm)
    
    # 项目描述
    project_description = """
    开发一个在线图书管理系统，主要功能包括：
    1. 用户注册和登录
    2. 图书信息管理（增删改查）
    3. 图书借阅和归还
    4. 用户借阅历史查询
    5. 图书推荐系统
    6. 管理员后台管理
    
    技术要求：
    - 前端使用React.js
    - 后端使用Python Flask
    - 数据库使用PostgreSQL
    - 支持RESTful API
    - 需要用户认证和授权
    - 响应式设计，支持移动端
    """
    
    print("=" * 80)
    print("CrewAI 软件开发全流程管理系统示例")
    print("=" * 80)
    
    try:
        # 阶段1: 项目启动
        print("\n🚀 阶段1: 项目启动")
        print("-" * 40)
        initiation_crew = workflow.create_project_initiation_crew(
            project_description=project_description,
            stakeholder_info="产品经理、开发团队、测试团队、运维团队"
        )
        initiation_result = initiation_crew.kickoff()
        print(f"项目启动结果:\n{initiation_result}")
        
        # 阶段2: 需求分析
        print("\n📋 阶段2: 需求分析")
        print("-" * 40)
        requirements_crew = workflow.create_requirements_analysis_crew(
            project_description=project_description
        )
        requirements_result = requirements_crew.kickoff()
        print(f"需求分析结果:\n{requirements_result}")
        
        # 阶段3: 系统设计
        print("\n🏗️ 阶段3: 系统设计")
        print("-" * 40)
        design_crew = workflow.create_system_design_crew(
            requirements_doc=str(requirements_result)
        )
        design_result = design_crew.kickoff()
        print(f"系统设计结果:\n{design_result}")
        
        # 阶段4: 开发规划
        print("\n💻 阶段4: 开发规划")
        print("-" * 40)
        development_crew = workflow.create_development_crew(
            technical_spec=str(design_result)
        )
        development_result = development_crew.kickoff()
        print(f"开发规划结果:\n{development_result}")
        
        # 阶段5: 测试规划
        print("\n🧪 阶段5: 测试规划")
        print("-" * 40)
        testing_crew = workflow.create_testing_crew(
            requirements_doc=str(requirements_result),
            architecture_doc=str(design_result)
        )
        testing_result = testing_crew.kickoff()
        print(f"测试规划结果:\n{testing_result}")
        
        # 阶段6: 部署规划
        print("\n🚀 阶段6: 部署规划")
        print("-" * 40)
        deployment_crew = workflow.create_deployment_crew(
            architecture_doc=str(design_result),
            environment_requirements="云平台部署，支持自动扩缩容，高可用架构"
        )
        deployment_result = deployment_crew.kickoff()
        print(f"部署规划结果:\n{deployment_result}")
        
        print("\n✅ 软件开发全流程规划完成！")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ 执行过程中出现错误: {e}")
        print("请检查API密钥配置和网络连接")

def run_complete_workflow_example(llm):
    """
    运行完整工作流示例
    """
    return main()

def run_single_stage_example(llm, stage: str = "requirements"):
    """
    运行单阶段示例
    """
    return run_single_phase_example()

def run_single_phase_example():
    """
    运行单个阶段的示例
    """
    # 创建LLM实例（支持多种提供商）
    llm = None
    try:
        if os.getenv("GOOGLE_API_KEY"):
            llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                temperature=0.7,
                google_api_key=os.getenv("GOOGLE_API_KEY")
            )
    except:
        pass
    
    if llm is None:
        try:
            if os.getenv("OPENAI_API_KEY"):
                llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.7,
                    openai_api_key=os.getenv("OPENAI_API_KEY")
                )
        except:
            pass
    
    if llm is None:
        print("⚠️  未找到可用的LLM提供商，使用模拟模式")
        return
    
    # 创建工作流
    workflow = create_software_development_workflow(llm)
    
    # 简单的项目描述
    simple_project = "开发一个简单的待办事项管理应用，支持任务的增删改查功能。"
    
    print("\n🔍 单阶段示例: 需求分析")
    print("-" * 40)
    
    try:
        # 只运行需求分析阶段
        requirements_crew = workflow.create_requirements_analysis_crew(
            project_description=simple_project
        )
        result = requirements_crew.kickoff()
        print(f"需求分析结果:\n{result}")
        
    except Exception as e:
        print(f"❌ 执行错误: {e}")

if __name__ == "__main__":
    # 检查API密钥
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ 请设置GOOGLE_API_KEY环境变量")
        print("   export GOOGLE_API_KEY='your-api-key'")
        exit(1)
    
    # 运行示例
    print("选择运行模式:")
    print("1. 完整工作流示例")
    print("2. 单阶段示例")
    
    choice = input("请输入选择 (1 或 2): ").strip()
    
    if choice == "1":
        main()
    elif choice == "2":
        run_single_phase_example()
    else:
        print("无效选择，运行单阶段示例")
        run_single_phase_example()