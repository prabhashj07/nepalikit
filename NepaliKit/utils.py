"""
utils.py

Utility functions for text processing in Nepali language.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from collections import Counter

def get_word_frequency(tokens):
    """Get word frequency from tokenized text."""
    from collections import Counter
    return Counter(tokens)

def split_text(text, delimiter=' '):
    """Split text by a delimiter."""
    return text.split(delimiter)

def merge_text(tokens, delimiter=' '):
    """Merge tokens into text with a delimiter."""
    return delimiter.join(tokens)

def count_word(text):
    """count total words in a sentence."""
    tokens = split_text(text)
    return len(tokens)

def count_words_in_paragraph(paragraph):
    """Count total words in a paragraph."""
    total_words = 0
    sentences = paragraph.split('.')
    for sentence in sentences:
        total_words += count_word(sentence)
    return total_words 

# Example usage
if __name__ == "__main__":
    pass
