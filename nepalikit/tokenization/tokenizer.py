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
        """Initialize the Tokenizer class and the current directory of the file."""
        self.this_dir = os.path.dirname(os.path.abspath(__file__))

    def sentence_tokenize(self, text):
        """
        Tokenizes input text into sentences based on '।' character.

        Parameters: 
        - text: str, input to tokenize into sentences.

        Returns:
        - list of str: tokenized sentences.
        """
        sentences = text.strip().split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences

    def word_tokenize(self, sentence, new_punctuation=None):
        """
        Tokenizes input sentence into words, handling specified punctuation.

        Parameters:
        - sentence: str, input sentence to tokenize into words.
        - new_punctuation: list, additional punctuation to consider for word tokenization.

        Returns:
        - list of str: tokenized words.
        """
        punctuations = ['।', ',', ';', '?', '!', '—', '-']
        if new_punctuation:
            punctuations.extend(new_punctuation)

        for punct in punctuations:
            sentence = ' '.join(sentence.split(punct))

        return sentence.split()

    def character_tokenize(self, word):
        """
        Tokenizes input word into characters.

        Parameters:
        - word: str, input word to tokenize into characters.

        Returns:
        - list of str: tokenized characters.
        """
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
        """
        Detokenizes a list of sentences back into the original text.

        Parameters:
        - sentences: list, tokenized sentences to be detokenized

        Returns:
        - str, original text formed by joining the sentences 

        """
        return u"।".join(sentences)

    def word_detokenize(self, words):
        """
        Detokenizes a list of words back into the original sentence.

        Parameters:
        - words: list, tokenized words to be detokenized.

        Returns:
        - str, original text fromed by joining the words

        """
        return " ".join(words)

    def character_detokenize(self, characters):
        """
        Detokenizes a list of characters back into the original word.

        Parameters:
        - characters: list, tokenized characters to be detokenizeed

        Returns:
        - str, original word formed by joining the characters 
        """
        return "".join(characters)

    def detokenize(self, tokens, level='word'):
        """
        General detokenization method

        Parameters:
        - tokens: list, tokenized text to be detokenized
        - level: str, level of detokenization ('sentence', 'word', 'character')

        Returns:
        - str, original text based on specified level of detokenization.
        """
        if level == 'sentence':
            return u"।".join(tokens)
        elif level == 'word':
            return " ".join(tokens)
        elif level == 'character':
            return "".join(tokens)
        else:
            raise ValueError("Unsupported detokenization level. Choose from 'sentence', 'word', 'character'.")

    def __str__(self):
        return "Tokenizer for Nepali language"

if __name__ == "__main__":
    tokenizer = Tokenizer()
