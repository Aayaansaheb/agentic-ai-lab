# Day 4 — Multi-Step Agent (Planning)

## Overview
This agent can solve tasks that require **multiple sequential steps**. Instead of routing to a single tool, it first creates a plan — a list of steps — and then executes them one by one, showing intermediate outputs at each stage.

## Project Structure
```
day4/
├── agent.py      # Main agent that runs the plan
├── planner.py    # Breaks queries into steps and executes them
└── README.md
```

## How It Works
1. User submits a complex query
2. **Planner** analyzes the query and generates a list of steps
3. Agent executes each step sequentially
4. Intermediate output is shown after every step
5. Final result is displayed at the end

## Example Steps for "Find the average of 5, 10, 15 and summarize the result"
| Step | Action | Output |
|---|---|---|
| 1 | Extract numbers | `[5.0, 10.0, 15.0]` |
| 2 | Compute average | `10.0` |
| 3 | Generate summary | `"The average of the numbers in your query is 10.00."` |

## How to Run

```bash
cd day4
python agent.py
```

## Example
```
Enter your task: find the average of 5, 10, 15 and summarize the result

Plan: ['extract_numbers', 'compute_average', 'generate_summary']

Step 1 - Extracted numbers: [5.0, 10.0, 15.0]
Step 2 - Average: 10.0
Step 3 - Summary: The average of the numbers in your query is 10.00.
```

## What I Learned
- How to decompose a complex task into smaller steps (task planning)
- How to execute steps sequentially and pass results between them
- How intermediate outputs help in debugging multi-step pipelines
- The concept of planning-based agents