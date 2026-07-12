"""
Spell checker module for Nepali language.

Provides dictionary-based spell checking with edit distance suggestions.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.spell_checker.spell_checker import NepaliSpellChecker, check_spelling, suggest_corrections

__all__ = [
    'NepaliSpellChecker',
    'check_spelling',
    'suggest_corrections',
]
