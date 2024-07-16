"""
tokenizer.py

Tokenizer module for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os
import string
import torch
import sentencepiece as spm

class Tokenizer:
    def __init__(self):
        self.this_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory of the file

    def sentence_tokenize(self, text):
        """Tokenizes input text into sentences based on '।' character."""
        sentences = text.strip().split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences

    def word_tokenize(self, sentence, new_punctuation=None):
        """Tokenizes input sentence into words, handling specified punctuation."""
        punctuations = ['।', ',', ';', '?', '!', '—', '-']
        if new_punctuation:
            punctuations.extend(new_punctuation)

        for punct in punctuations:
            sentence = ' '.join(sentence.split(punct))

        return sentence.split()

    def character_tokenize(self, word):
        """Tokenizes input word into characters."""
        return list(word)

    def __str__(self):
        return "Tokenizer for Nepali language"

# Example usage:
if __name__ == "__main__":
    tokenizer = Tokenizer()

