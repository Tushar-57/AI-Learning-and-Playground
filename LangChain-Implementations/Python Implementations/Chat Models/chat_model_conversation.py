from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Teaches about how we can send a bundle of messages to our LLM.


# Load .env from parent directory
load_dotenv(dotenv_path='../.env')  # Uncommented and corrected

# Verify API key
print("API Key Status:", "## Successfully Loaded API KEY ##" if os.getenv("OPENAI_API_KEY") else "Missing")

messages=[
    SystemMessage("you are an expert in astrology"),
    HumanMessage("What are the different ascendants for a person born on 2_June_1998")
]

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1
)
# Generate response
results = llm.invoke(messages)
print(f"Output from Chat GPT:\n{results}")
print(f"Output from Chat GPT:\n{results.content}")