
---

### 2. TaskSpecifyAgent/
- **File Name:** `task_specify_agent.py`
- **README.md:**

```markdown
# Task Specification Agent 🛠️

## Description 📝
`task_specify_agent.py` showcases the power of the `TaskSpecifyAgent` from the CAMEL library, refining vague tasks into detailed, actionable ones using a local language model.

### 🧠 Human Analogy
Think of this agent as a personal coach who takes your rough idea—like "get a promotion"—and turns it into a clear game plan, tailored to your role (e.g., a Software Engineer or Student).

## Flow:
1. **Sets up** a local Llama 3.2 3B model via Ollama  
2. **Creates** a `TaskSpecifyAgent` with a custom prompt template or task type  
3. **Receives** a vague task prompt and optional metadata (e.g., occupation or role)  
4. **Generates** a specific, detailed task description  
5. **Outputs** the refined task to the console  

> **Highlight:** This script demonstrates how AI can clarify your goals, making it a productivity booster!

Make sure you have the following ready:  
- **Python 3.x**  
- **CAMEL library** (`pip install camel-ai`)  
- **Ollama** with a local model (e.g., `ollama run llama3.2:3b`)  

## Usage 💻
Turn vague ideas into clear tasks with these steps:  

1. **Run the script directly:**  
   ```bash
   python task_specify_agent.py
   ```

## The Script Will:

- Take a sample task (e.g., "get promotion" or "clear an interview")
- Refine it based on metadata (e.g., occupation or role)
- Print the specified task

### To use it with your own task:

```python
task_specify_agent = TaskSpecifyAgent(model=finalModelToUse)
response = task_specify_agent.run(task_prompt="Your task", meta_dict={"occupation": "Your role"})
print(response)
```

## Code Features 🛠️
- Custom prompt templates for task refinement
- Metadata support for context-aware specification
- Local model integration with Ollama
- Flexible task type configuration


## Highlights 📌

- **Context-Sensitive:**  Adapts to your role or scenario
- **Practical:** Apply it to real world goals

Happy task refining! 📋🚀