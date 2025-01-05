"""This module contains the pinput function for displaying styled input prompts."""
import sys


def pinput(prompt: str, customprompt=">> ") -> str:
    """Display a styled input prompt with a custom prefix.

    Args:
        prompt (str): The input prompt message.
        customprompt (str): A custom prefix for the input prompt.

    Returns:
        str: The user's input.
    """
    sys.stdout.write(prompt + "\n" + customprompt + "")
    sys.stdout.flush()
    return sys.stdin.readline().strip()
