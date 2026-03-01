"""
Example: Using the Free AI LinkedIn Post Generator programmatically

This script shows how to use the AI LinkedIn Post Generator via HTTP requests.
The tool is completely free — no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/linkedin-writer"


def generate_linkedin_post(topic: str, tone: str = "professional") -> str:
    """
    Generate an engaging LinkedIn post using AI.

    Args:
        topic: What you want to post about
        tone: One of "professional", "storytelling", "thought-leadership"

    Returns:
        Generated LinkedIn post with hooks and hashtags
    """
    response = requests.post(TOOL_URL, data={
        "topic": topic,
        "tone": tone
    })
    return response.text


if __name__ == "__main__":
    # Example: Generate a post about launching a project
    post = generate_linkedin_post(
        topic="I just finished building 3 free AI tools in 24 hours as a 17-year-old developer. "
              "Here's what I learned about shipping fast and building in public.",
        tone="storytelling"
    )
    print(post)
