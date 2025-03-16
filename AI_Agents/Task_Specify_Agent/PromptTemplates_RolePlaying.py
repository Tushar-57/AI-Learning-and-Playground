from camel.agents import TaskSpecifyAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType, TaskType

def createModel(modelName):
	m1_model = ModelFactory.create(
		model_platform=ModelPlatformType.OLLAMA,
		model_type=modelName,
		url="http://localhost:11434/v1", #optional
		model_config_dict={"temperature":0.9},
	)
	return m1_model

finalModelToUse = createModel("llama3.2:3b")

# Create a task specify agent
task_specify_agent = TaskSpecifyAgent(
    model=finalModelToUse, task_type=TaskType.AI_SOCIETY
)
print("========================================")
print(TaskType) # get all available Task Types

# Run the agent with a task prompt
specified_task_prompt = task_specify_agent.run(
    task_prompt="Improving chances of clearing an interview round",
    meta_dict=dict(
        assistant_role="Parent", user_role="Student", word_limit=100
    ),
)

print(f"Specified task prompt:\n{specified_task_prompt}\n")