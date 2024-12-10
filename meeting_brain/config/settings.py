"""
Configuration settings for the Meeting Analyzer Agent
"""

import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# File Paths Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs", "summaries")

# Ensure output directory exists
os.makedirs(OUTPUTS_DIR, exist_ok=True)
