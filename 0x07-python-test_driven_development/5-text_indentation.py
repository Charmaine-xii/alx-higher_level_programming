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

    lines = text.splitlines()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            for char in stripped_line:
                print(char, end="")
                if char in ".?:":  # Check for '.', '?', or ':'
                    print("\n\n", end="")
            print()  # Add a newline after each line
