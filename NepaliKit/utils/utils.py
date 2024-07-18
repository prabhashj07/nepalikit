"""
utils.py

Utility class for text processing in Nepali language.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from collections import Counter

class NepaliTextProcessor:
    def __init__(self, delimiter=' '):
        self.delimiter = delimiter

    def merge_text(self, tokens):
        """Merge tokens into text with a delimiter."""
        return self.delimiter.join(tokens)

    def split_text(self, text):
        """Split text by a delimiter."""
        return text.split(self.delimiter)

    def count_words(self, text):
        """Count total words in a sentence."""
        tokens = self.split_text(text)
        return len(tokens)

    def count_words_in_paragraph(self, paragraph):
        """Count total words in a paragraph."""
        total_words = 0
        sentences = paragraph.split('.')
        for sentence in sentences:
            total_words += self.count_words(sentence)
        return total_words


