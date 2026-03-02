"""
Example: Using the Free AI Code Roast tool programmatically

This script shows how to use the AI Code Roast tool via HTTP requests.
The tool is completely free -- no API key needed.
"""

import requests

TOOL_URL = "https://crazeemedia.app.n8n.cloud/webhook/roast-code-api"


def roast_code(code: str, language: str = "python") -> str:
    """
    Get your code hilariously roasted by AI.

    Args:
        code: The source code to roast
        language: Programming language (python, javascript, go, rust, etc.)

    Returns:
        A funny but educational code roast with a Roast Score
    """
    response = requests.post(TOOL_URL, data={
        "code": code,
        "language": language
    })
    return response.text


if __name__ == "__main__":
    # Example: Roast some questionable JavaScript
    sample_code = '''
var x = new Array();
for (var i = 0; i < 10; i++) {
    x.push(i);
}
console.log(x);

function addNumbers(a, b) {
    return parseInt(a) + parseInt(b);
}

var result = addNumbers("5", "3");
console.log(result);
'''

    roast = roast_code(sample_code, "javascript")
    print(roast)
