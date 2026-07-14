"""
manage_stopwords.py

Stopword management for Nepali language.

Provides both the legacy API (load_stopwords, remove_stopwords_from_text)
and the enhanced API (get_stopwords, add_stopwords, is_stopword, etc.).

The curated stopword list (340+ words) is based on community resources
and Nepali grammar references.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os
from importlib import resources

_STOPWORDS = None
_CUSTOM_STOPWORDS: set[str] = set()


def _load_default_stopwords():
    """Load stopwords from the bundled data file on first access."""
    global _STOPWORDS
    if _STOPWORDS is not None:
        return
    words = set()
    try:
        data = resources.files("nepalikit").joinpath("data/stopwords.txt").read_text(encoding="utf-8")
        for line in data.splitlines():
            w = line.strip()
            if w and not w.startswith("#"):
                words.add(w)
    except (FileNotFoundError, TypeError):
        pass
    _STOPWORDS = words


def get_stopwords():
    """
    Get the default set of Nepali stopwords (340+ curated words).

    Returns:
        set: A set of stopword strings.

    Examples:
        >>> stopwords = get_stopwords()
        >>> "र" in stopwords
        True
    """
    _load_default_stopwords()
    return _STOPWORDS.copy()


def is_stopword(word):
    """
    Check if a word is a stopword.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a stopword.

    Examples:
        >>> is_stopword("र")
        True
        >>> is_stopword("नेपाल")
        False
    """
    _load_default_stopwords()
    return word in _STOPWORDS


def add_stopwords(words):
    """
    Add custom stopwords to the active set.

    Args:
        words (str or list): A single word or list of words to add.

    Examples:
        >>> add_stopwords(["नेपाल", "काठमाडौं"])
        >>> is_stopword("नेपाल")
        True
    """
    _load_default_stopwords()
    if isinstance(words, str):
        words = [words]
    for w in words:
        w = w.strip()
        if w:
            _STOPWORDS.add(w)
            _CUSTOM_STOPWORDS.add(w)


def remove_custom_stopwords(words):
    """
    Remove previously added custom stopwords from the active set.

    Args:
        words (str or list): A single word or list of words to remove.

    Examples:
        >>> add_stopwords(["नेपाल"])
        >>> remove_custom_stopwords(["नेपाल"])
        >>> is_stopword("नेपाल")
        False
    """
    _load_default_stopwords()
    if isinstance(words, str):
        words = [words]
    for w in words:
        w = w.strip()
        if w and w in _CUSTOM_STOPWORDS:
            _STOPWORDS.discard(w)
            _CUSTOM_STOPWORDS.discard(w)


def remove_stopwords_from_text(text, stopwords=None):
    """
    Remove stopwords from the given text.

    Args:
        text (str): Input text from which stopwords are to be removed.
        stopwords (list or set, optional): List of stopwords. If None, uses
            the default stopword list.

    Returns:
        str: Cleaned text with stopwords removed.

    Examples:
        >>> remove_stopwords_from_text("म घर जाँदै छु")
        "घर जाँदै"
    """
    if not text or not text.strip():
        return text

    if stopwords is None:
        stopwords = get_stopwords()

    tokens = text.split()
    filtered_tokens = [word for word in tokens if word not in stopwords]
    return " ".join(filtered_tokens)


# Legacy API - preserved for backward compatibility
def load_stopwords(folder_path):
    """
    Load stopwords from text files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing stopwords text files.

    Returns:
        list: A list of stopwords loaded from all text files in the folder.
    """
    stopwords = []
    if not os.path.isdir(folder_path):
        return stopwords
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), encoding="utf-8") as file:
                stopwords.extend([line.strip() for line in file.readlines()])
    return stopwords
