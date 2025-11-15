from .utils import analyze_photo_placeholder


# ---------------------------------------
#  PURE BUSINESS LOGIC (testable)
# ---------------------------------------

def process_text(text: str) -> str:
    """
    Processes an incoming text message.
    GPT integration will be added later.
    """
    if not text:
        return "I received an empty message."
    return f"Received message: {text}"


def process_photo(photo_bytes: bytes) -> str:
    """
    Processes photo bytes.
    Currently uses a placeholder analysis function.
    """
    return analyze_photo_placeholder(photo_bytes)


# ---------------------------------------
#  TELEGRAM HANDLERS (async functions)
# ---------------------------------------

async def start(update, context):
    """
    Handles the /start command.
    """
    await update.message.reply_text(
        "Welcome to SmartVision Bot! You can start sending messages."
    )


async def handle_text(update, context):
    """
    Handles incoming text messages.
    """
    msg = update.message.text or ""
    response = process_text(msg)
    await update.message.reply_text(response)


async def handle_photo(update, context):
    """
    Handles incoming photos sent by the user.
    Downloads the photo bytes and processes them.
    """
    photos = update.message.photo
    if not photos:
        await update.message.reply_text("No photo found.")
        return

    # Get the highest resolution photo
    photo = photos[-1]
    file = await photo.get_file()
    bio = await file.download_as_bytearray()

    response = process_photo(bytes(bio))
    await update.message.reply_text(response)
