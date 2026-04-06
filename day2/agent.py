from tools import calculator, get_weather, summarize

def route(query):
    if "calculate" in query:
        expr = query.replace("calculate", "").strip()
        return calculator(expr)
    elif "weather" in query:
        city = query.replace("weather", "").strip() or "Mumbai"
        return get_weather(city)
    elif "summarize" in query:
        text = query.replace("summarize", "").strip()
        return summarize(text)
    else:
        return "No tool found for this query."

while True:
    q = input("Query: ")
    print(route(q))