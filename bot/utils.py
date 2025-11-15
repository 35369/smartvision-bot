import os
from typing import Dict


def load_env_vars() -> Dict[str, str]:
    """
    Çevresel değişkenleri yükler ve sözlük olarak döner.
    Testlerde monkeypatch ile kolayca sahte değer atanabilir.
    """
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN", ""),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    }


def analyze_photo_placeholder(photo_bytes: bytes) -> str:
    """
    Fotoğraf analiz fonksiyonu.
    Şimdilik boyuta göre sahte bir çıktı döner (pytest için ideal).
    Daha sonra OpenAI Vision API entegre edilecek.
    """
    size = len(photo_bytes)
    return f"Fotoğraf alındı (boyut: {size} bytes). Analiz daha sonra eklenecek."
