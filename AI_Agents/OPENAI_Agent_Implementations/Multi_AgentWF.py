from duckduckgo_search import DDGS
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from datetime import datetime
import os

os.environ["OPENAI_API_KEY"] = "dummy-key"
curr_date = datetime.now().strftime("%Y-%m")

model = OpenAIChatCompletionsModel(
    model="llama3.2:3b",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
    )
)

@function_tool
def get_news_articles(topic):
    print(f"Searching DDGo for {topic} related articles.")
    ddgo_api = DDGS()
    results = ddgo_api.text(f"{topic} {curr_date}", max_results=1)
    print(results)
    if results:
        news_results = "\n\n".join([f"Title: {results['title']}, \n URL: {results['href']}, \n "])
        print(news_results)
        return news_results
    else:
        return f"Could not find any search results"


#Creating AI Agent to fetch News

NewsAgent = Agent(
    name="News Assistant",
    instructions="You provide the latest news articles for a given topic using DDGo ",
    tools=[get_news_articles], 
    model=model
)

#A2 - Editor
EditorAgent = Agent(
    name="Editor Assistant",
    instructions="Rewrite and give me as news article ready for publishing.",
    model=model
)

def run_news_wf(topic):
    news_response = Runner.run_sync(
        NewsAgent,
        f"Get me the news about {topic} on {curr_date}"
    )

    raw_news = news_response.final_output

    edited_news_response = Runner.run_sync(
        EditorAgent,
        raw_news
    )


    edited_news = edited_news_response.final_output
    print(edited_news)

print(run_news_wf("AI Agents"))