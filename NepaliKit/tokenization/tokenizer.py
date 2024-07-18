"""
tokenizer.py

Tokenizer module for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os
import string

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

    def tokenize(self, text, level='word', new_punctuation=None):
        """
        General tokenization method

        Parameters:
        - text: str, input text to tokenize 
        - level: str, level of tokenization ('sentence', 'word', 'character')
        - new_punctuation: list, additional punctuation to consider for word tokenization

        Returns:
        list, tokenized text based on specified level of tokenization.
        """
        if level == 'sentence':
            return self.sentence_tokenize(text)
        elif level == 'word':
            return self.word_tokenize(text, new_punctuation)
        elif level == 'characters':
            return self.character_tokenize(text)
        else:
            raise ValueError("Unsupported tokenization level. Choose from 'sentence', 'word', 'character'.")


    def sentence_detokenize(self, sentences):
        """Detokenizes a list of sentences back into the original text."""
        return u"।".join(sentences)

    def word_detokenize(self, words):
        """Detokenizes a list of words back into the original sentence."""
        return " ".join(words)

    def character_detokenize(self, characters):
        """Detokenizes a list of characters back into the original word."""
        return "".join(characters)

    def __str__(self):
        return "Tokenizer for Nepali language"

if __name__ == "__main__":
    tokenizer = Tokenizer()
