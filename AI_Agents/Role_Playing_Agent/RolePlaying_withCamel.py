from camel.societies import RolePlaying
from camel.types import TaskType, ModelType, ModelPlatformType
# from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
# from camel.utils import print_text_animated
# from colorama import Fore

def createModel(modelName):
	m1_model = ModelFactory.create(
		model_platform=ModelPlatformType.OLLAMA,
		model_type=modelName,
		url="http://localhost:11434/v1", #optional
		model_config_dict={"temperature":0.9},
	)
	return m1_model

finalModelToUse = createModel("llama3.2:3b")

#Setting up task arguments
task_kwargs = {
    'task_prompt': 'Develop a plan to TRAVEL TO THE PAST and make changes.',
    'with_task_specify': True,
    'task_specify_agent_kwargs': {'model': finalModelToUse}
}
#User Args
user_role_kwargs = {
    'user_role_name': 'an ambitious aspiring TIME TRAVELER',
    'user_agent_kwargs': {'model': finalModelToUse}
}
#Assistant Args
assistant_role_kwargs = {
    'assistant_role_name': 'the best-ever experimental physicist',
    'assistant_agent_kwargs': {'model': finalModelToUse}
}

#Kickstart Society
society = RolePlaying(
    **task_kwargs,             # The task arguments
    **user_role_kwargs,        # The instruction sender's arguments
    **assistant_role_kwargs,   # The instruction receiver's arguments
)

def is_terminated(response):
    """
    Give alerts when the session should be terminated.
    """
    if response.terminated:
        role = response.msg.role_type.name
        reason = response.info['termination_reasons']
        print(f'AI {role} terminated due to {reason}')

    return response.terminated

# simple loop for our society to proceed:
def run(society, round_limit: int=10):
    # Get the initial message from the ai assistant to the ai user
    input_msg = society.init_chat()
    
    for _ in range(round_limit):    # Starting the interactive session

        # Get the both responses for this round
        assistant_response, user_response = society.step(input_msg)

        # Check the termination condition
        if is_terminated(assistant_response) or is_terminated(user_response):
            break

        # Get the results
        print(f'[AI User] {user_response.msg.content}.\n')
        # Check if the task is end
        if 'CAMEL_TASK_DONE' in user_response.msg.content:
            break
        print(f'[AI Assistant] {assistant_response.msg.content}.\n')
        # Get the input message for the next round
        input_msg = assistant_response.msg
    return None

#Finally, let's see our created society in action
run(society)