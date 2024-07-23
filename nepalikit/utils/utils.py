"""
utils.py

Utility class for text processing in Nepali language.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from collections import Counter

class NepaliTextProcessor:
    """
    A class for processing Nepali text, including merging and splitting text,
    and counting words in sentences and paragraphs.

    Attributes:
    ----------
    delimiter: str
    The delimiter used to split or join text tokens (default - space).

    Methods:
    -------
    merge_text(tokens):
    - Merges a list of tokens into a single string, separated by the delimiter.

    split_text(text):
    - Splits a text string into a list of tokens using the delimiter.

    count_words(text):
    - Counts the number of words in a text string by splitting it with the delimiter.

    count_words_in_paragraph(paragraph):
    - Counts the total number of words in a paragraph, where the paragraph is split into sentences.

    """
    def __init__(self, delimiter=' '):
        """
        Initialize the NepaliTextProcessor with a specified delimiter.

        Parameters:
        delimiter: str(optional), the delimiter used to split or join text tokens(default - space).
        """
        self.delimiter = delimiter

    def merge_text(self, tokens):
        """
        Merge tokens into text with a delimiter.

        Parameters:
        tokens: list of str, a list of text tokens to be merged.

        Returns:
        str, a single string where tokens are joined by the delimiter.
        """
        return self.delimiter.join(tokens)

    def split_text(self, text):
        """
        Split text by a delimiter.

        Parameters:
        text: str, the text string to be split. 

        Returns:
        list of str, a list of tokens obtained by splitting the text using the delimiter.
        """
        return text.split(self.delimiter)

    def count_words(self, text):
        """
        Count total words in a sentence.

        Parameters:
        text: str, the text string whose words are to be counted.

        Returns:
        int: the number of words in the text string.

        """
        tokens = self.split_text(text)
        return len(tokens)

    def count_words_in_paragraph(self, paragraph):
        """
        Count total words in a paragraph.

        Parameters:
        str: the paragraph whose words are to be counted.

        Returns:
        int: the total number of words in the paragraph.
        """
        total_words = 0
        sentences = paragraph.split('.')
        for sentence in sentences:
            total_words += self.count_words(sentence)
        return total_words


