from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

PROJECT_ID="advanceddatabaseproject-22c24"
SESSION_ID="newSession"
COLLECTION_NAME="chat_history"

print("Initialize Firestore client")
fs_client = firestore.Client(project=PROJECT_ID)

chat_history = FirestoreChatMessageHistory(
    session_id = SESSION_ID, #Unique 16 digit number
    collection = COLLECTION_NAME,
    client = fs_client
)

print("Chat History Initialized")
print(f"Current Chat History: {chat_history.messages}")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1
)
# system_msg = SystemMessage(content="You are the helpful assitant")
# chatHistory.append(system_msg)

while True:
    query=input("You :-> ")
    if query.lower() == "exit":
        break
    chat_history.add_user_message(query)
    ai_response = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI Response :-> {ai_response.content}")

    



#comment='''
# After installing google cloud sdk run the below cmd
# $ gcloud auth application-default login 

# '''