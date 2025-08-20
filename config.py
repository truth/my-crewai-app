#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统配置文件

管理CrewAI软件开发管理系统的配置参数
"""

import os
from typing import Dict, Any

class Config:
    """
    系统配置类
    """
    
    # API配置
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # 模型配置
    DEFAULT_MODEL = "gemini-pro"
    DEFAULT_TEMPERATURE = 0.7
    MAX_TOKENS = 4096
    
    # 智能体配置
    AGENT_CONFIG = {
        "verbose": True,
        "allow_delegation": False,
        "max_iter": 3,
        "memory": True
    }
    
    # 任务配置
    TASK_CONFIG = {
        "verbose": True,
        "async_execution": False
    }
    
    # Crew配置
    CREW_CONFIG = {
        "verbose": True,
        "memory": True,
        "cache": True,
        "max_rpm": 10,
        "share_crew": False
    }
    
    # 项目配置
    PROJECT_CONFIG = {
        "default_language": "zh-CN",
        "output_format": "markdown",
        "max_project_size": "large",
        "quality_threshold": 0.8
    }
    
    # 工作流配置
    WORKFLOW_CONFIG = {
        "enable_parallel_execution": False,
        "auto_save_results": True,
        "result_format": "detailed",
        "enable_progress_tracking": True
    }
    
    # 日志配置
    LOGGING_CONFIG = {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file_path": "logs/crewai.log",
        "max_file_size": "10MB",
        "backup_count": 5
    }
    
    @classmethod
    def get_llm_config(cls) -> Dict[str, Any]:
        """
        获取语言模型配置
        """
        return {
            "model": cls.DEFAULT_MODEL,
            "temperature": cls.DEFAULT_TEMPERATURE,
            "google_api_key": cls.GOOGLE_API_KEY,
            "max_tokens": cls.MAX_TOKENS
        }
    
    @classmethod
    def get_agent_config(cls) -> Dict[str, Any]:
        """
        获取智能体配置
        """
        return cls.AGENT_CONFIG.copy()
    
    @classmethod
    def get_crew_config(cls) -> Dict[str, Any]:
        """
        获取Crew配置
        """
        return cls.CREW_CONFIG.copy()
    
    @classmethod
    def validate_config(cls) -> bool:
        """
        验证配置是否有效
        """
        if not cls.GOOGLE_API_KEY:
            return False
        
        # 可以添加更多验证逻辑
        return True
    
    @classmethod
    def get_environment_info(cls) -> Dict[str, Any]:
        """
        获取环境信息
        """
        return {
            "api_key_configured": bool(cls.GOOGLE_API_KEY),
            "python_version": os.sys.version,
            "working_directory": os.getcwd(),
            "config_valid": cls.validate_config()
        }

# 预定义的项目模板
PROJECT_TEMPLATES = {
    "web_app": {
        "name": "Web应用项目",
        "description": "标准的Web应用开发项目",
        "tech_stack": ["React", "Node.js", "MongoDB"],
        "phases": ["需求分析", "系统设计", "开发", "测试", "部署"]
    },
    "mobile_app": {
        "name": "移动应用项目",
        "description": "移动端应用开发项目",
        "tech_stack": ["React Native", "Firebase"],
        "phases": ["需求分析", "UI设计", "开发", "测试", "发布"]
    },
    "api_service": {
        "name": "API服务项目",
        "description": "后端API服务开发项目",
        "tech_stack": ["Python", "FastAPI", "PostgreSQL"],
        "phases": ["需求分析", "API设计", "开发", "测试", "部署"]
    },
    "data_analysis": {
        "name": "数据分析项目",
        "description": "数据分析和机器学习项目",
        "tech_stack": ["Python", "Pandas", "Scikit-learn"],
        "phases": ["需求分析", "数据探索", "模型开发", "验证", "部署"]
    }
}

# 智能体角色定义
AGENT_ROLES = {
    "project_manager": {
        "name": "项目经理",
        "description": "负责项目整体协调和管理",
        "skills": ["项目规划", "风险管理", "团队协调", "进度控制"]
    },
    "requirements_analyst": {
        "name": "需求分析师",
        "description": "负责需求收集、分析和文档编写",
        "skills": ["需求分析", "业务建模", "用户研究", "文档编写"]
    },
    "system_architect": {
        "name": "系统架构师",
        "description": "负责系统架构设计和技术选型",
        "skills": ["架构设计", "技术选型", "性能优化", "安全设计"]
    },
    "developer": {
        "name": "开发工程师",
        "description": "负责代码实现和开发",
        "skills": ["编程开发", "代码审查", "单元测试", "重构优化"]
    },
    "test_engineer": {
        "name": "测试工程师",
        "description": "负责测试规划、执行和质量保证",
        "skills": ["测试设计", "自动化测试", "性能测试", "缺陷管理"]
    },
    "devops_engineer": {
        "name": "DevOps工程师",
        "description": "负责部署、运维和CI/CD",
        "skills": ["自动化部署", "容器化", "监控运维", "CI/CD"]
    }
}

# 导出配置实例
config = Config()