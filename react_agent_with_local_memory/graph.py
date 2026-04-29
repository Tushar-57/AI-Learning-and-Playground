from tools import read_memory, save_memory, search_memory_for_regex
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
import os


model = init_chat_model("gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"], model_provider="openai")

tools = [read_memory, save_memory, search_memory_for_regex]

# We use a system message to explicitly instruct the agent on how to use its tools
system_prompt = """
    You are an autonomous AI agent with a persistent on-drive memory file 'agent_brain.txt' for all user conversations with query and response. 
    If the user asks you to recall something, use the 'read_memory' tool to check your local file 'agent_brain.txt' for loading past conversations. 
    After every conversation, when user decides to exit, only then use the 'save_memory' tool to write all the chat conversation history down permanently in 'agent_brain.txt'. 
    If the user asks you to search for something, use the 'search_memory_for_regex' tool to search your local file 'agent_brain.txt'."""

# create_react_agent automatically wires up the routing between the LLM and the tools
graph = create_react_agent(model, tools=tools, prompt=system_prompt)
