"""
tokenizer.py

Tokenizer module for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""


class Tokenizer:
    def __init__(self):
        """Initialize the Tokenizer class."""
        pass

    def sentence_tokenize(self, text):
        """
        Tokenize text into sentences.

        Splits on । ॥ ? ! while keeping punctuation attached to the
        preceding sentence.  A boundary is only recognised when the
        punctuation is followed by whitespace or end-of-string.

        Parameters:
        - text: str, input to tokenize into sentences.

        Returns:
        - list of str: tokenized sentences.
        """
        if not text:
            return []
        text = text.strip()
        if not text:
            return []

        sentences = []
        buf = ""
        for i, ch in enumerate(text):
            buf += ch
            if ch in ("।", "॥", "?", "!"):
                nxt = text[i + 1] if i + 1 < len(text) else None
                if nxt is None or nxt.isspace():
                    sentences.append(buf.strip())
                    buf = ""
        if buf.strip():
            sentences.append(buf.strip())
        return [s for s in sentences if s]

    def word_tokenize(self, sentence, new_punctuation=None):
        """
        Tokenize a sentence into words.

        Splits on whitespace and both Devanagari and Latin punctuation.
        Punctuation characters are dropped from the output.

        Parameters:
        - sentence: str, input sentence to tokenize into words.
        - new_punctuation: list, additional punctuation to consider.

        Returns:
        - list of str: tokenized words.
        """
        if not sentence:
            return []

        punctuations = [
            "।",
            "॥",
            ",",
            ";",
            ":",
            "?",
            "!",
            "'",
            "\u2018",
            "\u2019",
            '"',
            "\u201c",
            "\u201d",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            "/",
            "\\",
            "|",
            "<",
            ">",
            "—",
            "–",
            "-",
            "\u2010",
            "\u2011",
            "\u2012",
            "\u2013",
            "\u2014",
            "\u2015",
            ".",
            "\u0964",
            "\u0965",
        ]
        if new_punctuation:
            punctuations.extend(new_punctuation)

        for punct in punctuations:
            sentence = sentence.replace(punct, " ")

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

    def tokenize(self, text, level="word", new_punctuation=None):
        """
        General tokenization method

        Parameters:
        - text: str, input text to tokenize
        - level: str, level of tokenization ('sentence', 'word', 'character')
        - new_punctuation: list, additional punctuation to consider for word tokenization

        Returns:
        list, tokenized text based on specified level of tokenization.
        """
        if level == "sentence":
            return self.sentence_tokenize(text)
        elif level == "word":
            return self.word_tokenize(text, new_punctuation)
        elif level in ("character", "characters"):
            return self.character_tokenize(text)
        else:
            raise ValueError(
                "Unsupported tokenization level. Choose from 'sentence', 'word', 'character'."
            )

    def sentence_detokenize(self, sentences):
        """
        Detokenizes a list of sentences back into the original text.

        Parameters:
        - sentences: list, tokenized sentences to be detokenized

        Returns:
        - str, original text formed by joining the sentences

        """
        return "।".join(sentences)

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

    def detokenize(self, tokens, level="word"):
        """
        General detokenization method

        Parameters:
        - tokens: list, tokenized text to be detokenized
        - level: str, level of detokenization ('sentence', 'word', 'character')

        Returns:
        - str, original text based on specified level of detokenization.
        """
        if level == "sentence":
            return "।".join(tokens)
        elif level == "word":
            return " ".join(tokens)
        elif level == "character":
            return "".join(tokens)
        else:
            raise ValueError(
                "Unsupported detokenization level. Choose from 'sentence', 'word', 'character'."
            )

    def __str__(self):
        return "Tokenizer for Nepali language"
