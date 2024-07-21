"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import unicodedata

class TextNormalizer:
    def __init__(self, text: str):
        self.text = text

    def normalize(self) -> str:
        """Normalize Unicode characters in Nepali text."""
        return unicodedata.normalize('NFKC', self.text)

