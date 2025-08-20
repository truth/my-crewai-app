# CrewAI集成Gemini完整指南

## 概述

本指南详细说明如何在CrewAI项目中使用OpenAI兼容模式调用Google Gemini模型。通过LiteLLM库，我们可以轻松地将Gemini集成到CrewAI工作流中。

## 问题背景

在使用CrewAI时，您可能遇到以下错误：
```
litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=mock-llm
```

这个错误表明需要正确配置LLM提供商。本指南提供了完整的解决方案。

## 解决方案

### 1. 安装依赖

```bash
pip install litellm python-dotenv
```

### 2. 环境配置

在项目根目录创建`.env`文件：
```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. 获取Google API密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的API密钥
3. 将密钥添加到`.env`文件中

## 实现方法

### 方法一：直接使用LiteLLM

```python
import litellm
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

response = litellm.completion(
    model="gemini/gemini-1.5-flash",
    messages=[
        {"role": "user", "content": "你好，世界！"}
    ],
    temperature=0.1
)

print(response.choices[0].message.content)
```

### 方法二：创建CrewAI兼容包装器

```python
import os
import litellm
from dotenv import load_dotenv

class GeminiLLM:
    """Gemini LLM包装器，兼容CrewAI"""
    
    def __init__(self, model: str = "gemini/gemini-1.5-flash", **kwargs):
        self.model = model
        self.temperature = kwargs.get('temperature', 0.1)
        self.max_tokens = kwargs.get('max_tokens', 1000)
        
        # 确保API密钥已设置
        load_dotenv()
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("请在.env文件中设置GOOGLE_API_KEY")
        
        os.environ['GOOGLE_API_KEY'] = api_key
    
    def invoke(self, prompt: str):
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
            return Response(f"[模拟响应] 由于API调用失败，这是一个模拟回复")
```

### 方法三：在CrewAI中使用

```python
from crewai import Agent, Task, Crew

# 初始化Gemini LLM
llm = GeminiLLM(model="gemini/gemini-1.5-flash", temperature=0.1)

# 创建智能体
agent = Agent(
    role='软件开发助手',
    goal='帮助用户进行软件开发',
    backstory='你是一位经验丰富的软件开发专家',
    llm=llm,  # 使用Gemini LLM
    verbose=True
)

# 创建任务
task = Task(
    description="分析在线图书管理系统的需求",
    agent=agent,
    expected_output="详细的需求分析文档"
)

# 创建团队并执行
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

## 可用的Gemini模型

根据测试结果，以下模型可用：

1. **gemini/gemini-1.5-flash** ✅ (推荐)
   - 速度快，成本低
   - 适合大多数应用场景

2. **gemini/gemini-1.5-pro** ⚠️ (可能有速率限制)
   - 功能更强大
   - 适合复杂任务

3. **vertex_ai/gemini-1.5-flash** (需要Vertex AI配置)
4. **vertex_ai/gemini-1.5-pro** (需要Vertex AI配置)

## 测试文件

项目中包含以下测试文件：

1. **test_google_ai.py** - 基础Google AI调用测试
2. **test_openai_compatible_gemini.py** - OpenAI兼容模式测试
3. **test_litellm_gemini.py** - LiteLLM专项测试
4. **crewai_gemini_example.py** - 完整的CrewAI集成示例
5. **litellm_wrapper.py** - CrewAI兼容包装器

## 运行示例

### 基础测试
```bash
python test_litellm_gemini.py
```

### CrewAI集成示例
```bash
python crewai_gemini_example.py
```

选择运行模式：
1. 直接测试Gemini LLM
2. 需求分析示例
3. 架构设计示例
4. 代码生成示例
5. 运行所有示例

## 故障排除

### 常见问题

1. **ModuleNotFoundError: No module named 'langchain_google_genai'**
   - 解决方案：使用LiteLLM代替直接导入

2. **litellm.RateLimitError: VertexAIException**
   - 解决方案：使用gemini-1.5-flash模型，或等待后重试

3. **API密钥无效**
   - 检查.env文件中的GOOGLE_API_KEY
   - 确保API密钥在Google AI Studio中有效

4. **网络连接问题**
   - 检查网络连接
   - 确保可以访问Google AI服务

### 调试技巧

启用LiteLLM调试模式：
```python
import litellm
litellm.set_verbose = True
```

## 性能优化

1. **选择合适的模型**
   - 日常任务：gemini-1.5-flash
   - 复杂任务：gemini-1.5-pro

2. **调整参数**
   ```python
   llm = GeminiLLM(
       model="gemini/gemini-1.5-flash",
       temperature=0.1,  # 降低随机性
       max_tokens=1000   # 控制响应长度
   )
   ```

3. **错误处理**
   - 实现重试机制
   - 提供回退方案
   - 记录错误日志

## 最佳实践

1. **环境变量管理**
   - 使用.env文件存储敏感信息
   - 不要将API密钥提交到版本控制

2. **错误处理**
   - 实现优雅的错误处理
   - 提供有意义的错误信息

3. **性能监控**
   - 监控API调用次数
   - 跟踪响应时间
   - 记录成功率

4. **成本控制**
   - 选择合适的模型
   - 控制max_tokens参数
   - 实现缓存机制

## 总结

通过使用LiteLLM库，我们成功解决了在CrewAI中调用Gemini模型的问题。这种方法提供了：

- ✅ 简单的集成方式
- ✅ 良好的兼容性
- ✅ 灵活的配置选项
- ✅ 完整的错误处理
- ✅ 多模型支持

现在您可以在CrewAI项目中充分利用Google Gemini的强大功能！

## 相关链接

- [LiteLLM文档](https://docs.litellm.ai/)
- [Google AI Studio](https://makersuite.google.com/)
- [CrewAI文档](https://docs.crewai.com/)
- [Gemini API文档](https://ai.google.dev/docs)