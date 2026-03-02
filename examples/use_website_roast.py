"""
Example: Using the Free AI Website Roast tool programmatically

This script shows how to use the Roast My Website tool via HTTP requests.
The tool is completely free -- no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/roast-my-website"


def roast_website(url: str) -> str:
    """
    Get a hilarious design and UX roast of any website.

    Args:
        url: The URL of the website to roast

    Returns:
        A funny but insightful roast of the website's design and UX
    """
    response = requests.post(TOOL_URL, data={
        "url": url
    })
    return response.text


if __name__ == "__main__":
    # Example: Roast a website
    roast = roast_website("https://example.com")
    print(roast)
