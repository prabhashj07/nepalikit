"""
Stemmer module for Nepali language.

Provides rule-based suffix stripping for Nepali words, including
both a built-in stemmer and a Snowball stemmer wrapper.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.stemmer.stemmer import (
    NepaliStemmer,
    stem,
    stem_text,
    SnowballStemmer,
    snowball_stem,
)

__all__ = [
    "NepaliStemmer",
    "stem",
    "stem_text",
    "SnowballStemmer",
    "snowball_stem",
]
