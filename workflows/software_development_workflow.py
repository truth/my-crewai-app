from crewai import Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from agents import (
    create_project_manager,
    create_requirements_analyst,
    create_system_architect,
    create_developer,
    create_test_engineer,
    create_devops_engineer
)
from tasks import (
    create_project_initiation_task,
    create_requirements_analysis_task,
    create_system_design_task,
    create_development_planning_task,
    create_code_implementation_task,
    create_test_planning_task,
    create_deployment_planning_task
)

class SoftwareDevelopmentWorkflow:
    """
    软件开发全流程工作流
    """
    
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.agents = self._create_agents()
        
    def _create_agents(self):
        """
        创建所有智能体
        """
        return {
            'project_manager': create_project_manager(self.llm),
            'requirements_analyst': create_requirements_analyst(self.llm),
            'system_architect': create_system_architect(self.llm),
            'developer': create_developer(self.llm),
            'test_engineer': create_test_engineer(self.llm),
            'devops_engineer': create_devops_engineer(self.llm)
        }
    
    def create_project_initiation_crew(self, project_description: str, stakeholder_info: str = ""):
        """
        创建项目启动阶段的Crew
        """
        task = create_project_initiation_task(
            agent=self.agents['project_manager'],
            project_description=project_description,
            stakeholder_info=stakeholder_info
        )
        
        return Crew(
            agents=[self.agents['project_manager']],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
    
    def create_requirements_analysis_crew(self, project_description: str):
        """
        创建需求分析阶段的Crew
        """
        task = create_requirements_analysis_task(
            agent=self.agents['requirements_analyst'],
            project_description=project_description
        )
        
        return Crew(
            agents=[self.agents['requirements_analyst']],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
    
    def create_system_design_crew(self, requirements_doc: str):
        """
        创建系统设计阶段的Crew
        """
        task = create_system_design_task(
            agent=self.agents['system_architect'],
            requirements_doc=requirements_doc
        )
        
        return Crew(
            agents=[self.agents['system_architect']],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
    
    def create_development_crew(self, technical_spec: str, module_spec: str = "", task_description: str = ""):
        """
        创建开发阶段的Crew
        """
        planning_task = create_development_planning_task(
            agent=self.agents['developer'],
            technical_spec=technical_spec
        )
        
        tasks = [planning_task]
        
        if module_spec and task_description:
            implementation_task = create_code_implementation_task(
                agent=self.agents['developer'],
                module_spec=module_spec,
                task_description=task_description
            )
            tasks.append(implementation_task)
        
        return Crew(
            agents=[self.agents['developer']],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )
    
    def create_testing_crew(self, requirements_doc: str, architecture_doc: str):
        """
        创建测试阶段的Crew
        """
        task = create_test_planning_task(
            agent=self.agents['test_engineer'],
            requirements_doc=requirements_doc,
            architecture_doc=architecture_doc
        )
        
        return Crew(
            agents=[self.agents['test_engineer']],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
    
    def create_deployment_crew(self, architecture_doc: str, environment_requirements: str = ""):
        """
        创建部署阶段的Crew
        """
        task = create_deployment_planning_task(
            agent=self.agents['devops_engineer'],
            architecture_doc=architecture_doc,
            environment_requirements=environment_requirements
        )
        
        return Crew(
            agents=[self.agents['devops_engineer']],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
    
    def create_full_development_crew(self, project_description: str):
        """
        创建完整的软件开发流程Crew
        包含所有阶段的任务
        """
        # 创建所有任务
        initiation_task = create_project_initiation_task(
            agent=self.agents['project_manager'],
            project_description=project_description,
            stakeholder_info=""
        )
        
        requirements_task = create_requirements_analysis_task(
            agent=self.agents['requirements_analyst'],
            project_description=project_description
        )
        
        # 注意：在实际使用中，后续任务需要前一个任务的输出作为输入
        # 这里为了简化，使用占位符
        design_task = create_system_design_task(
            agent=self.agents['system_architect'],
            requirements_doc="{requirements_output}"
        )
        
        dev_planning_task = create_development_planning_task(
            agent=self.agents['developer'],
            technical_spec="{design_output}"
        )
        
        test_planning_task = create_test_planning_task(
            agent=self.agents['test_engineer'],
            requirements_doc="{requirements_output}",
            architecture_doc="{design_output}"
        )
        
        deployment_task = create_deployment_planning_task(
            agent=self.agents['devops_engineer'],
            architecture_doc="{design_output}",
            environment_requirements=""
        )
        
        return Crew(
            agents=list(self.agents.values()),
            tasks=[
                initiation_task,
                requirements_task,
                design_task,
                dev_planning_task,
                test_planning_task,
                deployment_task
            ],
            process=Process.sequential,
            verbose=True
        )

def create_software_development_workflow(llm: ChatGoogleGenerativeAI) -> SoftwareDevelopmentWorkflow:
    """
    创建软件开发工作流实例
    """
    return SoftwareDevelopmentWorkflow(llm)