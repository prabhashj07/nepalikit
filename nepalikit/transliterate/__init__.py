"""
Transliteration module for Nepali language.

Provides character-level Roman to Devanagari and Devanagari to Roman conversion.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.transliterate.transliterate import (
    NepaliTransliterator,
    roman_to_devanagari,
    devanagari_to_roman,
)

__all__ = [
    "NepaliTransliterator",
    "roman_to_devanagari",
    "devanagari_to_roman",
]
