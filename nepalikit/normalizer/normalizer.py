"""
normalizer.py

Text normalization for Nepali language.
Handles Unicode normalization, ZWNJ/ZWJ stripping, and script detection.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
import string
import unicodedata


class NepaliNormalizer:
    """
    Normalize Nepali text for consistent processing.

    Features:
    - Unicode NFC/NFKC normalization
    - Zero-width non-joiner (ZWNJ, U+200C) and zero-width joiner (ZWJ, U+200D) stripping
    - Script detection (Devanagari, Latin, mixed)
    - Common Unicode cleanup
    """

    DEVANAGARI_RANGE = re.compile(r"[\u0900-\u097F\uA8E0-\uA8FF]")
    LATIN_RANGE = re.compile(r"[A-Za-z\u00C0-\u024F]")
    DEVANAGARI_DIGITS_RE = re.compile(r"[\u0966-\u096F]")

    def normalize(self, text, form="NFC"):
        """
        Apply full normalization pipeline to Nepali text.

        Args:
            text (str): Input text.
            form (str): Unicode normalization form ('NFC' or 'NFKC'). Default 'NFC'.

        Returns:
            str: Normalized text.
        """
        if not text:
            return text
        text = unicodedata.normalize(form, text)
        text = self.strip_zwnj(text)
        text = self.strip_control_chars(text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def detect_script(self, text):
        """
        Detect the script of the input text.

        Args:
            text (str): Input text.

        Returns:
            str: 'devanagari', 'latin', 'mixed', or 'other'.
        """
        if not text:
            return "other"

        dev_count = len(self.DEVANAGARI_RANGE.findall(text))
        lat_count = len(self.LATIN_RANGE.findall(text))
        total = dev_count + lat_count

        if total == 0:
            return "other"

        dev_ratio = dev_count / total
        lat_ratio = lat_count / total

        if dev_ratio > 0.8:
            return "devanagari"
        elif lat_ratio > 0.8:
            return "latin"
        elif dev_ratio > 0.1 and lat_ratio > 0.1:
            return "mixed"
        elif dev_ratio > lat_ratio:
            return "devanagari"
        elif lat_ratio > dev_ratio:
            return "latin"
        return "other"

    def is_devanagari(self, text):
        """
        Check if every non-whitespace, non-punctuation character is Devanagari.

        Args:
            text (str): Input text.

        Returns:
            bool: True if the text is purely Devanagari.
        """
        if not text:
            return False
        has_devanagari = False
        for ch in text:
            if ch.isspace() or ch in string.punctuation:
                continue
            if self.DEVANAGARI_RANGE.match(ch):
                has_devanagari = True
            else:
                return False
        return has_devanagari

    def contains_devanagari(self, text):
        """
        Check if text contains at least one Devanagari character.

        Args:
            text (str): Input text.

        Returns:
            bool: True if at least one Devanagari character found.
        """
        if not text:
            return False
        return bool(self.DEVANAGARI_RANGE.search(text))

    def contains_latin(self, text):
        """
        Check if text contains at least one Latin character.

        Args:
            text (str): Input text.

        Returns:
            bool: True if at least one Latin character found.
        """
        if not text:
            return False
        return bool(self.LATIN_RANGE.search(text))

    def mixed_script_ratio(self, text):
        """
        Compute the Devanagari fraction over Devanagari + Latin characters.

        Args:
            text (str): Input text.

        Returns:
            float: Ratio of Devanagari chars to total Devanagari + Latin chars.
        """
        if not text:
            return 0.0
        dev_count = len(self.DEVANAGARI_RANGE.findall(text))
        lat_count = len(self.LATIN_RANGE.findall(text))
        total = dev_count + lat_count
        if total == 0:
            return 0.0
        return dev_count / total

    def strip_zwnj(self, text):
        """
        Remove zero-width joiners and non-joiners.

        Args:
            text (str): Input text.

        Returns:
            str: Text without ZWNJ (U+200C) and ZWJ (U+200D).
        """
        if not text:
            return text
        return text.replace("\u200c", "").replace("\u200d", "")

    def strip_control_chars(self, text):
        """
        Remove Unicode control and format characters (except whitespace).

        Args:
            text (str): Input text.

        Returns:
            str: Cleaned text.
        """
        if not text:
            return text
        cleaned = []
        for ch in text:
            cat = unicodedata.category(ch)
            if cat.startswith("C") and cat != "Cc":
                continue
            cleaned.append(ch)
        return "".join(cleaned)

    def normalize_unicode(self, text, form="NFC"):
        """
        Apply Unicode normalization only.

        Args:
            text (str): Input text.
            form (str): Normalization form.

        Returns:
            str: Unicode-normalized text.
        """
        return unicodedata.normalize(form, text)


def normalize(text, form="NFC"):
    """
    Convenience function to normalize Nepali text.

    Args:
        text (str): Input text.
        form (str): Unicode normalization form.

    Returns:
        str: Normalized text.
    """
    return NepaliNormalizer().normalize(text, form)


def detect_script(text):
    """
    Convenience function to detect script of text.

    Args:
        text (str): Input text.

    Returns:
        str: 'devanagari', 'latin', 'mixed', or 'other'.
    """
    return NepaliNormalizer().detect_script(text)


def is_devanagari(text):
    """
    Check if text is purely Devanagari (ignoring whitespace/punctuation).

    Args:
        text (str): Input text.

    Returns:
        bool: True if purely Devanagari.
    """
    return NepaliNormalizer().is_devanagari(text)


def contains_devanagari(text):
    """
    Check if text contains at least one Devanagari character.

    Args:
        text (str): Input text.

    Returns:
        bool: True if Devanagari found.
    """
    return NepaliNormalizer().contains_devanagari(text)


def contains_latin(text):
    """
    Check if text contains at least one Latin character.

    Args:
        text (str): Input text.

    Returns:
        bool: True if Latin found.
    """
    return NepaliNormalizer().contains_latin(text)


def mixed_script_ratio(text):
    """
    Compute Devanagari fraction over Devanagari + Latin characters.

    Args:
        text (str): Input text.

    Returns:
        float: Ratio (0.0 to 1.0).
    """
    return NepaliNormalizer().mixed_script_ratio(text)
