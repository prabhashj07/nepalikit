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
    """

    def __init__(self):
        pkg = resources.files("nepalikit")
        rules_path = str(pkg.joinpath("data", "stemmer_rules.json"))
        try:
            with open(rules_path, "r", encoding="utf-8") as f:
                rules = json.load(f)
            self.suffixes = rules.get("suffixes", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.suffixes = [
                "हरूमा",
                "हरूले",
                "हरूको",
                "हरूबाट",
                "हरूलाई",
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
                "एक",
                "दुई",
                "तीन",
                "चार",
                "पहिलो",
                "दोस्रो",
                "तेस्रो",
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
        if not word or len(word) <= 2:
            return word

        for suffix in self.suffixes:
            if word.endswith(suffix) and len(word) - len(suffix) >= 2:
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
