# Agent Benchmark Suite

A comprehensive benchmark suite to evaluate multi-agent AI frameworks across collaborative task scenarios. This project compares the performance of popular frameworks such as **MetaGPT**, **CrewAI**, and **LangGraph** using models served via **Ollama**.

---

## Overview

This benchmark evaluates the capabilities of different multi-agent orchestration frameworks in executing structured collaborative tasks. Key metrics include:

- Task planning and decomposition
- Collaboration fluidity between agents
- Output structure and readability
- Originality and insight
- Execution flow and consistency

---

## Benchmark Setup

- **Hardware:** RTX 3060 (12GB VRAM), 64GB RAM, Ubuntu  
- **Frameworks Tested:** MetaGPT, CrewAI, LangGraph  
- **Models Used:** Served via [Ollama](https://ollama.com)  
- **Evaluation Criteria:**  
  - Scored on a 1.0–5.0 scale per dimension with decimal precision  
  - Manual review of structure, flow, and collaboration

---

## Summary of Results

| Framework         | Score (Avg) | Highlights                                             |
|------------------|-------------|--------------------------------------------------------|
| **MetaGPT**       | ⭐ **Highest**   | Excellent planning, modularity, and collaboration flow |
| CrewAI           | High        | Fast and readable with solid performance               |
| LangGraph        | Moderate    | Accurate and consistent, slightly rigid in tone        |

> **Note:** Framework performance can vary by task type and prompt design. Always validate against your use case.

---

## Key Takeaways

- **MetaGPT** is ideal for modular, logic-heavy workflows  
- **CrewAI** is great for rapid prototyping and simple chains  
- **LangGraph** excels in complex flow and stateful task orchestration  
- Model choice significantly influences quality and coherence

---

## How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/agent-benchmark-suite.git
cd agent-benchmark-suite
