from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

# Example 1
# template = "Write a {tone} cover letter to {person} expressing intrest in the {position} position, mentioning {skill} as key strength. keep it 1 paragraph max"
# prompt_template = ChatPromptTemplate.from_template(template)
# result = prompt_template.invoke({
#     "tone": "energetic",
#     "person": "Company HR",
#     "position": "AI Engineer",
#     "skill": "NLP"
# })
# print(result)

# Example 2 below with messages as tuples/
messages = [
    ("system", "You are a dark comedian who tells jokes on topic {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template2 = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template2.invoke({"topic": "AI Engineers", "joke_count": 2})

print(prompt.content)
