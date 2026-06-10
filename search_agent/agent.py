from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction="""You are a helpful assistant. Use Google Search 
    whenever you need to verify real-time data.
    """,
    tools=[google_search] # Passing the built-in tool directly
)
