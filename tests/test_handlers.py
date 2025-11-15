from bot.handlers import process_text, process_photo


def test_process_text():
    """
    Tests the behavior of the text processing function.
    """
    assert process_text("Hello") == "Received message: Hello"
    assert process_text("") == "I received an empty message."


def test_process_photo():
    """
    Tests that the photo processing returns the correct placeholder output.
    """
    fake_bytes = b"\x00\x01\x02"
    response = process_photo(fake_bytes)
    assert "Photo received" in response or "Fotoğraf alındı" in response
