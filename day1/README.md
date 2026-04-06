# Day 1 — Rule-Based AI Agent

## Overview
A simple AI agent built using rule-based logic. The agent takes user input, identifies the intent using keyword matching, and executes the appropriate action. This forms the foundation of understanding how agents work: **input → decision → action**.

## How It Works
1. **Input Handler** — reads the user's query from the terminal
2. **Decision Logic** — matches keywords to identify intent
3. **Action Execution** — runs the correct action based on intent

## Supported Commands
| User Input | Action |
|---|---|
| `calculate 2 + 3` | Evaluates the math expression |
| `date` | Returns today's date |
| `hello` / `hi` | Responds with a greeting |

## How to Run

```bash
cd day1
python agent.py
```

## Example
```
Enter command: calculate 10 + 5
Result: 15

Enter command: date
Today is: 2025-04-06

Enter command: hello
Hello! How can I help you?
```

## What I Learned
- Basic agent architecture (input → decision → action pipeline)
- How rule-based reasoning works using keyword matching
- How to structure a Python program into modular components