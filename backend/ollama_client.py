import requests

OLLAMA_URL = "http://ollama:11434/api/generate"  # URL inside Docker


def generate_text(prompt):
    """
    Send a request to the Ollama server and return the generated text.
    """
    payload = {
        "model": "llama3.2:1b",  # Ensure this model is downloaded
        "prompt": prompt,
        "stream": False  # Use streaming if needed
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()  # Raise error if request failed
        return response.json()["response"]  # Extract response text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
