"""
Example: Using the Free AI Email Writer programmatically

This script shows how to use the AI Email Writer tool via HTTP requests.
The tool is completely free — no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/email-writer"


def generate_email(context: str, tone: str = "professional") -> str:
    """
    Generate a professional email using the AI Email Writer.

    Args:
        context: Describe what you want the email to say
        tone: One of "professional", "casual", "follow-up"

    Returns:
        Generated email text
    """
    response = requests.post(TOOL_URL, data={
        "context": context,
        "tone": tone
    })
    return response.text


if __name__ == "__main__":
    # Example: Generate a job application follow-up
    email = generate_email(
        context="Follow up on my software engineering internship application at Google. "
                "I applied 2 weeks ago and haven't heard back. I'm very excited about the role.",
        tone="professional"
    )
    print(email)
