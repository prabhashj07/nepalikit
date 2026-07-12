"""
spell_checker.py

Dictionary-based spell checking and correction for Nepali text.
Uses edit distance for generating suggestions.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
from importlib import resources


class NepaliSpellChecker:
    """
    Spell checker for Nepali text.

    Uses a dictionary of known words and Levenshtein edit distance
    to suggest corrections for misspelled words.
    """

    def __init__(self, dictionary_path=None):
        """
        Initialize the spell checker.

        Args:
            dictionary_path (str, optional): Path to a custom dictionary file
                (one word per line). If None, loads the bundled dictionary.
        """
        self.known_words = set()
        if dictionary_path:
            self._load_dictionary(dictionary_path)
        else:
            pkg = resources.files("nepalikit")
            default_path = str(pkg.joinpath("data", "spelling_dict.txt"))
            self._load_dictionary(default_path)

    def _load_dictionary(self, path):
        """Load words from a dictionary file."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip()
                    if word:
                        self.known_words.add(word)
        except FileNotFoundError:
            pass

    def check(self, word):
        """
        Check if a word is spelled correctly.

        Args:
            word (str): A single word.

        Returns:
            bool: True if the word is in the dictionary.
        """
        return word in self.known_words

    def suggest(self, word, max_distance=2, max_suggestions=5):
        """
        Suggest corrections for a misspelled word.

        Args:
            word (str): The misspelled word.
            max_distance (int): Maximum edit distance to consider.
            max_suggestions (int): Maximum number of suggestions to return.

        Returns:
            list: List of suggested corrections, sorted by edit distance.
        """
        if not word:
            return []

        if word in self.known_words:
            return [word]

        candidates = []
        for known in self.known_words:
            dist = self._edit_distance(word, known, max_distance)
            if dist <= max_distance:
                candidates.append((known, dist))

        candidates.sort(key=lambda x: (x[1], len(x[0])))
        return [c[0] for c in candidates[:max_suggestions]]

    def correct(self, text, max_distance=1):
        """
        Correct misspellings in text.

        Only corrects words where exactly one suggestion is found
        within the edit distance to avoid false positives.

        Args:
            text (str): Input text.
            max_distance (int): Maximum edit distance for corrections.

        Returns:
            str: Corrected text.
        """
        words = text.split()
        corrected = []
        for word in words:
            clean = re.sub(r'[।,;?!—\-]', '', word)
            if clean and not self.check(clean):
                suggestions = self.suggest(clean, max_distance=max_distance, max_suggestions=2)
                if len(suggestions) == 1:
                    corrected.append(word.replace(clean, suggestions[0]))
                else:
                    corrected.append(word)
            else:
                corrected.append(word)
        return " ".join(corrected)

    def add_word(self, word):
        """
        Add a word to the dictionary.

        Args:
            word (str): Word to add.
        """
        self.known_words.add(word)

    def _edit_distance(self, s1, s2, max_dist):
        """
        Compute Levenshtein edit distance between two strings.
        Uses early termination when distance exceeds max_dist.
        """
        if abs(len(s1) - len(s2)) > max_dist:
            return max_dist + 1

        m, n = len(s1), len(s2)
        prev = list(range(n + 1))
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            curr[0] = i
            min_val = curr[0]
            for j in range(1, n + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                curr[j] = min(
                    prev[j] + 1,
                    curr[j - 1] + 1,
                    prev[j - 1] + cost
                )
                min_val = min(min_val, curr[j])
            if min_val > max_dist:
                return max_dist + 1
            prev, curr = curr, prev

        return prev[n]


def check_spelling(word, dictionary_path=None):
    """
    Convenience function to check if a word is spelled correctly.

    Args:
        word (str): The word to check.
        dictionary_path (str, optional): Custom dictionary path.

    Returns:
        bool: True if correct.
    """
    checker = NepaliSpellChecker(dictionary_path)
    return checker.check(word)


def suggest_corrections(word, max_distance=2, dictionary_path=None):
    """
    Convenience function to get spelling suggestions.

    Args:
        word (str): Misspelled word.
        max_distance (int): Max edit distance.
        dictionary_path (str, optional): Custom dictionary path.

    Returns:
        list: Suggested corrections.
    """
    checker = NepaliSpellChecker(dictionary_path)
    return checker.suggest(word, max_distance)
