from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Teaches about how we can send a bundle of messages to our LLM.


# Load .env from parent directory
load_dotenv(dotenv_path='../.env')  # Uncommented and corrected

# Verify API key
print("API Key Status:", "## Successfully Loaded API KEY ##" if os.getenv("OPENAI_API_KEY") else "Missing")


chatHistory =[] 
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1
)
system_msg = SystemMessage(content="You are the best astrologer")
chatHistory.append(system_msg)


while True:
    query=input("You :-> ")
    if query.lower() == "exit":
        break
    chatHistory.append(HumanMessage(content=query))
    
    results = llm.invoke(chatHistory)
    chatHistory.append(AIMessage(content=results.content))

    print(f"AI Response :-> {results.content}")

#If You want to retrieve msg history.
# print(chatHistory)