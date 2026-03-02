"""
Example: Using the Free AI Regex Generator programmatically

This script shows how to use the AI Regex Generator tool via HTTP requests.
The tool is completely free -- no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/regex-generator"


def generate_regex(description: str) -> str:
    """
    Generate a regex pattern from a plain English description.

    Args:
        description: Plain English description of what you want to match
                     (e.g., "match email addresses", "extract phone numbers")

    Returns:
        A working regex pattern with explanation and test examples
    """
    response = requests.post(TOOL_URL, data={
        "description": description
    })
    return response.text


if __name__ == "__main__":
    # Example 1: Match email addresses
    print("=== Email Address Regex ===")
    result = generate_regex("Match all valid email addresses")
    print(result)

    print("\n" + "=" * 50 + "\n")

    # Example 2: Extract US phone numbers
    print("=== US Phone Number Regex ===")
    result = generate_regex(
        "Match US phone numbers in formats like (555) 123-4567, "
        "555-123-4567, 5551234567, and +1-555-123-4567"
    )
    print(result)
