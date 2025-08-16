##Deep Research Scoping with LangGraph Agents
This repository contains a Jupyter Notebook that demonstrates how to use LangGraph agents for deep research scoping. The notebook focuses on clarifying user queries, generating structured research briefs, and evaluating the results using LangSmith.
##Overview
The notebook implements a multi-step process for research scoping:

- User Clarification: Determines if more information is needed from the user via structured prompts and decisions.
- Brief Generation: Transforms conversation history into a detailed research brief.
- Workflow with LangGraph: Builds a stateful graph to manage the scoping process, including nodes for clarification and brief writing.
- Evaluation: Uses LangSmith to evaluate the generated research briefs against success criteria, checking for completeness and absence of unwarranted assumptions.

**Key concepts include:**

* LangGraph for agent workflows and state management.
* Pydantic schemas for structured outputs.
* LLM-as-judge for evaluation.
* Handling vague user inputs in research tasks.

The notebook is based on a Colab file: Deep Research Scoping with Langgraph Agents.ipynb.
