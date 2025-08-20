#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrewAI 软件开发全流程管理系统

主程序入口，提供多种运行模式：
1. 完整软件开发工作流
2. 单个阶段执行
3. 自定义工作流
"""

import os
import sys
from typing import Optional

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from crewai import Crew
    # 尝试导入Google Gemini，如果失败则使用OpenAI
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        LLM_PROVIDER = "google"
    except ImportError:
        try:
            from langchain_openai import ChatOpenAI
            LLM_PROVIDER = "openai"
        except ImportError:
            print("警告: 未找到支持的LLM提供商，将使用模拟模式")
            LLM_PROVIDER = "mock"
except ImportError as e:
    print(f"导入错误: {e}")
    print("请确保已安装所需依赖: pip install crewai")
    sys.exit(1)

from config import Config
from workflows import create_software_development_workflow
from examples.complete_workflow_example import run_complete_workflow_example, run_single_stage_example

class MockLLM:
    """模拟LLM用于测试"""
    def __init__(self):
        self.model_name = "mock-llm"
    
    def invoke(self, prompt):
        return "这是一个模拟响应，用于测试系统架构。在实际使用中，请配置真实的LLM API密钥。"
    
    def __call__(self, prompt):
        return self.invoke(prompt)

def check_environment():
    """
    检查运行环境
    """
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
        print("请设置您的Google API密钥:")
        print("   Windows: set GOOGLE_API_KEY=your-api-key")
        print("   Linux/Mac: export GOOGLE_API_KEY='your-api-key'")
        return False
    return True

def create_llm():
    """
    创建语言模型实例
    """
    if LLM_PROVIDER == "google":
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 未设置GOOGLE_API_KEY环境变量")
            print("请设置您的Google API密钥:")
            print("Windows: set GOOGLE_API_KEY=your-api-key")
            print("Linux/Mac: export GOOGLE_API_KEY='your-api-key'")
            return None
        
        try:
            llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                temperature=0.7,
                google_api_key=api_key
            )
            print("✅ Google Gemini LLM 初始化成功")
            return llm
        except Exception as e:
            print(f"❌ Google Gemini LLM初始化失败: {e}")
            return None
    
    elif LLM_PROVIDER == "openai":
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ 未设置OPENAI_API_KEY环境变量")
            print("请设置您的OpenAI API密钥:")
            print("Windows: set OPENAI_API_KEY=your-api-key")
            print("Linux/Mac: export OPENAI_API_KEY='your-api-key'")
            return None
        
        try:
            llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0.7,
                openai_api_key=api_key
            )
            print("✅ OpenAI LLM 初始化成功")
            return llm
        except Exception as e:
            print(f"❌ OpenAI LLM初始化失败: {e}")
            return None
    
    else:
        print("⚠️  使用模拟模式 - 仅用于测试")
        return MockLLM()

def run_demo_project():
    """
    运行演示项目
    """
    print("\n🚀 运行CrewAI软件开发工作流演示")
    print("=" * 60)
    
    # 创建模型和工作流
    llm = create_llm()
    workflow = create_software_development_workflow(llm)
    
    # 演示项目描述
    demo_project = """
    开发一个个人博客系统，主要功能包括：
    1. 用户注册和登录
    2. 文章发布和编辑
    3. 文章分类和标签
    4. 评论系统
    5. 搜索功能
    6. 响应式设计
    
    技术栈：
    - 前端：React.js + TypeScript
    - 后端：Node.js + Express
    - 数据库：MongoDB
    - 部署：Docker + AWS
    """
    
    try:
        # 运行需求分析阶段
        print("\n📋 执行需求分析...")
        requirements_crew = workflow.create_requirements_analysis_crew(
            project_description=demo_project
        )
        requirements_result = requirements_crew.kickoff()
        
        print("\n✅ 需求分析完成！")
        print("\n" + "="*60)
        print("需求分析结果:")
        print("="*60)
        print(requirements_result)
        
        return str(requirements_result)
        
    except Exception as e:
        print(f"❌ 执行失败: {e}")
        return None

def run_interactive_mode():
    """
    交互式模式
    """
    print("\n🎯 CrewAI 交互式模式")
    print("=" * 40)
    
    # 获取用户输入
    project_description = input("请描述您的项目需求: ")
    
    if not project_description.strip():
        print("❌ 项目描述不能为空")
        return
    
    # 选择执行阶段
    print("\n请选择要执行的阶段:")
    print("1. 项目启动")
    print("2. 需求分析")
    print("3. 系统设计")
    print("4. 开发规划")
    print("5. 测试规划")
    print("6. 部署规划")
    
    choice = input("请输入选择 (1-6): ").strip()
    
    # 创建工作流
    llm = create_llm()
    workflow = create_software_development_workflow(llm)
    
    try:
        if choice == "1":
            crew = workflow.create_project_initiation_crew(project_description)
        elif choice == "2":
            crew = workflow.create_requirements_analysis_crew(project_description)
        elif choice == "3":
            crew = workflow.create_system_design_crew(project_description)
        elif choice == "4":
            crew = workflow.create_development_crew(project_description)
        elif choice == "5":
            crew = workflow.create_testing_crew(project_description, "")
        elif choice == "6":
            crew = workflow.create_deployment_crew(project_description)
        else:
            print("❌ 无效选择")
            return
        
        print(f"\n🚀 执行阶段 {choice}...")
        result = crew.kickoff()
        
        print("\n✅ 执行完成！")
        print("\n" + "="*60)
        print("执行结果:")
        print("="*60)
        print(result)
        
    except Exception as e:
        print(f"❌ 执行失败: {e}")

def show_menu():
    """
    显示主菜单
    """
    print("\n" + "="*60)
    print("    CrewAI 软件开发全流程管理系统")
    print("="*60)
    print("1. 运行演示项目 (推荐)")
    print("2. 交互式模式")
    print("3. 查看系统信息")
    print("4. 退出")
    print("="*60)

def show_system_info():
    """
    显示系统信息
    """
    print("\n📊 系统信息")
    print("-" * 40)
    print(f"Python版本: {sys.version}")
    print(f"工作目录: {os.getcwd()}")
    print(f"API密钥状态: {'✅ 已配置' if os.getenv('GOOGLE_API_KEY') else '❌ 未配置'}")
    
    # 显示智能体信息
    print("\n🤖 可用智能体:")
    agents = [
        "项目经理 - 项目协调和管理",
        "需求分析师 - 需求收集和分析", 
        "系统架构师 - 架构设计和技术选型",
        "开发工程师 - 代码实现和开发",
        "测试工程师 - 测试规划和执行",
        "DevOps工程师 - 部署和运维"
    ]
    
    for agent in agents:
        print(f"  • {agent}")

def main():
    """
    主程序入口
    """
    # 检查环境
    if not check_environment():
        return
    
    while True:
        show_menu()
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == "1":
            run_demo_project()
        elif choice == "2":
            run_interactive_mode()
        elif choice == "3":
            show_system_info()
        elif choice == "4":
            print("\n👋 感谢使用CrewAI软件开发管理系统！")
            break
        else:
            print("❌ 无效选择，请重新输入")
        
        input("\n按回车键继续...")

if __name__ == "__main__":
    # 设置Google API密钥环境变量
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBgwJ43oFRLQweegXgj1OXgIbg1g8kz5Do"
    main()
