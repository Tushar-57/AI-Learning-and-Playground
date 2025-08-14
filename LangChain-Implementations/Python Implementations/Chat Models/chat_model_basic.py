from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load .env from parent directory
load_dotenv(dotenv_path="../.env")  # Uncommented and corrected

# Verify API key
print(
    "API Key Status:",
    "## Successfully Loaded API KEY ##" if os.getenv("OPENAI_API_KEY") else "Missing",
)


# Parameter	| Description
# model	-> The name or identifier of the specific AI model you want to use (e.g., "gpt-3.5-turbo" or "gpt-4").
# temperature ->	Controls the randomness of the model's output. A higher value (e.g., 1.0) makes responses more creative, while a lower value (e.g., 0.0) makes them more deterministic and focused.
# timeout ->	The maximum time (in seconds) to wait for a response from the model before canceling the request. Ensures the request doesn’t hang indefinitely.
# max_tokens ->	Limits the total number of tokens (words and punctuation) in the response. This controls how long the output can be.
# stop ->	Specifies stop sequences that indicate when the model should stop generating tokens. For example, you might use specific strings to signal the end of a response.
# max_retries ->	The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits.
# api_key ->	The API key required for authenticating with the model provider. This is usually issued when you sign up for access to the model.
# base_url ->	The URL of the API endpoint where requests are sent. This is typically provided by the model's provider and is necessary for directing your requests.
# rate_limiter ->	An optional BaseRateLimiter to space out requests to avoid exceeding rate limits. See rate-limiting below for more details.
# Initialize model with explicit API key
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
# Generate response
results = llm.invoke("What does Tushar Mean?")
print(f"Output from Chat GPT:\n{results}")
print(f"Output from Chat GPT:\n{results.content}")