import re


def remove_think_tags(text):
    """
    Remove all content within <think>...</think> tags from the given text.

    Parameters:
        text (str): The input text containing <think> tags.

    Returns:
        str: The text with all <think> tags and their content removed.
    """
    # Use re.DOTALL to ensure the dot matches newline characters.
    cleaned_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return cleaned_text
