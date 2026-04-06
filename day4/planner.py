# planner.py

def plan(query):
    """Returns a list of steps to execute."""
    steps = []
    if any(c.isdigit() for c in query):
        steps.append("extract_numbers")
    if "average" in query or "mean" in query:
        steps.append("compute_average")
    if "summarize" in query or "summary" in query:
        steps.append("generate_summary")
    return steps

def extract_numbers(query):
    import re
    return [float(n) for n in re.findall(r'\d+\.?\d*', query)]

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def generate_summary(average, query):
    return f"The average of the numbers in your query is {average:.2f}."