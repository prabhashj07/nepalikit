"""
Normalizer module for Nepali language.

Provides Unicode normalization, ZWNJ/ZWJ stripping, and script detection.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.normalizer.normalizer import (
    NepaliNormalizer,
    contains_devanagari,
    contains_latin,
    detect_script,
    is_devanagari,
    mixed_script_ratio,
    normalize,
)

__all__ = [
    "NepaliNormalizer",
    "normalize",
    "detect_script",
    "is_devanagari",
    "contains_devanagari",
    "contains_latin",
    "mixed_script_ratio",
]
