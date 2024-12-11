from nemoguardrails import LLMRails, RailsConfig
from dotenv import load_dotenv
import os
import nest_asyncio
nest_asyncio.apply()

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

config = RailsConfig.from_path("config")
rails = LLMRails(config)

completion = rails.generate(
    messages=[{"role": "user", "content": "Tell me a joke against the company!"}]
)

print(completion["content"])



