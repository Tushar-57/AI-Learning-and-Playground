from camel.agents import TaskSpecifyAgent
# from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.prompts import TextPrompt
from camel.types import ModelPlatformType, ModelType

def createModel(modelName):
	m1_model = ModelFactory.create(
		model_platform=ModelPlatformType.OLLAMA,
		model_type=modelName,
		url="http://localhost:11434/v1", #optional
		model_config_dict={"temperature":0.9},
	)
	return m1_model

finalModelToUse = createModel("llama3.2:3b")
# ModelPlatformType.SAMBA, "Meta-Llama-3.1-8B-Instruct" #Fastest Token per second
# ModelPlatformType.SAMBA, "Meta-Llama-3.1-70B-Instruct"

print("========================================")

# Create a custom prompt template
my_prompt_template = TextPrompt(
    'Here is a task: I\'m a {occupation} and I want to {task}. Help me to make this task more specific.'
)

# Create a task specify agent with the custom prompt
task_specify_agent = TaskSpecifyAgent(
    model=finalModelToUse, task_specify_prompt=my_prompt_template
)

# Run the agent with a task prompt
response = task_specify_agent.run(
    task_prompt="get promotion",
    meta_dict=dict(occupation="Software Engineer"),
)

print(response)