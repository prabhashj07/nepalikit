"""
sentence_stats.py

Sentence statistics for Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from typing import Dict

from nepalikit.manage_stopwords import get_stopwords
from nepalikit.tokenization.tokenizer import Tokenizer


class SentenceAnalyzer:
    """Compute statistics for a given Nepali sentence.

    Provides character count, word count, stopword count, and
    punctuation count for a sentence.

    Examples:
        >>> analyzer = SentenceAnalyzer()
        >>> stats = analyzer.sentence_stats("म घर जाँदै छु।")
        >>> stats['word_count']
        4
    """

    def __init__(self):
        self.tokenizer = Tokenizer()
        self.stopwords = get_stopwords()

    def sentence_stats(self, sentence: str) -> Dict[str, int]:
        """Compute statistics for a given sentence.

        Args:
            sentence (str): The sentence to analyze.

        Returns:
            dict: Keys are 'char_count', 'word_count',
                'stopword_count', 'punctuation_count'.
        """
        tokens = self.tokenizer.tokenize(sentence)
        return {
            "char_count": len(sentence),
            "word_count": len(tokens),
            "stopword_count": sum(1 for token in tokens if token in self.stopwords),
            "punctuation_count": sum(1 for char in sentence if char in "।?!,;:"),
        }
