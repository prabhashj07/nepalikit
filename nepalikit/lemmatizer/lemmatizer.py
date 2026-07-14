"""
lemmatizer.py

Dictionary-based lemmatizer for Nepali words.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2026
"""

import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)


class NepaliLemmatizer:
    """Dictionary-based lemmatizer for Nepali words.

    Maps inflected forms to their canonical lemma (dictionary form).
    Falls back to rule-based suffix stripping when no dictionary entry exists.

    Attributes:
        dictionary: dict mapping inflected forms to lemmas
        min_residue: minimum stem length after suffix stripping (default 2)
    """

    def __init__(self, dictionary_path=None, min_residue=2):
        """Initialize the lemmatizer.

        Args:
            dictionary_path: Optional path to a custom JSON dictionary file.
                If None, uses the bundled lemma_dictionary.json.
            min_residue: Minimum characters required after suffix stripping.
        """
        self.min_residue = min_residue
        self.dictionary = {}
        self._suffixes = []

        if dictionary_path:
            self._load_from_path(Path(dictionary_path))
        else:
            self._load_bundled()

        # Sort suffixes longest-first for rule-based fallback
        self._suffixes.sort(key=len, reverse=True)

    def _load_bundled(self):
        """Load the bundled lemma dictionary."""
        try:
            import importlib.resources as pkg_resources

            data_dir = Path(__file__).parent.parent / "data"
            dict_path = data_dir / "lemma_dictionary.json"
            suffix_path = data_dir / "stemmer_rules.json"

            if dict_path.exists():
                with open(dict_path, encoding="utf-8") as f:
                    data = json.load(f)
                self._merge_dictionary(data)

            if suffix_path.exists():
                with open(suffix_path, encoding="utf-8") as f:
                    data = json.load(f)
                self._suffixes = data.get("suffixes", [])

        except Exception:
            logger.warning("Failed to load bundled lemma dictionary, using empty dictionary")
            self.dictionary = {}
            self._suffixes = []

    def _load_from_path(self, path):
        """Load dictionary from a custom path."""
        if not path.exists():
            raise FileNotFoundError(f"Dictionary file not found: {path}")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict) and "suffixes" in data:
            self._merge_dictionary(data)
            self._suffixes = data.get("suffixes", [])
        elif isinstance(data, dict):
            self._merge_dictionary(data)
        elif isinstance(data, list):
            for entry in data:
                if "inflected" in entry and "lemma" in entry:
                    self.dictionary[entry["inflected"]] = entry["lemma"]

    def _merge_dictionary(self, data):
        """Merge dictionary entries from loaded JSON data."""
        for category, entries in data.items():
            if category == "suffixes":
                self._suffixes = entries
                continue
            if isinstance(entries, dict):
                self.dictionary.update(entries)

    def lemmatize(self, word):
        """Find the lemma for a single word.

        First checks the dictionary for an exact match.
        If not found, falls back to rule-based suffix stripping.

        Args:
            word: A Nepali word string.

        Returns:
            The lemma (dictionary form) of the word.
        """
        if not word or not isinstance(word, str):
            return word

        word = word.strip()
        if not word:
            return word

        # Check dictionary first
        if word in self.dictionary:
            return self.dictionary[word]

        # Check with common suffixes stripped
        for suffix in self._suffixes:
            if word.endswith(suffix) and len(word) - len(suffix) >= self.min_residue:
                candidate = word[: -len(suffix)]
                if candidate in self.dictionary:
                    return self.dictionary[candidate]

        # Rule-based fallback: strip known suffixes
        for suffix in self._suffixes:
            if word.endswith(suffix) and len(word) - len(suffix) >= self.min_residue:
                return word[: -len(suffix)]

        return word

    def lemmatize_text(self, text):
        """Lemmatize all words in a text string.

        Args:
            text: A string of Nepali text.

        Returns:
            A string with each word replaced by its lemma.
        """
        if not text:
            return text

        words = text.split()
        lemmatized = [self.lemmatize(w) for w in words]
        return " ".join(lemmatized)

    def lemmatize_words(self, words):
        """Lemmatize a list of words.

        Args:
            words: A list of Nepali word strings.

        Returns:
            A list of lemma strings.
        """
        if not words:
            return words

        return [self.lemmatize(w) for w in words]


def lemmatize(word):
    """Lemmatize a single word using the default lemmatizer.

    Args:
        word: A Nepali word string.

    Returns:
        The lemma of the word.
    """
    lemmatizer = NepaliLemmatizer()
    return lemmatizer.lemmatize(word)


def lemmatize_text(text):
    """Lemmatize all words in text using the default lemmatizer.

    Args:
        text: A string of Nepali text.

    Returns:
        A string with each word replaced by its lemma.
    """
    lemmatizer = NepaliLemmatizer()
    return lemmatizer.lemmatize_text(text)
