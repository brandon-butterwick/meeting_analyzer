"""
Utilities for agent initialization and management
"""

from phi.agent import Agent
from phi.model.ollama import Ollama

def phidata_agent():
    """
    Create and initialize the meeting analyzer agent with the given system prompt
    """
    agent = Agent(
        name="Meeting Analyzer",
        description="A specialized tool designed to process meeting transcripts and produce actionable outputs",
        model=Ollama(model="llama3.2"),  # Using llama3.2 model from ollama
        system_prompt="system_prompt"
    )

    return agent
