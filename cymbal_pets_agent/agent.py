from google.adk.agents import Agent


root_agent = Agent(
    name="cymbal_pets_agent",
    model="gemini-2.5-flash",
    instruction="""
        You are a retail analytics assistant
        for the Cymbal Pets business.
        Answer to retail related questions using a 
        simple, concise, and professional language.
    """,
)