"""
segment_sentences.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.sentence_operation.extract_sentences import (
    extract_sentences as ExtractSentences,
)


def segment_sentences(text: str) -> list:
    """
    Segment text into sentences.

    Uses extract_sentences to split on punctuation marks, then returns
    the list of sentences.

    Args:
        text (str): Input text to segment.

    Returns:
        list: List of sentence strings.
    """
    extractor = ExtractSentences(text)
    return extractor.extract_sentences()
