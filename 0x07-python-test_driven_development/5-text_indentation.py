#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the given text with indentation.

    The function adds two newline characters ("\n\n") after each occurrence of ".", "?", and ":" in the text
    to create indentation.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print(text, end="")
