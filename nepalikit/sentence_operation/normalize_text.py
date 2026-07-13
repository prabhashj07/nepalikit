"""
normalize_text.py

Unicode normalization for Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import unicodedata


class TextNormalizer:
    """Normalize Unicode characters in Nepali text.

    Uses NFKC normalization to decompose and recompose Unicode
    characters into their canonical form.

    Args:
        text (str): The text to normalize.

    Examples:
        >>> normalizer = TextNormalizer("म  नाम   राम हो")
        >>> normalizer.normalize()
        'म  नाम   राम हो'
    """

    def __init__(self, text: str):
        self.text = text

    def normalize(self) -> str:
        """Normalize Unicode characters using NFKC form.

        Returns:
            str: The normalized text.
        """
        return unicodedata.normalize("NFKC", self.text)
