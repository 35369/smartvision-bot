import os

def test_env_file_exists():
    assert os.path.exists(".env"), "Missing .env file!"

def test_python_file_exists():
    assert os.path.exists("telegrambot.py"), "Bot file not found!"

def test_env_has_token():
    with open(".env", "r") as f:
        data = f.read()
        assert "TELEGRAM_TOKEN" in data, "Missing TELEGRAM_TOKEN in .env"

