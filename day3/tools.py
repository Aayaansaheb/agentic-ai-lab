# day3/tools.py
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"

def get_weather(city):
    return f"The weather in {city} is 25°C and sunny."

def summarize(text):
    words = text.split()
    return " ".join(words[:20]) + "..." if len(words) > 20 else text