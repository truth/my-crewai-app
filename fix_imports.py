#!/usr/bin/env python3
"""
彻底修复智能体文件中的导入问题
"""

import os
import re

def fix_agent_file(file_path):
    """彻底修复单个智能体文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除所有现有的langchain导入
    content = re.sub(r'from langchain_google_genai import.*\n', '', content)
    content = re.sub(r'# 兼容不同的LLM提供商.*?pass  # 将在运行时处理\n', '', content, flags=re.DOTALL)
    
    # 在第二行后添加新的导入
    lines = content.split('\n')
    if len(lines) >= 2:
        # 在from typing import之后插入新的导入
        insert_pos = 2
        new_import = [
            "",
            "# 兼容不同的LLM提供商",
            "try:",
            "    from langchain_google_genai import ChatGoogleGenerativeAI",
            "except ImportError:",
            "    try:",
            "        from langchain_openai import ChatOpenAI",
            "    except ImportError:",
            "        pass  # 将在运行时处理"
        ]
        
        lines = lines[:insert_pos] + new_import + lines[insert_pos:]
        content = '\n'.join(lines)
    
    # 移除类型注解
    content = re.sub(r'def (create_\w+)\(llm: ChatGoogleGenerativeAI([^)]*?)\)', 
                    r'def \1(llm\2)', 
                    content)
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已修复: {file_path}")
    return True

def main():
    """主函数"""
    agents_dir = "agents"
    
    if not os.path.exists(agents_dir):
        print(f"❌ 目录不存在: {agents_dir}")
        return
    
    fixed_count = 0
    
    # 遍历agents目录下的所有Python文件
    for filename in os.listdir(agents_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            file_path = os.path.join(agents_dir, filename)
            if fix_agent_file(file_path):
                fixed_count += 1
    
    print(f"\n🎉 修复完成! 共修复了 {fixed_count} 个文件")

if __name__ == "__main__":
    main()