# day3/agent.py
import json
import datetime
from tools import calculator, get_weather, summarize

def simulate_llm_decision(query):
    """Simulates an LLM deciding which tool to use."""
    query_lower = query.lower()
    if any(op in query_lower for op in ["calculate", "add", "subtract", "multiply", "divide", "+", "-", "*", "/"]):
        return "calculator"
    elif "weather" in query_lower:
        return "weather"
    elif "summarize" in query_lower or "summary" in query_lower:
        return "summarize"
    else:
        return "unknown"

def extract_expression(query):
    """Pulls out just the math expression from the query."""
    for word in ["calculate", "what is", "compute"]:
        query = query.lower().replace(word, "")
    return query.strip()

def extract_city(query):
    """Pulls out the city name from the query."""
    for word in ["weather", "in", "what's the", "what is the"]:
        query = query.lower().replace(word, "")
    return query.strip().title() or "Mumbai"

def extract_text(query):
    """Pulls out the text to summarize."""
    for word in ["summarize", "summary of", "summarise"]:
        query = query.lower().replace(word, "")
    return query.strip()

def log(query, tool, output):
    with open("log.json", "a") as f:
        json.dump({
            "time": str(datetime.datetime.now()),
            "input": query,
            "tool": tool,
            "output": str(output)
        }, f)
        f.write("\n")

def run_agent(query):
    print(f"\nQuery: {query}")
    
    # Step 1: LLM decides which tool
    tool = simulate_llm_decision(query)
    print(f"LLM selected tool: {tool}")

    # Step 2: Actually call the tool
    if tool == "calculator":
        expression = extract_expression(query)
        result = calculator(expression)

    elif tool == "weather":
        city = extract_city(query)
        result = get_weather(city)

    elif tool == "summarize":
        text = extract_text(query)
        result = summarize(text)

    else:
        result = "Sorry, I don't have a tool for that."

    # Step 3: Log and return result
    log(query, tool, result)
    print(f"Result: {result}\n")

# Main loop
while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    run_agent(user_input)