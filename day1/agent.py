# 1. Input handler
def get_input():
    return input("Enter command: ").lower()

# 2. Decision logic (keyword matching)
def decide_intent(query):
    if "calculate" in query:
        return "calculate"
    elif "date" in query:
        return "date"
    elif "hello" in query or "hi" in query:
        return "greet"
    else:
        return "unknown"

# 3. Action execution
def execute(intent, query):
    if intent == "calculate":
        # parse and eval a simple expression
        expr = query.replace("calculate", "").strip()
        print(f"Result: {eval(expr)}")
    elif intent == "date":
        from datetime import date
        print(f"Today is: {date.today()}")
    elif intent == "greet":
        print("Hello! How can I help you?")
    else:
        print("I don't understand that command.")

# Main loop
while True:
    user_input = get_input()
    intent = decide_intent(user_input)
    execute(intent, user_input)