SmartVision Telegram Bot 🤖
SmartVision is an AI-powered Telegram bot built with Python, OpenAI GPT-4, and python-telegram-bot.
It can chat naturally, analyze photos, and runs 24/7 on a Mikrus VPS server.

🧩 Features
🧠 Chat and photo analysis using OpenAI GPT-4o
💬 Telegram integration via python-telegram-bot
🔐 Secure environment management with .env
🧪 Tested with pytest
🧹 Code quality checked with ruff
⚙️ Dependency & environment management using uv
☁️ Deployed on Mikrus VPS (runs 24/7 using nohup)
⚙️ Installation & Setup
# 1️⃣ Clone the repository
git clone https://github.com/USERNAME/smartvision-bot.git
cd smartvision-bot

# 2️⃣ Install dependencies (using uv)
pip install uv
uv pip install python-telegram-bot python-dotenv openai pytest ruff

# 3️⃣ Create a .env file and add your keys
TELEGRAM_TOKEN=your_telegram_token
OPENAI_API_KEY=your_openai_api_key

# 4️⃣ Run the bot
python3 telegrambot.py
# smartvision-bot
