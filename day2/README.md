# Day 2 — Tool-Using Agent

## Overview
An extension of the Day 1 agent that integrates external tools. Instead of hardcoding actions, the agent routes user queries to modular tool functions. This introduces the concept of **tool abstraction** and **function calling**.

## Project Structure
```
day2/
├── agent.py      # Main agent logic and routing
├── tools.py      # Tool definitions (calculator, weather, summarizer)
└── README.md
```

## Tools Available
| Tool | Description |
|---|---|
| `calculator` | Evaluates a mathematical expression |
| `get_weather` | Returns mocked weather info for a city |
| `summarize` | Shortens a long piece of text to 20 words |

## How to Run

```bash
cd day2
python agent.py
```

## Example
```
Query: calculate 20 * 3
Result: 60

Query: weather in Mumbai
Result: The weather in Mumbai is 25°C and sunny.

Query: summarize Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and learn
Result: Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and...
```

## What I Learned
- How to abstract tools as reusable functions
- How to build a modular project structure (agent + tools separated)
- How an agent decides which tool to call based on user input