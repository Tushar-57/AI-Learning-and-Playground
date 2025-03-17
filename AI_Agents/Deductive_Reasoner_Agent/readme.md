# Deductive Reasoning Agent 🕵️‍♂️

## Description 📝
`deductive_reasoner_agent.py` unleashes the `DeductiveReasonerAgent` from CAMEL to perform logical deductions and assess quality between states, all powered by a local language model.

### 🧠 Human Analogy
Picture a detective analyzing clues: starting with a case’s beginning (e.g., a project’s start) and deducing what must happen to reach the resolution (e.g., a milestone).

## Flow:
1. **Sets up** a local Llama 3.2 3B model via Ollama  
2. **Defines** a starting state (e.g., project start) and target state (e.g., milestone)  
3. **Creates** a `DeductiveReasonerAgent` with optional role descriptions  
4. **Deduces** conditions and assesses quality between states  
5. **Outputs** the logical conclusions to the console  

> **Highlight:** This script shows how AI can reason logically, perfect for problem-solving or planning!

Make sure you have the following ready:  
- **Python 3.x**  
- **CAMEL library** (`pip install camel-ai`)  
- **Ollama** with a local model (e.g., `ollama run llama3.2:3b`)  

## Usage 💻
Solve mysteries with AI reasoning in these steps:  

1. **Run the script directly:**  
   ```bash
   python deductive_reasoner_agent.py
   ```

## The Script Will:

- Deduce conditions between a project’s start and first milestone
- Print the logical conditions and quality assessment

## To use it with your own states(start, end)
``` python
agent = DeductiveReasonerAgent(model=m1_model)
deduction_result = agent.deduce_conditions_and_quality(starting_state="Your start", target_state="Your goal")
print(deduction_result)
```

## Code Features 🛠️

- Logical deduction from state transitions
- Quality assessment of outcomes
- Role-based context for reasoning
- Local model integration with Ollama

## What's in it for you 💡

- Learn how AI performs deductive reasoning
- Practice state-based problem-solving
- Explore applications in planning and evaluation
- Understand logical inference in agent design

## Highlights 📌

- **Analytical:** Breaks down complex scenarios into logical steps
- **Practical:** Useful for project planning or decision-making
- **Educational:** A clear intro to reasoning agents
- **Customizable:** Adjust states or roles for different use cases

Happy deducing! 🔍✨