#!/usr/bin/python3
"""
Contains a function that prints text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, f"{char}\n\n")

    lines = [line.strip() for line in text.splitlines()]
    result = "\n".join(lines)
    print(result, end="")
