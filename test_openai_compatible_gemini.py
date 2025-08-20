#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenAI兼容模式调用Gemini测试
演示如何通过OpenAI兼容接口调用Google Gemini模型
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_openai_compatible_gemini():
    """测试通过OpenAI兼容接口调用Gemini"""
    try:
        from langchain_openai import ChatOpenAI
        
        # 检查Google API密钥
        google_api_key = os.getenv('GOOGLE_API_KEY')
        if not google_api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            print("请在.env文件中设置: GOOGLE_API_KEY=your_google_api_key")
            return False
            
        print(f"✅ 找到Google API密钥: {google_api_key[:10]}...")
        
        # 使用OpenAI兼容接口调用Gemini
        # 通过LiteLLM代理或其他OpenAI兼容服务
        llm = ChatOpenAI(
            model="gemini-1.5-flash",  # 使用可用的Gemini模型
            api_key=google_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Google的OpenAI兼容端点
            temperature=0.1
        )
        
        print("✅ OpenAI兼容Gemini LLM初始化成功")
        
        # 测试调用
        response = llm.invoke("你好，请简单介绍一下你自己。")
        print(f"✅ 测试调用成功: {response.content[:100]}...")
        
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请安装: pip install langchain-openai")
        return False
    except Exception as e:
        print(f"❌ 调用错误: {e}")
        return False

def test_litellm_openai_compatible():
    """测试通过LiteLLM的OpenAI兼容模式调用Gemini"""
    try:
        import litellm
        from openai import OpenAI
        
        # 检查API密钥
        google_api_key = os.getenv('GOOGLE_API_KEY')
        if not google_api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        # 设置环境变量
        os.environ['GOOGLE_API_KEY'] = google_api_key
        
        print("✅ 开始测试LiteLLM OpenAI兼容模式...")
        
        # 方法1: 直接使用LiteLLM
        try:
            response = litellm.completion(
                model="gemini/gemini-1.5-flash",  # 使用可用的Gemini模型
                messages=[
                    {"role": "user", "content": "你好，请简单介绍一下你自己。"}
                ],
                temperature=0.1
            )
            print(f"✅ LiteLLM直接调用成功: {response.choices[0].message.content[:100]}...")
        except Exception as e:
            print(f"⚠️ LiteLLM直接调用失败: {e}")
        
        # 方法2: 通过OpenAI客户端使用LiteLLM代理
        try:
            # 启动LiteLLM代理服务器（需要单独运行）
            client = OpenAI(
                api_key=google_api_key,
                base_url="http://localhost:4000"  # LiteLLM代理服务器地址
            )
            
            response = client.chat.completions.create(
                model="gemini-pro",
                messages=[
                    {"role": "user", "content": "你好，请简单介绍一下你自己。"}
                ],
                temperature=0.1
            )
            print(f"✅ OpenAI客户端通过LiteLLM代理调用成功: {response.choices[0].message.content[:100]}...")
        except Exception as e:
            print(f"⚠️ OpenAI客户端通过LiteLLM代理调用失败: {e}")
            print("提示: 需要先启动LiteLLM代理服务器")
        
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请安装: pip install litellm openai")
        return False
    except Exception as e:
        print(f"❌ 调用错误: {e}")
        return False

def test_crewai_openai_compatible():
    """测试CrewAI中使用OpenAI兼容模式调用Gemini"""
    try:
        from langchain_openai import ChatOpenAI
        
        # 检查API密钥
        google_api_key = os.getenv('GOOGLE_API_KEY')
        if not google_api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        print("✅ 开始测试CrewAI OpenAI兼容模式...")
        
        # 配置OpenAI兼容的Gemini LLM
        llm = ChatOpenAI(
            model="gemini-1.5-flash",
            api_key=google_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            temperature=0.1,
            max_tokens=1000
        )
        
        print("✅ CrewAI兼容LLM配置成功")
        
        # 测试调用
        response = llm.invoke("请用中文简单介绍一下人工智能的发展历程。")
        print(f"✅ CrewAI兼容模式测试成功: {response.content[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ CrewAI兼容性测试错误: {e}")
        return False

def create_env_template():
    """创建环境变量模板"""
    env_template = """
# Google AI API密钥
GOOGLE_API_KEY=your_google_api_key_here

# OpenAI API密钥（可选，作为备选）
OPENAI_API_KEY=your_openai_api_key_here

# LiteLLM配置（可选）
LITELLM_LOG=INFO
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_template.strip())
        print("✅ 已创建.env模板文件")
    else:
        print("ℹ️ .env文件已存在")

def show_usage_examples():
    """显示使用示例"""
    print("\n" + "=" * 60)
    print("OpenAI兼容模式调用Gemini的使用示例")
    print("=" * 60)
    
    examples = [
        {
            "title": "1. 直接使用LangChain OpenAI",
            "code": """
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gemini-pro",
    api_key="your_google_api_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    temperature=0.1
)

response = llm.invoke("你好，世界！")
print(response.content)
"""
        },
        {
            "title": "2. 使用LiteLLM",
            "code": """
import litellm
import os

os.environ['GOOGLE_API_KEY'] = 'your_google_api_key'

response = litellm.completion(
    model="gemini/gemini-pro",
    messages=[{"role": "user", "content": "你好，世界！"}]
)

print(response.choices[0].message.content)
"""
        },
        {
            "title": "3. 在CrewAI中使用",
            "code": """
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# 配置LLM
llm = ChatOpenAI(
    model="gemini-pro",
    api_key=os.getenv('GOOGLE_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 创建智能体
agent = Agent(
    role='助手',
    goal='帮助用户解决问题',
    backstory='我是一个有用的AI助手',
    llm=llm
)

# 创建任务
task = Task(
    description='回答用户的问题',
    agent=agent
)

# 创建团队
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
"""
        }
    ]
    
    for example in examples:
        print(f"\n{example['title']}:")
        print("-" * 40)
        print(example['code'])

def main():
    """主测试函数"""
    print("=" * 60)
    print("OpenAI兼容模式调用Gemini测试")
    print("=" * 60)
    
    # 创建环境变量模板
    create_env_template()
    
    # 检查环境变量
    if not os.getenv('GOOGLE_API_KEY'):
        print("\n⚠️  警告: 未设置GOOGLE_API_KEY环境变量")
        print("请在.env文件中设置您的Google API密钥")
        print()
    
    tests = [
        ("OpenAI兼容接口调用Gemini", test_openai_compatible_gemini),
        ("LiteLLM OpenAI兼容模式", test_litellm_openai_compatible),
        ("CrewAI OpenAI兼容模式", test_crewai_openai_compatible)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name}")
        print("-" * 40)
        result = test_func()
        results.append((test_name, result))
        print()
    
    # 总结
    print("=" * 60)
    print("测试结果总结")
    print("=" * 60)
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{status} {test_name}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"\n总计: {passed}/{total} 个测试通过")
    
    # 显示使用示例
    show_usage_examples()
    
    if passed == 0:
        print("\n💡 故障排除建议:")
        print("1. 确保已安装必要的包: pip install langchain-openai litellm")
        print("2. 在.env文件中设置GOOGLE_API_KEY")
        print("3. 检查API密钥是否有效")
        print("4. 确保网络连接正常")
        print("5. 检查Google AI Studio是否启用了API访问")

if __name__ == "__main__":
    main()