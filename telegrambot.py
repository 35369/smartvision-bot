from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
import os
import openai

# === Load environment variables ===
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Conversation memory per user ===
chat_history = {}

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm SmartVision Bot.\nYou can chat with me or send a photo for AI analysis 💬📸"
    )

# === Handle text messages ===
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_message = (update.message.text or "").strip()
    print(f"📩 [TEXT] From {user_id}: {user_message}")

    if not user_message:
        return

    # Create user history if doesn't exist
    if user_id not in chat_history:
        chat_history[user_id] = [
            {
                "role": "system",
                "content": "You are SmartVision, a polite, friendly, and intelligent English-speaking AI assistant.",
            }
        ]

    chat_history[user_id].append({"role": "user", "content": user_message})

    try:
        # Generate OpenAI response with previous context
        resp = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat_history[user_id],
        )

        reply = resp.choices[0].message.content
        chat_history[user_id].append({"role": "assistant", "content": reply})

        await update.message.reply_text(reply)
        print(f"🤖 [REPLY] {reply}")

    except Exception as e:
        print(f"⚠️ [ERROR - TEXT] {e}")
        await update.message.reply_text(f"⚠️ Error generating reply: {e}")

# === Handle photo messages (context-aware) ===
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    print(f"📸 [PHOTO] {user.first_name} ({user.id}) sent a photo.")

    try:
        file = await update.message.photo[-1].get_file()
        file_path = file.file_path

        # ✅ FIX: handle full or partial Telegram file paths correctly
        if file_path.startswith("https://"):
            image_url = file_path
        else:
            image_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

        print(f"🌐 [PHOTO URL] {image_url}")

        await update.message.reply_text("📷 Photo received! Analyzing, please wait...")

        # Send image to OpenAI Vision for analysis
        result = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in detail."},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                }
            ],
        )

        description = result.choices[0].message.content

        # ✅ Add the image analysis result into conversation memory
        if user_id not in chat_history:
            chat_history[user_id] = [
                {
                    "role": "system",
                    "content": "You are SmartVision, a polite, friendly, and intelligent English-speaking AI assistant.",
                }
            ]

        chat_history[user_id].append({"role": "user", "content": "I sent you a photo."})
        chat_history[user_id].append({"role": "assistant", "content": description})

        await update.message.reply_text(f"🧠 AI Analysis:\n{description}")
        print(f"🧠 [VISION RESULT] {description}")

    except Exception as e:
        print(f"⚠️ [ERROR - PHOTO] {e}")
        await update.message.reply_text(f"⚠️ Error analyzing photo: {e}")

# === Main app ===
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🤖 SmartVision Bot is active! You can send text or photos.")
    print("📡 Waiting for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()
