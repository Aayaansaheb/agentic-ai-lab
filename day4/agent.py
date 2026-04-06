from planner import plan, extract_numbers, compute_average, generate_summary

query = input("Enter your task: ")
steps = plan(query)
print(f"\nPlan: {steps}\n")

result = None
numbers = []
for step in steps:
    if step == "extract_numbers":
        numbers = extract_numbers(query)
        print(f"Step 1 - Extracted numbers: {numbers}")
    elif step == "compute_average":
        result = compute_average(numbers)
        print(f"Step 2 - Average: {result}")
    elif step == "generate_summary":
        summary = generate_summary(result, query)
        print(f"Step 3 - Summary: {summary}")