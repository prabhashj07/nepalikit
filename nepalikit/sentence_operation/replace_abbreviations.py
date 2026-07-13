"""
replace_abbreviations.py

Abbreviation replacement for Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re


class AbbreviationReplacer:
    """Replace abbreviations in Nepali text with their expanded forms.

    Args:
        abbreviations (dict, optional): Mapping of abbreviation to full form.
            Defaults to empty dict.

    Examples:
        >>> replacer = AbbreviationReplacer({"उ.मा.वि.": "उच्च माध्यमिक विद्यालय"})
        >>> replacer.replace_abbreviations("उ.मा.वि. मा पढ्छु")
        'उच्च माध्यमिक विद्यालय मा पढ्छु'
    """

    def __init__(self, abbreviations=None):
        self.abbreviations = abbreviations or {}
        self.pattern = self._generate_pattern()

    def _generate_pattern(self):
        abbr_patterns = [re.escape(abbr) for abbr in self.abbreviations]
        return "|".join(abbr_patterns) if abbr_patterns else None

    def _replace_match(self, match):
        matched_text = match.group(0)
        for abbr, full_form in self.abbreviations.items():
            if matched_text.lower() == abbr.lower():
                return full_form
        return matched_text

    def replace_abbreviations(self, text: str) -> str:
        """Replace all abbreviations in text with their expanded forms.

        Args:
            text (str): Input text containing abbreviations.

        Returns:
            str: Text with abbreviations replaced.
        """
        if not self.pattern:
            return text
        return re.sub(
            self.pattern, self._replace_match, text, flags=re.UNICODE | re.IGNORECASE
        )
