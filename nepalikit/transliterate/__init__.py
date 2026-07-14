"""
Transliteration module for Nepali language.

Provides character-level Roman to Devanagari and Devanagari to Roman conversion,
as well as Preeti font to Unicode conversion.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.transliterate.preeti import PreetiConverter, preeti_to_unicode
from nepalikit.transliterate.transliterate import (
    NepaliTransliterator,
    devanagari_to_roman,
    roman_to_devanagari,
)

__all__ = [
    "NepaliTransliterator",
    "roman_to_devanagari",
    "devanagari_to_roman",
    "PreetiConverter",
    "preeti_to_unicode",
]
