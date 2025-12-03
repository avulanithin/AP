"""
A tiny helper module that wraps the Google Gemini client
and exposes two simple functions for this assignment:

- ask_gemini(prompt: str) -> str
- summarize_text(text: str) -> str

It uses the official google-genai library and the model "gemini-2.5-flash".
The code is synchronous and designed to be easy to read for beginners.
"""
from typing import Optional

# Import the official Google GenAI SDK
from google import genai

# Import the API key from the local config file
from config import API_KEY


# We'll create the client lazily the first time it's needed
_client: Optional[genai.Client] = None


def _validate_api_key() -> None:
    """Ensure the user has set a real API key in config.py.

    Raises:
        ValueError: If the API key is missing or still the placeholder.
    """
    if not API_KEY or API_KEY == "API_KEY":
        raise ValueError(
            "Gemini API key not set. Open config.py and replace 'API_KEY' "
            "with your actual key from Google AI Studio (https://aistudio.google.com/apikey)."
        )


def _get_client() -> genai.Client:
    """Create (once) and return a Google GenAI client using the API key.

    Returns:
        genai.Client: A configured client for the Gemini API.
    """
    global _client
    if _client is None:
        _validate_api_key()
        # Create a client for the Gemini Developer API using the provided key
        _client = genai.Client(api_key=API_KEY)
    return _client


def ask_gemini(prompt: str) -> str:
    """Send a general text prompt to the Gemini model and return plain text.

    Args:
        prompt: The user's question or instruction.

    Returns:
        The model's response as a simple string.

    Notes:
        - Uses the synchronous SDK call: client.models.generate_content(...)
        - Uses the model: "gemini-2.5-flash" as required by the assignment.
        - `response.text` returns the plain text from the model.
    """
    client = _get_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    # The SDK exposes a convenient .text property for text output
    return response.text


def summarize_text(text: str) -> str:
    """Summarize a long text using the Gemini model.

    The function prepends a clear instruction and then appends the user's text.

    Args:
        text: The long text to summarize.

    Returns:
        A short, simple summary as a string.
    """
    client = _get_client()

    instruction = (
        "Summarize the following text in simple language. "
        "Keep it short, clear, and easy to understand:\n\n"
    )
    prompt = instruction + text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
