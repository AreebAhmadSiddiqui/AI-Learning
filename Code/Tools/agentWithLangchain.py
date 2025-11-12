from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent

load_dotenv()

search_tool = DuckDuckGoSearchRun()


# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

# Create agent with tools
agent = create_agent(
    model=model,
    tools=[search_tool],  # Add your tools here
    system_prompt="You are a helpful assistant"
)

# Invoke the agent
result = agent.invoke({
    "messages": [{"role": "user", "content": "10 news in India"}]
})

print(result)
