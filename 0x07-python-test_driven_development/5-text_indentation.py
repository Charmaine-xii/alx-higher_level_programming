#!/usr/bin/python3

def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n\n", end="")
        c += 1
