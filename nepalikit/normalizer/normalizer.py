"""
normalizer.py

Text normalization for Nepali language.
Handles Unicode normalization, ZWNJ/ZWJ stripping, and script detection.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import unicodedata
import re


class NepaliNormalizer:
    """
    Normalize Nepali text for consistent processing.

    Features:
    - Unicode NFC/NFKC normalization
    - Zero-width non-joiner (ZWNJ, U+200C) and zero-width joiner (ZWJ, U+200D) stripping
    - Script detection (Devanagari, Latin, mixed)
    - Common Unicode cleanup
    """

    DEVANAGARI_RANGE = re.compile(r"[\u0900-\u097F]")
    LATIN_RANGE = re.compile(r"[A-Za-z]")

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
