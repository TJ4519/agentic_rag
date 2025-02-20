from dotenv import load_dotenv
import os
from smolagents.agents import CodeAgent
from smolagents import HfApiModel

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
model = HfApiModel()

### Agent configuration
agent = CodeAgent(
    tools=[],   
    model=model,
    add_base_tools=True,
    verbosity_level=5,
    # system_prompt=Prompt(
    #     "You are a helpful assistant that can write code in Python."
    # )
)

### Agent execution with input sequence
agent.run("How do I convert a weblink into a pdf? I want to conver the page in this link: https://applied-llms.org/#tactical-nuts-bolts-of-working-with-llms into a pdf that I can parse myself into markdown")
