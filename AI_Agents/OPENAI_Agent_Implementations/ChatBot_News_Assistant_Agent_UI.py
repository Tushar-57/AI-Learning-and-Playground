import chainlit as cl
from Multi_AgentWF import run_news_wf

@cl.on_message
async def main(message: cl.Message):
    topic = message.content

    await cl.Message(
        content=f"Searching for news about '{topic}' ...",
        author = "News Bot"
    ).send()

    try:
        news_content = run_news_wf(topic)

        await cl.Message(
            content=news_content,
            author="News Bot"
        ).send()
    except Exception as e:
        await cl.Message(
            content = f"Error Fetching News: {str(e)}",
            author="News Bot"
        ).send()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to the News Assistant ! Give topic for news",
        author="News Bot"
    ).send()
