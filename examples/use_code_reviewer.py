"""
Example: Using the Free AI Code Reviewer programmatically

This script shows how to use the AI Code Reviewer tool via HTTP requests.
The tool is completely free — no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/code-review"


def review_code(code: str, language: str = "python") -> str:
    """
    Get an AI-powered code review.

    Args:
        code: The source code to review
        language: Programming language (python, javascript, go, rust, etc.)

    Returns:
        Detailed code review with suggestions
    """
    response = requests.post(TOOL_URL, data={
        "code": code,
        "language": language
    })
    return response.text


if __name__ == "__main__":
    # Example: Review a Python function
    sample_code = '''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first 40 fibonacci numbers
for i in range(40):
    print(f"fib({i}) = {fibonacci(i)}")
'''

    review = review_code(sample_code, "python")
    print(review)
