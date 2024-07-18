"""
load_stopwords.py

Load stopwords from text files in a specified folder.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os

def load_stopwords(folder_path):
    """
    Load stopwords from text files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing stopwords text files.

    Returns:
        list: A list of stopwords loaded from all text files in the folder.
    """
    stopwords = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Ensure only text files are considered
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                stopwords.extend([line.strip() for line in file.readlines()])
    return stopwords

def remove_stopwords_from_text(text, stopwords):
    """
    Remove stopwords from the given text.

    Args:
        text (str): Input text from which stopwords are to be removed.
        stopwords (list): List of stopwords to be removed.

    Returns:
        str: Cleaned text with stopwords removed.
    """
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
    return ' '.join(filtered_tokens)


