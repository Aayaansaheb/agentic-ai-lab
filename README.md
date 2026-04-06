# Agentic AI Lab

A progressive 4-day lab exploring the fundamentals of Agentic AI systems — from simple rule-based logic to multi-step planning agents.

## Overview

This repository contains four assignments that build on each other to develop a complete understanding of how AI agents work. Each day introduces a new concept, starting from basic input-output logic and ending with a planning-capable agent.

## Repository Structure

```
agentic-ai-lab/
│
├── day1/               # Rule-based agent
│   ├── agent.py
│   └── README.md
│
├── day2/               # Tool-using agent
│   ├── agent.py
│   ├── tools.py
│   └── README.md
│
├── day3/               # LLM-based agent
│   ├── agent.py
│   ├── tools.py
│   ├── log.json
│   └── README.md
│
├── day4/               # Multi-step planning agent
│   ├── agent.py
│   ├── planner.py
│   └── README.md
│
└── README.md
```

## Progression of Concepts

| Day | Type | Key Concept |
|---|---|---|
| Day 1 | Rule-Based Agent | Input → Decision → Action pipeline |
| Day 2 | Tool-Using Agent | Tool abstraction and function calling |
| Day 3 | LLM-Based Agent | AI-driven decision making + logging |
| Day 4 | Multi-Step Agent | Task decomposition and planning |

## Setup & Installation

### Prerequisites
- Python 3.9 or above
- pip

### Steps

```bash
# Clone the repository
git clone https://github.com/Aayaansaheb/agentic-ai-lab.git
cd agentic-ai-lab

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install langchain openai
```

## Running Each Assignment

```bash
# Day 1
cd day1 && python agent.py

# Day 2
cd day2 && python agent.py

# Day 3
cd day3 && python agent.py

# Day 4
cd day4 && python agent.py
```

## Key Learnings

- **Agent architecture** — every agent follows an input → decision → action loop
- **Tool abstraction** — separating tools from agent logic makes systems modular and scalable
- **LLM integration** — language models can act as intelligent routers in an agent pipeline
- **Multi-step planning** — complex tasks can be broken into steps and executed sequentially
- **Logging** — tracking inputs, decisions, and outputs is essential for debugging agents

## Tech Stack
- Python 3.9+
- LangChain (framework)
- Git & GitHub (version control)

## Author
Aayaan Saheb