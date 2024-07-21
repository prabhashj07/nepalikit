"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.sentence_operation.extract_sentences import extract_sentences
from nepalikit.sentence_operation.load_abbreviation import load_abbreviations
from nepalikit.sentence_operation.normalize_text import TextNormalizer
from nepalikit.sentence_operation.replace_abbreviations import AbbreviationReplacer
from nepalikit.sentence_operation.segment_sentences import segment_sentences
from nepalikit.sentence_operation.sentence_stats import SentenceAnalyzer

__all__ = [
    'extract_sentences',
    'load_abbreviations',
    'TextNormalizer',
    'AbbreviationReplacer',
    'segment_sentences',
    'SentenceAnalyzer',
]

