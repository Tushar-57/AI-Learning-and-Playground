
# Role-Playing Society Simulation 🎭

## Description 📝
`RolePlaying_withCamel.py` simulates a dynamic interaction between AI agents using CAMEL’s `RolePlaying` class, powered by a local model. It’s like a virtual stage where agents play out a scenario together!

### 🧠 Human Analogy
Imagine a play where two actors—a time traveler and a physicist—improvise a story about traveling to the past. The script guides their roles, but their dialogue emerges naturally!

## Flow:
1. **Initializes** a local Llama 3.2 3B model via Ollama  
2. **Defines** a task (e.g., "Develop a plan to travel to the past") and roles (e.g., user and assistant)  
3. **Sets up** a `RolePlaying` society with task and role arguments  
4. **Runs** a simulation loop where agents interact  
5. **Outputs** the conversation to the console  

> **Highlight:** This script brings multi-agent systems to life, showing how AI entities can collaborate or debate!

Make sure you have the following ready:  
- **Python 3.x**  
- **CAMEL library** (`pip install camel-ai`)  
- **Ollama** with a local model (e.g., `ollama run llama3.2:3b`)  

## Usage 💻
Watch your AI society in action with these steps:  

1. **Run the script directly:**  
   ```bash
   python role_playing.py
   ```

## The script will:

- Simulate a conversation between a time traveler and a physicist
- Print each agent’s responses until the task is done or the loop ends

## To customize it:
```python
task_kwargs = {'task_prompt': 'Your scenario'}
user_role_kwargs = {'user_role_name': 'Your role'}
assistant_role_kwargs = {'assistant_role_name': 'Their role'}
society = RolePlaying(**task_kwargs, **user_role_kwargs, **assistant_role_kwargs)
run(society)
```
## Code Features 🛠️
- Multi-agent interaction simulation
- Customizable roles and tasks
- Termination conditions for the simulation
- Local model support with Ollama

## What's in it for you 💡
- Explore how AI agents interact in a society
- Learn about multi-agent system design
- Experiment with creative scenarios and roles
- Understand emergent behaviors in AI conversations

## Highlights 📌
- Dynamic: Agents respond to each other in real-time
- Fun: Perfect for storytelling or simulation experiments
- Insightful: Reveals how AI can model complex interactions
- Flexible: Change the task or roles for new outcomes