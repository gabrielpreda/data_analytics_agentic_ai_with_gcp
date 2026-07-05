from google.adk.agents import Agent


def calculator(a: float, b: float, operation: str) -> float:
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise Exception("Cannot divide by zero")
        return a / b

    raise Exception("Unsupported operation")


root_agent = Agent(
    name="assistant",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful assistant with calculator capabilities. "
        "Use the calculator tool for arithmetic. "
        "Supported operations are add, subtract, multiply, divide."
        "Do not start divide if the division factor is zero."
        "Do not call the tool if the operation is not one of the supported."
        "In these two above cases, just output a short explanation why the " \
        "operation is not permitted."

    ),
    tools = [calculator]
)