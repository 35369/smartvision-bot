# SmartVision Telegram Bot 🤖

SmartVision is an AI-powered Telegram bot that can:
- Chat using OpenAI GPT models 🧠
- Analyze photos and describe them using image recognition 📸
- Run 24/7 on a mikr.us VPS server 🌐

## 🧩 Features
- Text and image understanding (GPT-4o)
- Telegram integration via `python-telegram-bot`
- Environment variables managed with `.env`
- Linting with `ruff`
- Testing with `pytest`
- Dependencies managed with `uv`

## 🚀 Run Instructions
```bash
uv init
uv add python-telegram-bot python-dotenv openai pytest ruff
python3 telegrambot.py
