
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
