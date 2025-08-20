#!/usr/bin/env python3
"""
批量修复tasks文件中的导入问题
"""

import os
import re

def fix_task_file(file_path):
    """修复单个任务文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否包含langchain导入
    if 'from langchain_google_genai import' not in content:
        print(f"⏭️  跳过: {file_path} (无需修复)")
        return False
    
    # 替换导入语句
    old_import = "from langchain_google_genai import ChatGoogleGenerativeAI"
    new_import = """# 兼容不同的LLM提供商
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        pass  # 将在运行时处理"""
    
    content = content.replace(old_import, new_import)
    
    # 移除类型注解
    content = re.sub(r'llm: ChatGoogleGenerativeAI', 'llm', content)
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已修复: {file_path}")
    return True

def main():
    """主函数"""
    tasks_dir = "tasks"
    
    if not os.path.exists(tasks_dir):
        print(f"❌ 目录不存在: {tasks_dir}")
        return
    
    fixed_count = 0
    
    # 遍历tasks目录下的所有Python文件
    for filename in os.listdir(tasks_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            file_path = os.path.join(tasks_dir, filename)
            if fix_task_file(file_path):
                fixed_count += 1
    
    print(f"\n🎉 修复完成! 共修复了 {fixed_count} 个文件")

if __name__ == "__main__":
    main()