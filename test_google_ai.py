#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google AI 调用测试用例
用于验证Google Generative AI的正确配置和调用方式
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_google_ai_basic():
    """测试基本的Google AI调用"""
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        # 检查API密钥
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            print("请在.env文件中设置: GOOGLE_API_KEY=your_api_key_here")
            return False
            
        print(f"✅ 找到Google API密钥: {api_key[:10]}...")
        
        # 初始化LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=api_key,
            temperature=0.1
        )
        
        print("✅ Google Generative AI LLM初始化成功")
        
        # 测试简单调用
        response = llm.invoke("你好，请简单介绍一下你自己。")
        print(f"✅ 测试调用成功: {response.content[:100]}...")
        
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请安装: pip install langchain-google-genai")
        return False
    except Exception as e:
        print(f"❌ 调用错误: {e}")
        return False

def test_litellm_google_ai():
    """测试通过LiteLLM调用Google AI"""
    try:
        import litellm
        
        # 检查API密钥
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        # 设置LiteLLM的Google API密钥
        os.environ['GOOGLE_API_KEY'] = api_key
        
        print("✅ 开始测试LiteLLM Google AI调用...")
        
        # 使用正确的模型名称格式
        response = litellm.completion(
            model="gemini/gemini-pro",  # 正确的LiteLLM格式
            messages=[
                {"role": "user", "content": "你好，请简单介绍一下你自己。"}
            ],
            temperature=0.1
        )
        
        print(f"✅ LiteLLM调用成功: {response.choices[0].message.content[:100]}...")
        return True
        
    except ImportError as e:
        print(f"❌ LiteLLM导入错误: {e}")
        print("请安装: pip install litellm")
        return False
    except Exception as e:
        print(f"❌ LiteLLM调用错误: {e}")
        return False

def test_crewai_compatible_llm():
    """测试CrewAI兼容的LLM配置"""
    try:
        # 测试我们项目中的兼容性配置
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        # 尝试Google Generative AI
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                google_api_key=api_key,
                temperature=0.1
            )
            print("✅ 使用Google Generative AI")
            
        except ImportError:
            # 回退到OpenAI
            try:
                from langchain_openai import ChatOpenAI
                openai_key = os.getenv('OPENAI_API_KEY')
                if openai_key:
                    llm = ChatOpenAI(
                        model="gpt-3.5-turbo",
                        api_key=openai_key,
                        temperature=0.1
                    )
                    print("✅ 回退到OpenAI")
                else:
                    print("❌ 未找到OpenAI API密钥")
                    return False
            except ImportError:
                print("❌ 无可用的LLM提供商")
                return False
        
        # 测试调用
        response = llm.invoke("测试消息")
        print(f"✅ CrewAI兼容LLM测试成功: {response.content[:50]}...")
        return True
        
    except Exception as e:
        print(f"❌ CrewAI兼容性测试错误: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("Google AI 调用测试")
    print("=" * 60)
    
    # 检查环境变量文件
    if not os.path.exists('.env'):
        print("⚠️  警告: 未找到.env文件")
        print("请创建.env文件并设置以下变量:")
        print("GOOGLE_API_KEY=your_google_api_key")
        print("OPENAI_API_KEY=your_openai_api_key (可选)")
        print()
    
    tests = [
        ("基本Google AI调用测试", test_google_ai_basic),
        ("LiteLLM Google AI调用测试", test_litellm_google_ai),
        ("CrewAI兼容LLM测试", test_crewai_compatible_llm)
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
    
    if passed == 0:
        print("\n💡 建议:")
        print("1. 确保已安装必要的包: pip install langchain-google-genai litellm")
        print("2. 在.env文件中设置GOOGLE_API_KEY")
        print("3. 检查API密钥是否有效")
        print("4. 确保网络连接正常")

if __name__ == "__main__":
    main()