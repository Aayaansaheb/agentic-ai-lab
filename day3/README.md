# Day 3 — LLM-Based Agent

## Overview
This agent replaces the hardcoded keyword-matching logic from Day 2 with an **LLM-based decision engine**. The language model reads the user query and decides which tool to call. The selected tool is then actually executed and the real result is returned to the user. All interactions are logged to a JSON file.

## Project Structure
```
day3/
├── agent.py      # Main agent with LLM decision + tool execution
├── tools.py      # Same tools as Day 2
├── log.json      # Auto-generated log of all interactions
└── README.md
```

## How It Works
1. User submits a query
2. LLM (simulated) reads the query and selects the best tool
3. Agent extracts the relevant arguments from the query
4. The actual tool is called and returns a real result
5. The interaction is logged to `log.json`

## Tools Available
| Tool | Trigger keywords |
|---|---|
| `calculator` | calculate, add, subtract, multiply, +, -, *, / |
| `get_weather` | weather |
| `summarize` | summarize, summary |

## How to Run

```bash
cd day3
python agent.py
```

## Example
```
Enter your query: calculate 10 + 5 * 2
LLM selected tool: calculator
Result: 20

Enter your query: weather in Delhi
LLM selected tool: weather
Result: The weather in Delhi is 25°C and sunny.
```

## Log Format (`log.json`)
Each interaction is stored as a JSON object:
```json
{"time": "2025-04-06 10:23:01", "input": "calculate 10 + 5", "tool": "calculator", "output": "15"}
```

## What I Learned
- How LLMs can act as decision-makers in an agent pipeline
- How to connect LLM output to real tool execution
- How to log agent interactions for debugging and transparency
- The difference between selecting a tool and actually calling it