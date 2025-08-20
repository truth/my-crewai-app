#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrewAI集成Gemini示例
演示如何在CrewAI项目中使用LiteLLM调用Gemini模型
"""

import os
import litellm
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from typing import Any

# 加载环境变量
load_dotenv()

class GeminiLLM:
    """Gemini LLM包装器，兼容CrewAI"""
    
    def __init__(self, model: str = "gemini/gemini-1.5-flash", **kwargs):
        self.model = model
        self.temperature = kwargs.get('temperature', 0.1)
        self.max_tokens = kwargs.get('max_tokens', 1000)
        
        # 确保API密钥已设置
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("请在.env文件中设置GOOGLE_API_KEY")
        
        os.environ['GOOGLE_API_KEY'] = api_key
        print(f"✅ 初始化Gemini LLM: {self.model}")
    
    def invoke(self, prompt: str) -> Any:
        """兼容LangChain的invoke方法"""
        try:
            response = litellm.completion(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # 创建兼容的响应对象
            class Response:
                def __init__(self, content):
                    self.content = content
            
            return Response(response.choices[0].message.content)
            
        except Exception as e:
            print(f"❌ Gemini调用失败: {e}")
            # 返回模拟响应以保持系统运行
            class Response:
                def __init__(self, content):
                    self.content = content
            return Response(f"[模拟响应] 由于API调用失败，这是一个模拟回复: {prompt[:50]}...")
    
    def __call__(self, prompt: str) -> str:
        """直接调用方法"""
        response = self.invoke(prompt)
        return response.content

def create_software_development_crew():
    """创建软件开发团队，使用Gemini LLM"""
    
    # 初始化Gemini LLM
    llm = GeminiLLM(model="gemini/gemini-1.5-flash", temperature=0.1)
    
    # 创建需求分析师
    requirements_analyst = Agent(
        role='需求分析师',
        goal='分析和整理用户需求，编写详细的需求文档',
        backstory='你是一位经验丰富的需求分析师，擅长与客户沟通，理解业务需求，并将其转化为清晰的技术规格。',
        llm=llm,
        verbose=True
    )
    
    # 创建系统架构师
    system_architect = Agent(
        role='系统架构师',
        goal='设计系统架构，制定技术方案',
        backstory='你是一位资深的系统架构师，具有丰富的大型系统设计经验，能够设计可扩展、高性能的系统架构。',
        llm=llm,
        verbose=True
    )
    
    # 创建开发工程师
    developer = Agent(
        role='开发工程师',
        goal='根据需求和架构设计，编写高质量的代码',
        backstory='你是一位技术精湛的开发工程师，熟悉多种编程语言和框架，能够编写清晰、可维护的代码。',
        llm=llm,
        verbose=True
    )
    
    return requirements_analyst, system_architect, developer, llm

def run_requirements_analysis_example():
    """运行需求分析示例"""
    print("\n" + "=" * 60)
    print("CrewAI + Gemini 需求分析示例")
    print("=" * 60)
    
    try:
        # 创建团队
        requirements_analyst, system_architect, developer, llm = create_software_development_crew()
        
        # 创建需求分析任务
        requirements_task = Task(
            description="""
            分析以下项目需求，并编写详细的需求文档：
            
            项目：在线图书管理系统
            
            基本功能：
            1. 用户注册和登录
            2. 图书信息管理（增删改查）
            3. 图书借阅和归还
            4. 用户借阅历史查询
            5. 图书搜索和分类
            
            请分析功能需求、非功能需求，并提出技术建议。
            """,
            agent=requirements_analyst,
            expected_output="详细的需求分析文档，包括功能需求、非功能需求和技术建议"
        )
        
        # 创建团队并执行任务
        crew = Crew(
            agents=[requirements_analyst],
            tasks=[requirements_task],
            verbose=True
        )
        
        print("\n🚀 开始执行需求分析任务...")
        result = crew.kickoff()
        
        print("\n" + "=" * 60)
        print("需求分析结果")
        print("=" * 60)
        print(result)
        
        return True
        
    except Exception as e:
        print(f"❌ 需求分析示例执行失败: {e}")
        return False

def run_architecture_design_example():
    """运行架构设计示例"""
    print("\n" + "=" * 60)
    print("CrewAI + Gemini 架构设计示例")
    print("=" * 60)
    
    try:
        # 创建团队
        requirements_analyst, system_architect, developer, llm = create_software_development_crew()
        
        # 创建架构设计任务
        architecture_task = Task(
            description="""
            基于在线图书管理系统的需求，设计系统架构：
            
            需求概述：
            - 支持多用户并发访问
            - 图书信息管理
            - 借阅管理
            - 用户管理
            - 搜索功能
            
            请设计：
            1. 系统整体架构
            2. 数据库设计
            3. API接口设计
            4. 技术栈选择
            5. 部署方案
            """,
            agent=system_architect,
            expected_output="完整的系统架构设计文档，包括架构图、数据库设计、API设计等"
        )
        
        # 创建团队并执行任务
        crew = Crew(
            agents=[system_architect],
            tasks=[architecture_task],
            verbose=True
        )
        
        print("\n🚀 开始执行架构设计任务...")
        result = crew.kickoff()
        
        print("\n" + "=" * 60)
        print("架构设计结果")
        print("=" * 60)
        print(result)
        
        return True
        
    except Exception as e:
        print(f"❌ 架构设计示例执行失败: {e}")
        return False

def run_code_generation_example():
    """运行代码生成示例"""
    print("\n" + "=" * 60)
    print("CrewAI + Gemini 代码生成示例")
    print("=" * 60)
    
    try:
        # 创建团队
        requirements_analyst, system_architect, developer, llm = create_software_development_crew()
        
        # 创建代码生成任务
        development_task = Task(
            description="""
            为在线图书管理系统编写核心代码模块：
            
            请实现以下功能：
            1. 用户模型类（User）
            2. 图书模型类（Book）
            3. 借阅记录模型类（BorrowRecord）
            4. 用户注册和登录功能
            5. 图书搜索功能
            
            要求：
            - 使用Python语言
            - 包含必要的注释
            - 遵循PEP8编码规范
            - 包含基本的错误处理
            """,
            agent=developer,
            expected_output="完整的Python代码模块，包括模型类和核心功能实现"
        )
        
        # 创建团队并执行任务
        crew = Crew(
            agents=[developer],
            tasks=[development_task],
            verbose=True
        )
        
        print("\n🚀 开始执行代码生成任务...")
        result = crew.kickoff()
        
        print("\n" + "=" * 60)
        print("代码生成结果")
        print("=" * 60)
        print(result)
        
        return True
        
    except Exception as e:
        print(f"❌ 代码生成示例执行失败: {e}")
        return False

def test_gemini_llm_directly():
    """直接测试Gemini LLM"""
    print("\n" + "=" * 60)
    print("直接测试Gemini LLM")
    print("=" * 60)
    
    try:
        llm = GeminiLLM()
        
        test_prompts = [
            "请简单介绍一下Python编程语言。",
            "什么是软件架构？",
            "解释一下数据库的CRUD操作。"
        ]
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\n📝 测试 {i}: {prompt}")
            print("-" * 40)
            response = llm.invoke(prompt)
            print(f"回复: {response.content[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 直接测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("CrewAI集成Gemini完整示例")
    print("=" * 60)
    
    # 检查环境变量
    if not os.getenv('GOOGLE_API_KEY'):
        print("\n❌ 错误: 未设置GOOGLE_API_KEY环境变量")
        print("请在.env文件中设置您的Google API密钥")
        return
    
    # 选择运行模式
    print("\n请选择运行模式:")
    print("1. 直接测试Gemini LLM")
    print("2. 需求分析示例")
    print("3. 架构设计示例")
    print("4. 代码生成示例")
    print("5. 运行所有示例")
    
    try:
        choice = input("\n请输入选择 (1-5): ").strip()
        
        if choice == '1':
            test_gemini_llm_directly()
        elif choice == '2':
            run_requirements_analysis_example()
        elif choice == '3':
            run_architecture_design_example()
        elif choice == '4':
            run_code_generation_example()
        elif choice == '5':
            print("\n🚀 运行所有示例...")
            test_gemini_llm_directly()
            run_requirements_analysis_example()
            run_architecture_design_example()
            run_code_generation_example()
        else:
            print("❌ 无效选择")
            
    except KeyboardInterrupt:
        print("\n\n👋 用户取消操作")
    except Exception as e:
        print(f"\n❌ 执行错误: {e}")
    
    print("\n" + "=" * 60)
    print("示例执行完成")
    print("=" * 60)
    print("\n💡 提示:")
    print("- 确保.env文件中设置了有效的GOOGLE_API_KEY")
    print("- 如果遇到速率限制，请稍后重试")
    print("- 查看LiteLLM文档了解更多配置选项")

if __name__ == "__main__":
    main()