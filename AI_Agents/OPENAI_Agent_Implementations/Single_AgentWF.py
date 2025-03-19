from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import os

# Set a dummy API key since the OpenAI client requires it
os.environ["OPENAI_API_KEY"] = "dummy-key"

model = OpenAIChatCompletionsModel(
    model="llama3.2:3b",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="dummy-key"
    )
)

agent = Agent(
    name="A1",
    instructions="You are a Helpful Agent",
    model=model
)

result = Runner.run_sync(agent, "Create Meal Plan for a week")
print(result.final_output)