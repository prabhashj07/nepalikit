"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import unicodedata

def normalize_text(text: str) -> str:
    """Normalize Unicode characters in Nepali text."""
    return unicodedata.normalize('NFKC', text)

