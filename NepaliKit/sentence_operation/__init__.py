"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from .extract_sentences import extract_sentences
from .load_abbreviation import load_abbreviations
from .normalize_text import normalize_text
from .replace_abbreviations import AbbreviationReplacer
from .segment_sentences import segment_sentences
from .sentence_stats import SentenceAnalyzer

__all__ = [
    'extract_sentences',
    'load_abbreviations',
    'normalize_text',
    'AbbreviationReplacer',
    'segment_sentences',
    'SentenceAnalyzer',
]

