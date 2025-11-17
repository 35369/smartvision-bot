import os
from typing import Dict


def load_env_vars() -> Dict[str, str]:
    """
    Loads environment variables and returns them as a dictionary.
    In tests, fake values can easily be injected using monkeypatch.
    """
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN", ""),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    }


def analyze_photo_placeholder(photo_bytes: bytes) -> str:
    """
    Photo analysis placeholder function.
    For now, it returns a fake output based on file size (ideal for pytest).
    OpenAI Vision API integration will be added later.
    """
    size = len(photo_bytes)
    return f"Photo received (size: {size} bytes). Analysis will be added later."


