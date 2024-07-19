"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from typing import Dict
from nepalikit.tokenization.tokenizer import Tokenizer
from nepalikit.manage_stopwords.manage_stopwords import load_stopwords

class SentenceAnalyzer:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.stopwords = load_stopwords()
        
    def sentence_stats(self, sentence: str) -> Dict[str, int]:
        """Compute statistics for a given sentence."""
        tokens = self.tokenizer.tokenize(sentence)
        return {
            'char_count': len(sentence),
            'word_count': len(tokens),
            'stopword_count': sum(1 for token in tokens if token in self.stopwords),
            'punctuation_count': sum(1 for char in sentence if char in '।?!,;:')
        }


