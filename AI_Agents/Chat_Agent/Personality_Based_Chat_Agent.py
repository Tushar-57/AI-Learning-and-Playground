from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType

def createModel(modelName):
	m1_model = ModelFactory.create(
		model_platform=ModelPlatformType.OLLAMA,
		model_type=modelName,
		url="http://localhost:11434/v1", #Since I am using my locally available model
		model_config_dict={"temperature":0.9},
	)
	return m1_model

modelToUse = createModel("llama3.2:3b")

assistant_sys_msg = BaseMessage.make_assistant_message(
	role_name="Warren Buffet", # you can give any role, it allow the assistant to simulate the persona of Warren Buffett
	content="You are an expert financial advisor with 10+ years of stock experience",
)

agent = ChatAgent(assistant_sys_msg, model=modelToUse, token_limit=4096)

user_msg = BaseMessage.make_user_message(
	role_name="User", content="Give you fundamental analysis briefly about IBM?"
)

assistant_response = agent.step(user_msg)
print(assistant_response)