#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LiteLLM调用Gemini测试
专门测试通过LiteLLM调用Google Gemini的各种方式
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_litellm_gemini_models():
    """测试不同的Gemini模型"""
    try:
        import litellm
        
        # 检查API密钥
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        # 设置环境变量
        os.environ['GOOGLE_API_KEY'] = api_key
        
        print(f"✅ 找到Google API密钥: {api_key[:10]}...")
        
        # 测试不同的Gemini模型
        models_to_test = [
            "gemini/gemini-1.5-flash",
            "gemini/gemini-2.5-pro",
            # "vertex_ai/gemini-1.5-flash",
            # "vertex_ai/gemini-1.5-pro"
        ]
        
        successful_models = []
        
        for model in models_to_test:
            print(f"\n🧪 测试模型: {model}")
            try:
                response = litellm.completion(
                    model=model,
                    messages=[
                        {"role": "user", "content": "请用一句话介绍你自己。"}
                    ],
                    temperature=0.1,
                    max_tokens=100
                )
                
                content = response.choices[0].message.content
                print(f"✅ 成功: {content[:80]}...")
                successful_models.append(model)
                
            except Exception as e:
                print(f"❌ 失败: {str(e)[:100]}...")
        
        if successful_models:
            print(f"\n✅ 成功的模型: {', '.join(successful_models)}")
            return True
        else:
            print("\n❌ 所有模型测试都失败了")
            return False
            
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请安装: pip install litellm")
        return False
    except Exception as e:
        print(f"❌ 测试错误: {e}")
        return False

def test_litellm_with_crewai_format():
    """测试LiteLLM在CrewAI中的使用格式"""
    try:
        import litellm
        
        # 检查API密钥
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ 错误: 未设置GOOGLE_API_KEY环境变量")
            return False
            
        os.environ['GOOGLE_API_KEY'] = api_key
        
        print("✅ 测试CrewAI格式的LiteLLM调用...")
        
        # 模拟CrewAI的调用方式
        def create_llm_response(prompt):
            """模拟CrewAI中LLM的调用"""
            response = litellm.completion(
                model="gemini/gemini-1.5-flash",
                messages=[
                    {"role": "system", "content": "你是一个有用的AI助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=500
            )
            return response.choices[0].message.content
        
        # 测试不同类型的任务
        test_prompts = [
            "请分析一个在线图书管理系统的需求。",
            "设计一个简单的数据库架构。",
            "编写一个Python函数来处理用户登录。"
        ]
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\n📝 测试任务 {i}: {prompt[:30]}...")
            try:
                response = create_llm_response(prompt)
                print(f"✅ 响应: {response[:100]}...")
            except Exception as e:
                print(f"❌ 失败: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ CrewAI格式测试错误: {e}")
        return False

def create_crewai_compatible_wrapper():
    """创建CrewAI兼容的LLM包装器"""
    wrapper_code = '''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrewAI兼容的LiteLLM包装器
用于在CrewAI中使用LiteLLM调用Gemini
"""

import os
import litellm
from typing import Any, Dict, List, Optional

class LiteLLMWrapper:
    """LiteLLM包装器，兼容CrewAI的LLM接口"""
    
    def __init__(self, model: str = "gemini/gemini-1.5-flash", **kwargs):
        self.model = model
        self.temperature = kwargs.get('temperature', 0.1)
        self.max_tokens = kwargs.get('max_tokens', 1000)
        
        # 确保API密钥已设置
        if not os.getenv('GOOGLE_API_KEY'):
            raise ValueError("请设置GOOGLE_API_KEY环境变量")
    
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
            raise Exception(f"LiteLLM调用失败: {e}")
    
    def __call__(self, prompt: str) -> str:
        """直接调用方法"""
        response = self.invoke(prompt)
        return response.content

# 使用示例
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    # 创建LLM实例
    llm = LiteLLMWrapper(model="gemini/gemini-1.5-flash")
    
    # 测试调用
    response = llm.invoke("你好，请介绍一下你自己。")
    print(f"响应: {response.content}")
'''
    
    with open('litellm_wrapper.py', 'w', encoding='utf-8') as f:
        f.write(wrapper_code)
    
    print("✅ 已创建CrewAI兼容的LiteLLM包装器: litellm_wrapper.py")

def show_integration_guide():
    """显示集成指南"""
    print("\n" + "=" * 60)
    print("CrewAI集成LiteLLM Gemini指南")
    print("=" * 60)
    
    guide = """
1. 安装依赖:
   pip install litellm python-dotenv

2. 设置环境变量(.env文件):
   GOOGLE_API_KEY=your_google_api_key_here

3. 在CrewAI中使用LiteLLM:
   
   方法一: 直接使用LiteLLM
   ```python
   import litellm
   import os
   
   os.environ['GOOGLE_API_KEY'] = 'your_key'
   
   response = litellm.completion(
       model="gemini/gemini-1.5-flash",
       messages=[{"role": "user", "content": "Hello"}]
   )
   ```
   
   方法二: 使用包装器
   ```python
   from litellm_wrapper import LiteLLMWrapper
   
   llm = LiteLLMWrapper(model="gemini/gemini-1.5-flash")
   
   # 在CrewAI Agent中使用
   agent = Agent(
       role='助手',
       goal='帮助用户',
       backstory='我是AI助手',
       llm=llm  # 使用包装器
   )
   ```

4. 可用的Gemini模型:
   - gemini/gemini-1.5-flash (推荐，速度快)
   - gemini/gemini-1.5-pro (功能强大)
   - vertex_ai/gemini-1.5-flash (通过Vertex AI)
   - vertex_ai/gemini-1.5-pro (通过Vertex AI)

5. 故障排除:
   - 确保API密钥有效
   - 检查网络连接
   - 查看LiteLLM文档: https://docs.litellm.ai/
"""
    
    print(guide)

def main():
    """主测试函数"""
    print("=" * 60)
    print("LiteLLM调用Gemini专项测试")
    print("=" * 60)
    
    # 检查环境变量
    if not os.getenv('GOOGLE_API_KEY'):
        print("\n⚠️  警告: 未设置GOOGLE_API_KEY环境变量")
        print("请在.env文件中设置您的Google API密钥")
        return
    
    tests = [
        ("LiteLLM Gemini模型测试", test_litellm_gemini_models),
        ("CrewAI格式兼容性测试", test_litellm_with_crewai_format)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name}")
        print("-" * 40)
        result = test_func()
        results.append((test_name, result))
        print()
    
    # 创建包装器
    print("\n🔧 创建CrewAI兼容包装器")
    print("-" * 40)
    create_crewai_compatible_wrapper()
    
    # 总结
    print("\n" + "=" * 60)
    print("测试结果总结")
    print("=" * 60)
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{status} {test_name}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"\n总计: {passed}/{total} 个测试通过")
    
    # 显示集成指南
    show_integration_guide()

if __name__ == "__main__":
    main()