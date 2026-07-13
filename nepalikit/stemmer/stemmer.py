"""
stemmer.py

Rule-based stemmer for Nepali language.
Strips common Nepali suffixes to reduce words to their root forms.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import json
from importlib import resources


class NepaliStemmer:
    """
    Rule-based stemmer for Nepali language.

    Implements suffix stripping for common Nepali inflections
    including case markers, possessives, plurals, and verb endings.
    Suffixes are tried longest-first so composite forms like
    'हरूकोलागि' are stripped before shorter ones like 'को'.

    Args:
        min_residue (int): Minimum stem length after stripping. Default 2.
    """

    def __init__(self, min_residue=2):
        self.min_residue = min_residue
        pkg = resources.files("nepalikit")
        rules_path = str(pkg.joinpath("data", "stemmer_rules.json"))
        try:
            with open(rules_path, "r", encoding="utf-8") as f:
                rules = json.load(f)
            self.suffixes = rules.get("suffixes", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.suffixes = [
                "हरूकोलागि",
                "हरूकालागि",
                "हरूको",
                "हरूका",
                "हरूकी",
                "हरूले",
                "हरूलाई",
                "हरूमा",
                "हरूबाट",
                "हरूसँग",
                "हरूसम्म",
                "हरुमा",
                "हरुले",
                "हरुको",
                "हरुबाट",
                "हरुलाई",
                "हरू",
                "हरु",
                "लगायत",
                "माथि",
                "तल",
                "लाई",
                "बाट",
                "मा",
                "को",
                "का",
                "की",
                "ले",
                "मध्ये",
                "पछि",
                "अघि",
                "बीच",
                "द्वारा",
                "सँग",
                "प्रति",
                "तर्फ",
                "नजिक",
                "देखि",
                "सहित",
                "समेत",
                "सम्बन्धी",
                "गत",
                "विपरीत",
                "अनुसार",
                "भन्दा",
                "भन्ने",
                "नै",
                "पनि",
                "सँगै",
                "देख",
                "देखी",
                "सक्छ",
                "सक्दै",
                "सक्न",
                "नु",
                "ने",
                "ना",
                "यो",
                "ऊ",
                "हो",
                "थियो",
                "थिए",
                "थिएन",
                "छ",
                "छन्",
                "छौँ",
                "छु",
                "छैन",
                "हुन्छ",
                "हुन्न",
                "हुन्छन्",
                "हुन्",
                "हुने",
                "हुँदै",
                "गर्",
                "भन्",
                "जान्",
                "आउन्",
                "इन्",
                "उन्",
            ]
        self.suffixes.sort(key=len, reverse=True)

    def stem(self, word):
        """
        Stem a single Nepali word.

        Args:
            word (str): A single Nepali word.

        Returns:
            str: The stemmed (root) form of the word.
        """
        if not word or len(word) <= self.min_residue:
            return word

        for suffix in self.suffixes:
            if word.endswith(suffix) and len(word) - len(suffix) >= self.min_residue:
                stemmed = word[: -len(suffix)]
                if stemmed:
                    return stemmed
        return word

    def stem_text(self, text):
        """
        Stem all words in a Nepali text.

        Args:
            text (str): Input Nepali text.

        Returns:
            str: Text with all words stemmed.
        """
        if not text:
            return text
        words = text.split()
        return " ".join(self.stem(w) for w in words)

    def stem_words(self, words):
        """
        Stem a list of Nepali words.

        Args:
            words (list): List of Nepali words.

        Returns:
            list: List of stemmed words.
        """
        if not words:
            return []
        return [self.stem(w) for w in words]


def stem(word):
    """
    Convenience function to stem a single word.

    Args:
        word (str): A single Nepali word.

    Returns:
        str: The stemmed form.
    """
    return NepaliStemmer().stem(word)


def stem_text(text):
    """
    Convenience function to stem all words in text.

    Args:
        text (str): Input Nepali text.

    Returns:
        str: Stemmed text.
    """
    return NepaliStemmer().stem_text(text)


class SnowballStemmer:
    """
    Wrapper around the Snowball stemmer for Nepali.

    Uses the snowballstemmer library which provides a well-tested
    rule-based stemmer for Nepali. This is an alternative to the
    built-in NepaliStemmer that may provide better accuracy for
    some use cases.

    Args:
        ignore_stopwords (bool): Whether to ignore stopwords. Default False.

    Usage:
        sb = SnowballStemmer()
        sb.stem("नेपालमा")  # -> "नेपाल"
    """

    def __init__(self, ignore_stopwords=False):
        try:
            import snowballstemmer

            self._stemmer = snowballstemmer.stemmer("nepali")
            self._available = True
        except ImportError:
            self._available = False

    @property
    def available(self):
        return self._available

    def stem(self, word):
        """
        Stem a single word using Snowball algorithm.

        Args:
            word (str): A single Nepali word.

        Returns:
            str: The stemmed form.
        """
        if not self._available:
            raise ImportError(
                "snowballstemmer is required. Install with: pip install snowballstemmer"
            )
        if not word:
            return word
        result = self._stemmer.stemWord(word)
        return result

    def stem_words(self, words):
        """
        Stem a list of words using Snowball algorithm.

        Args:
            words (list): List of Nepali words.

        Returns:
            list: List of stemmed words.
        """
        if not self._available:
            raise ImportError(
                "snowballstemmer is required. Install with: pip install snowballstemmer"
            )
        if not words:
            return []
        return self._stemmer.stemWords(words)

    def stem_text(self, text):
        """
        Stem all words in a text using Snowball algorithm.

        Args:
            text (str): Input Nepali text.

        Returns:
            str: Text with all words stemmed.
        """
        if not self._available:
            raise ImportError(
                "snowballstemmer is required. Install with: pip install snowballstemmer"
            )
        if not text:
            return text
        words = text.split()
        return " ".join(self._stemmer.stemWords(words))


def snowball_stem(word):
    """
    Convenience function to stem a word using Snowball algorithm.

    Args:
        word (str): A single Nepali word.

    Returns:
        str: The stemmed form.
    """
    return SnowballStemmer().stem(word)
