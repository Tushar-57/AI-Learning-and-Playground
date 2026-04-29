import logging
import colorlog
from graph import graph
from langchain_core.messages import HumanMessage, ToolMessage

# Setup colored logger
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(message)s%(reset)s',
    log_colors={
        'USER': 'cyan,bold',
        'TOOL_CALL': 'yellow,bold',
        'TOOL_RESULT': 'green',
        'AGENT': 'purple,bold',
        'SEPARATOR': 'white,bold',
        'INFO': 'white'
    }
))
logger = logging.getLogger('agent')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Custom log levels for different message types
logging.addLevelName(21, 'USER')
logging.addLevelName(22, 'TOOL_CALL')
logging.addLevelName(23, 'TOOL_RESULT')
logging.addLevelName(24, 'AGENT')
logging.addLevelName(25, 'SEPARATOR')

current_messages = []
logger.log(25, "═" * 50)
logger.log(24, "ReAct Agent is online! Type 'exit' to quit.")
logger.log(25, "═" * 50)

while True:
    user_text = input("👤 YOU:")
    logger.log(21, f"👤 YOU: {user_text}")
    logger.log(25, "─" * 30)
    is_exit = user_text.lower() in ["exit", "quit"]

    current_messages.append(HumanMessage(content=user_text))
    logger.log(24, "🤖 [Agent thinking...]\n")

    # Stream the graph execution to see each step
    ai_response = ""
    for step in graph.stream({"messages": current_messages}, stream_mode="values"):
        messages = step["messages"]
        last_message = messages[-1]

        # Show tool calls being made
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            for tc in last_message.tool_calls:
                logger.log(22, f"🔧 TOOL CALL: {tc['name']}({tc['args']})")

        # Show tool results
        if isinstance(last_message, ToolMessage):
            content = last_message.content[:150] + "..." if len(last_message.content) > 150 else last_message.content
            logger.log(23, f"📦 TOOL RESULT [{last_message.name}]: {content}")

        # Capture final AI response
        if hasattr(last_message, "content") and last_message.content and not isinstance(last_message, ToolMessage):
            ai_response = last_message.content

    if not is_exit:
        logger.log(24, f"🤖 AGENT: {ai_response}")
        logger.log(25, "═" * 50)
    current_messages = messages

    if is_exit:
        logger.log(24, f"🤖 AGENT: {ai_response}")
        logger.log(25, "═" * 50)
        break