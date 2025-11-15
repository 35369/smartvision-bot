from bot.utils import load_env_vars


def test_env_vars(monkeypatch):
    """
    Ensures environment variables are correctly loaded.
    """
    monkeypatch.setenv("TELEGRAM_TOKEN", "fake-token")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    envs = load_env_vars()

    assert envs["TELEGRAM_TOKEN"] == "fake-token"
    assert envs["OPENAI_API_KEY"] == "fake-key"
