"""
number_extractor.py

Extract and convert Nepali numeric expressions to integers.
Handles Devanagari digits, Nepali number words, decimal scales,
and comma-separated Indian-style formatting.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re


class NepaliNumberExtractor:
    """
    Extract and convert Nepali numeric expressions to integers.

    Handles:
    - Devanagari digits (०-९)
    - Nepali number words (एक through महाशंख)
    - Multipliers (सय, हजार, लाख, करोड, अर्ब, खर्ब, etc.)
    - Compound expressions (२ लाख ५ हजार)
    - Decimal scales (२.५ लाख = 250000)
    - Indian-style comma-separated digits (१,२३,४५६)
    """

    DEVANAGARI_DIGITS = {
        "०": 0,
        "१": 1,
        "२": 2,
        "३": 3,
        "४": 4,
        "५": 5,
        "६": 6,
        "७": 7,
        "८": 8,
        "९": 9,
    }

    NUMBER_WORDS = {
        "शून्य": 0,
        "एक": 1,
        "दुई": 2,
        "तीन": 3,
        "चार": 4,
        "पाँच": 5,
        "पाच": 5,
        "छ": 6,
        "सात": 7,
        "आठ": 8,
        "नौ": 9,
        "दश": 10,
        "दस": 10,
        "एघार": 11,
        "बाह्र": 12,
        "तेह्र": 13,
        "चौध": 14,
        "पन्ध्र": 15,
        "सोह्र": 16,
        "सत्र": 17,
        "अठार": 18,
        "उन्नाइस": 19,
        "बीस": 20,
        "तीस": 30,
        "चालीस": 40,
        "पचास": 50,
        "साठी": 60,
        "सत्तरी": 70,
        "असी": 80,
        "नब्बे": 90,
        "एक्काइस": 21,
        "बाइस": 22,
        "तेइस": 23,
        "चौबीस": 24,
        "पच्चीस": 25,
        "छब्बीस": 26,
        "सत्ताइस": 27,
        "अठ्ठाइस": 28,
        "उनन्तिस": 29,
        "एकतीस": 31,
        "बत्तीस": 32,
        "तेत्तीस": 33,
        "चौँतीस": 34,
        "पैँतीस": 35,
        "छत्तीस": 36,
        "सैँतीस": 37,
        "अठतीस": 38,
        "उनन्चालीस": 39,
        "एकचालीस": 41,
        "बयालीस": 42,
        "त्रिचालीस": 43,
        "चवालीस": 44,
        "पैँतालीस": 45,
        "छयालीस": 46,
        "सतचालीस": 47,
        "अठचालीस": 48,
        "उनन्चास": 49,
        "एकाउन्न": 51,
        "बाउन्न": 52,
        "त्रिपन्न": 53,
        "चवन्न": 54,
        "पचपन्न": 55,
        "छपन्न": 56,
        "सन्ताउन्न": 57,
        "अन्ठाउन्न": 58,
        "उनन्साठी": 59,
        "एकसट्ठी": 61,
        "बैसट्ठी": 62,
        "त्रिसट्ठी": 63,
        "चौंसट्ठी": 64,
        "पैंसट्ठी": 65,
        "छैसट्ठी": 66,
        "सतसट्ठी": 67,
        "अठसट्ठी": 68,
        "उनन्सत्तरी": 69,
        "एकहत्तर": 71,
        "बहत्तर": 72,
        "त्रिहत्तर": 73,
        "चौहत्तर": 74,
        "पचहत्तर": 75,
        "छहत्तर": 76,
        "सतहत्तर": 77,
        "अठहत्तर": 78,
        "उनासी": 79,
        "एकासी": 81,
        "बयासी": 82,
        "त्रियासी": 83,
        "चौरासी": 84,
        "पचासी": 85,
        "छयासी": 86,
        "सतासी": 87,
        "अठासी": 88,
        "उनान्नब्बे": 89,
        "एकानब्बे": 91,
        "बयानब्बे": 92,
        "त्रियानब्बे": 93,
        "चौरानब्बे": 94,
        "पन्चानब्बे": 95,
        "छयानब्बे": 96,
        "सन्तानब्बे": 97,
        "अन्ठानब्बे": 98,
        "उनान्सय": 99,
    }

    MULTIPLIERS = {
        "सय": 100,
        "हजार": 1000,
        "हजारौं": 1000,
        "लाख": 100000,
        "लाखौं": 100000,
        "करोड": 10000000,
        "करोडौं": 10000000,
        "अर्ब": 1000000000,
        "अर्बौं": 1000000000,
        "खर्ब": 100000000000,
    }

    def extract(self, text):
        """
        Find all number expressions in text.

        Args:
            text (str): Input text containing Nepali numbers.

        Returns:
            list: List of (expression, value) tuples.
        """
        if not text or not text.strip():
            return []

        results = []

        devanagari_num_pattern = r"[०-९]+"
        for match in re.finditer(devanagari_num_pattern, text):
            expr = match.group()
            value = self._devanagari_to_int(expr)
            if value is not None:
                results.append((expr, value))

        multipliers_re = "|".join(
            re.escape(w) for w in sorted(self.MULTIPLIERS.keys(), key=len, reverse=True)
        )
        word_values_re = "|".join(
            re.escape(w)
            for w in sorted(self.NUMBER_WORDS.keys(), key=len, reverse=True)
        )
        compound_pattern = (
            r"(?:[०-९]+(?:\.[०-९]+)?"
            r"|" + word_values_re + r")"
            r"\s*"
            r"(?:" + multipliers_re + r")"
            r"(?:\s+(?:[०-९]+(?:\.[०-९]+)?"
            r"|" + word_values_re + r")"
            r"\s*(?:" + multipliers_re + r")?)*"
        )
        for match in re.finditer(compound_pattern, text):
            expr = match.group().strip()
            if expr not in [r[0] for r in results]:
                value = self.convert(expr)
                if value is not None:
                    results.append((expr, value))

        standalone_words = sorted(self.NUMBER_WORDS.keys(), key=len, reverse=True)
        non_standalone = set(self.MULTIPLIERS.keys()) | {
            "छ",  # ambiguous: number 6 or auxiliary verb
        }
        standalone_re = "|".join(
            re.escape(w) for w in standalone_words if w not in non_standalone
        )
        if standalone_re:
            for match in re.finditer(r"\b(" + standalone_re + r")\b", text):
                expr = match.group()
                if expr not in [r[0] for r in results]:
                    value = self.NUMBER_WORDS.get(expr)
                    if value is not None and value < 100:
                        results.append((expr, value))

        return results

    def convert(self, text):
        """
        Convert a Nepali number expression to an integer.

        Args:
            text (str): A Nepali number expression (e.g., '२ लाख ५ हजार').

        Returns:
            int or None: The integer value, or None if conversion fails.
        """
        if not text or not text.strip():
            return None

        text = text.strip()
        text = self._normalize_digits(text)
        text = self._strip_commas(text)

        devanagari_digits = re.fullmatch(r"[०-९]+", text)
        if devanagari_digits:
            return self._devanagari_to_int(text)

        if re.fullmatch(r"\d+", text):
            return int(text)

        if re.fullmatch(r"\d+\.\d+", text):
            return round(float(text))

        return self._word_to_int(text)

    def _normalize_digits(self, text):
        """Convert Devanagari digits to ASCII."""
        for nepali, ascii_d in self.DEVANAGARI_DIGITS.items():
            text = text.replace(nepali, str(ascii_d))
        return text

    def _strip_commas(self, text):
        """Remove commas only between digits (Indian-style grouping)."""
        return re.sub(r"(?<=\d),(?=\d)", "", text)

    def _devanagari_to_int(self, text):
        """Convert a Devanagari digit string to integer."""
        result = 0
        for ch in text:
            digit = self.DEVANAGARI_DIGITS.get(ch)
            if digit is None:
                return None
            result = result * 10 + digit
        return result

    def _word_to_int(self, text):
        """Convert a Nepali number word expression to integer."""
        tokens = text.split()
        total = 0
        current = 0

        for token in tokens:
            if token in self.MULTIPLIERS:
                if current == 0:
                    current = 1
                total += current * self.MULTIPLIERS[token]
                current = 0
            elif token in self.NUMBER_WORDS:
                val = self.NUMBER_WORDS[token]
                if val >= 100 and token not in self.MULTIPLIERS:
                    if current == 0:
                        current = 1
                    total += current * val
                    current = 0
                else:
                    current += val
            else:
                try:
                    if "." in token:
                        current += float(token)
                    else:
                        current += int(token)
                except (ValueError, TypeError):
                    return None

        total += current
        return int(total)


def extract_numbers(text):
    """
    Convenience function to extract all number expressions from text.

    Args:
        text (str): Input text.

    Returns:
        list: List of (expression, value) tuples.
    """
    return NepaliNumberExtractor().extract(text)


def convert_number(text):
    """
    Convenience function to convert a single Nepali number expression.

    Args:
        text (str): A Nepali number expression.

    Returns:
        int or None: The integer value.
    """
    return NepaliNumberExtractor().convert(text)
