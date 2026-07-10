import requests

from config import OLLAMA_URL, OLLAMA_MODEL


def generate_sql(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1
            }
        }
    )

    response.raise_for_status()

    raw_text = response.json()["response"]

    return raw_text.strip()
