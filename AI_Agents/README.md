# CAMEL Agents with Local Models 🤖

Welcome to the CAMEL Agents project! This repository contains implementations and examples of various AI agents using the CAMEL library, all powered by local language models via Ollama. Each folder focuses on a different aspect of agent development, from simple chatbots to multi-agent simulations, logical reasoning, and prompt generation for coding tasks.

## 🌟 Overview
This project demonstrates how to implement CAMEL (Conversational Agents with Memory and Extensible Logic) using local models, allowing you to experiment with AI agents without worrying about token limits or external APIs. The repository is structured to help you explore different agent types and utilities, each with its own script and detailed documentation.

## 🛠️ Prerequisites
Before diving in, ensure you have the following installed:
- **Python 3.x**
- **CAMEL library** (`pip install camel-ai`)
- **Ollama** with a local model (e.g., `ollama run llama3.2:3b`)

## 📂 Project Structure
The repository is organized into the following folders, each containing a Python script and a detailed `README.md`:

1. **ChatAgent/**  
   - **File:** `chat_agent.py`  
   - **Description:** Demonstrates a conversational AI agent that can act as a helpful assistant or a specialized expert, like a financial advisor.

2. **TaskSpecifyAgent/**  
   - **File:** `task_specify_agent.py`  
   - **Description:** Shows how to refine vague tasks into detailed, actionable plans using AI, tailored to specific roles or contexts.

3. **RolePlaying/**  
   - **File:** `role_playing.py`  
   - **Description:** Simulates interactions between multiple AI agents in a society, each with their own roles, to collaboratively solve a task.

4. **DeductiveReasonerAgent/**  
   - **File:** `deductive_reasoner_agent.py`  
   - **Description:** Utilizes logical deduction to analyze transitions between states, useful for planning and problem-solving.

5. **CamelCodePrompts/**  
   - **Description:** Provides utilities for generating prompts related to programming languages, coding tasks, and AI coding assistants.

## 💻 Usage
Each folder contains a Python script that can be run directly. For example:
```bash
python ChatAgent/chat_agent.py
```
> **Highlight:** Refer to the individual README.md files in each folder for detailed instructions, code explanations, and customization options.