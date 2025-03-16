# Chat Agent Implementation 🤖

## Description 📝
`Personality_Based_Chat_Agent.py` brings to life a conversational AI agent using the CAMEL library, powered by a local language model via Ollama. This script sets up a chat agent that responds to user queries, like a virtual financial advisor or a helpful assistant.

### 🧠 Human Analogy
Imagine having a friendly expert at your fingertips—like a seasoned stock advisor or a kind assistant—who answers your questions based on their knowledge, all while running on your own computer!

## Flow:
1. **Initializes** a local Llama 3.2 3B model through Ollama  
2. **Configures** a chat agent with a system message defining its role (e.g., "Warren Buffet" or "Helpful Assistant")  
3. **Processes** a user message with a query (e.g., "Which stock should I invest in?")  
4. **Generates** a response based on the model’s reasoning  
5. **Outputs** the agent’s reply to the console  

> **Highlight:** This script shows how to create a chatbot that runs locally, giving you full control over its personality and responses!

Make sure you have the following ready before running the script:  
- **Python 3.x**  
- **CAMEL library** (`pip install camel-ai`)  
- **Ollama** with a local model (e.g., `ollama run llama3.2:3b`)  

## Usage 💻
Get chatting with your AI agent in just a few steps:  

1. **Run the script directly:**  
   ```bash
   python chat_agent.py
   ```

## The Script Will:

- Set up a chat agent with a predefined role
- Respond to a sample user query (e.g., "What is your name?" or "Which stock should I invest in?")
- Print the response to the console

### To Customize It:

```python
assistant_sys_msg = BaseMessage.make_assistant_message(role_name="Your Role", content="Your description")
agent = ChatAgent(assistant_sys_msg, model=modelToUse)
user_msg = BaseMessage.make_user_message(role_name="User", content="Your question")
response = agent.step(user_msg)
print(response)
```

## Code Features 🛠️

- Local model integration with Ollama
- Customizable agent roles and personalities
- Configurable model parameters (e.g., temperature, token limit)
- Simple message handling with BaseMessage

## What's in it for you 💡

- Learn how to build a conversational AI agent from scratch
- Experiment with local LLMs for chat applications
- Understand role-based prompting in agent design
- Explore the foundations of chatbot development

## Highlights 📌

- **Fully Local:** No token limits or external API costs!
- **Beginner-Friendly:** A straightforward intro to conversational agents
- **Flexible:** Change the role or query to suit your needs
- **Expandable:** Add more features like memory or multi-turn conversations

Happy chatting! 💬✨
