# pip install langchain langchain-openai langchain-anthropic

from langchain_core.tools import tool
import os
import re

MEMORY_FILE = "agent_brain.txt"

@tool
def read_memory() -> str:
    """Use this tool to read past memories, facts, and context about the user from your local file."""
    if not os.path.exists(MEMORY_FILE):
        return "No memories recorded yet."
    with open(MEMORY_FILE, "r") as f:
        return f.read()

@tool
def save_memory(fact: str) -> str:
    """Use this tool to save a new, important fact or summary about the user to your local file."""
    with open(MEMORY_FILE, "a") as f:
        f.write(f"- {fact}\n")
    return f"Successfully saved: {fact}"

@tool
def search_memory_for_regex(pattern: str) -> str:
    """Use this tool to search for a regex pattern in your local memory file.
    Returns all matching lines or 'No matches found.' if nothing matches."""
    if not os.path.exists(MEMORY_FILE):
        return "No memories recorded yet."

    with open(MEMORY_FILE, "r") as f:
        lines = f.readlines()

    matches = []
    for i, line in enumerate(lines, 1):
        if re.search(pattern, line, re.IGNORECASE):
            matches.append(f"Line {i}: {line.strip()}")

    if matches:
        return "Found matches:\n" + "\n".join(matches[:10])  # Limit to 10 matches
    return "No matches found."
