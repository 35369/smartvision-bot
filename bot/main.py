import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
from .handlers import start, handle_text, handle_photo


def main():
    """
    Entry point of the SmartVision Bot application.
    Loads environment variables and starts the Telegram bot.
    """
    # Load environment variables from .env file
    load_dotenv()

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN is missing. Please set it in the .env file.")

    # Create the Telegram bot application
    app = ApplicationBuilder().token(token).build()

    # Register command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("SmartVision Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

