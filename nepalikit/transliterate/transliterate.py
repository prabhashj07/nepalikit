"""
transliterate.py

Transliteration between Romanized and Devanagari Nepali.
Provides character-level mapping for both directions.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""


class NepaliTransliterator:
    """
    Transliterate between Roman and Devanagari scripts for Nepali.

    Supports:
    - Roman to Devanagari (e.g., 'nepal' → 'नेपाल')
    - Devanagari to Roman (e.g., 'नेपाल' → 'nepal')

    Scheme:
    - Consonants followed by a vowel compose correctly (e.g., 'ka' → 'क',
      'ki' → 'कि', 'ne' → 'ने').
    - Dental/retroflex distinction is not preserved in Roman → Devanagari
      (dental is used as default for t/d/n).
    """

    ROMAN_TO_DEVANAGARI = {
        "a": "\u0905",
        "aa": "\u0906",
        "i": "\u0907",
        "ee": "\u0908",
        "u": "\u0909",
        "oo": "\u090a",
        "e": "\u090f",
        "ai": "\u0910",
        "o": "\u0913",
        "au": "\u0914",
        "ksha": "\u0915\u094d\u0937",
        "tra": "\u0924\u094d\u0930",
        "gya": "\u091c\u094d\u091e",
        "kh": "\u0916\u094d",
        "gh": "\u0918\u094d",
        "ng": "\u0919\u094d",
        "chh": "\u091b\u094d",
        "jh": "\u091d\u094d",
        "ny": "\u091e\u094d",
        "th": "\u0925\u094d",
        "dh": "\u0927\u094d",
        "ph": "\u092b\u094d",
        "bh": "\u092d\u094d",
        "sh": "\u0936\u094d",
        "shh": "\u0937\u094d",
        "k": "\u0915\u094d",
        "g": "\u0917\u094d",
        "ch": "\u091a\u094d",
        "j": "\u091c\u094d",
        "t": "\u0924\u094d",
        "d": "\u0926\u094d",
        "n": "\u0928\u094d",
        "p": "\u092a\u094d",
        "b": "\u092c\u094d",
        "m": "\u092e\u094d",
        "y": "\u092f\u094d",
        "r": "\u0930\u094d",
        "l": "\u0932\u094d",
        "v": "\u0935\u094d",
        "w": "\u0935\u094d",
        "s": "\u0938\u094d",
        "h": "\u0939\u094d",
    }

    DEVANAGARI_TO_ROMAN = {
        "\u0905": "a",
        "\u0906": "aa",
        "\u0907": "i",
        "\u0908": "ee",
        "\u0909": "u",
        "\u090a": "oo",
        "\u090f": "e",
        "\u0910": "ai",
        "\u0913": "o",
        "\u0914": "au",
        "\u090b": "ri",
        "\u0972": "e",
        "\u0911": "o",
        "\u0915": "ka",
        "\u0916": "kha",
        "\u0917": "ga",
        "\u0918": "gha",
        "\u0919": "nga",
        "\u091a": "cha",
        "\u091b": "chha",
        "\u091c": "ja",
        "\u091d": "jha",
        "\u091e": "nya",
        "\u091f": "\u1e6ba",
        "\u0920": "\u1e6bha",
        "\u0921": "\u1e0da",
        "\u0922": "\u1e0dha",
        "\u0923": "\u1e47a",
        "\u0924": "ta",
        "\u0925": "tha",
        "\u0926": "da",
        "\u0927": "dha",
        "\u0928": "na",
        "\u092a": "pa",
        "\u092b": "pha",
        "\u092c": "ba",
        "\u092d": "bha",
        "\u092e": "ma",
        "\u092f": "ya",
        "\u0930": "ra",
        "\u0932": "la",
        "\u0935": "va",
        "\u0936": "sha",
        "\u0937": "shha",
        "\u0938": "sa",
        "\u0939": "ha",
        "\u093e": "aa",
        "\u093f": "i",
        "\u0940": "ee",
        "\u0941": "u",
        "\u0942": "oo",
        "\u0947": "e",
        "\u0948": "ai",
        "\u094b": "o",
        "\u094c": "au",
        "\u0943": "ri",
        "\u0949": "o",
        "\u0946": "e",
        "\u0902": "n",
        "\u0903": "h",
        "\u0901": "n",
        "\u094d": "",
        "\u093c": "",
        "\u0965": "",
        "\u0964": "",
    }

    VOWEL_MARKS = {
        "a": "\u093e",
        "i": "\u093f",
        "ee": "\u0940",
        "u": "\u0941",
        "oo": "\u0942",
        "e": "\u0947",
        "ai": "\u0948",
        "o": "\u094b",
        "au": "\u094c",
        "ri": "\u0943",
    }

    DEVANAGARI_DIGITS = "\u0966\u0967\u0968\u0969\u096a\u096b\u096c\u096d\u096e\u096f"

    def roman_to_devanagari(self, text):
        """
        Convert Romanized Nepali to Devanagari.

        Args:
            text (str): Romanized Nepali text.

        Returns:
            str: Devanagari text.
        """
        if not text:
            return text

        text = text.lower()
        result = []
        i = 0

        while i < len(text):
            matched = False
            for length in [4, 3, 2, 1]:
                chunk = text[i : i + length]
                if chunk in self.ROMAN_TO_DEVANAGARI:
                    dev = self.ROMAN_TO_DEVANAGARI[chunk]
                    if dev.endswith("\u094d") and i + length < len(text):
                        next_char = text[i + length]
                        if next_char in self.VOWEL_MARKS:
                            base = dev[:-1]
                            matra = self.VOWEL_MARKS[next_char]
                            result.append(base + matra)
                            i += length + 1
                            matched = True
                            break
                    result.append(dev)
                    i += length
                    matched = True
                    break
            if not matched:
                ch = text[i]
                if ch in "0123456789":
                    result.append(self.DEVANAGARI_DIGITS[int(ch)])
                elif ch in " \t\n":
                    result.append(ch)
                else:
                    result.append(ch)
                i += 1

        return "".join(result)

    def devanagari_to_roman(self, text):
        """
        Convert Devanagari Nepali to Romanized text.

        Uses diacritics for retroflex: \u1e6ba, \u1e0da, \u1e47a.

        Args:
            text (str): Devanagari text.

        Returns:
            str: Romanized text.
        """
        if not text:
            return text

        result = []
        i = 0

        while i < len(text):
            ch = text[i]

            if i + 1 < len(text):
                bigram = ch + text[i + 1]
                if bigram in self.DEVANAGARI_TO_ROMAN:
                    result.append(self.DEVANAGARI_TO_ROMAN[bigram])
                    i += 2
                    continue

            if ch in self.DEVANAGARI_TO_ROMAN:
                result.append(self.DEVANAGARI_TO_ROMAN[ch])
            elif "\u0966" <= ch <= "\u096f":
                result.append(str(ord(ch) - 0x966))
            elif ch in " \t\n":
                result.append(ch)
            else:
                result.append(ch)
            i += 1

        return "".join(result)


def roman_to_devanagari(text):
    """
    Convenience function to convert Roman to Devanagari.

    Args:
        text (str): Romanized text.

    Returns:
        str: Devanagari text.
    """
    return NepaliTransliterator().roman_to_devanagari(text)


def devanagari_to_roman(text):
    """
    Convenience function to convert Devanagari to Roman.

    Args:
        text (str): Devanagari text.

    Returns:
        str: Romanized text.
    """
    return NepaliTransliterator().devanagari_to_roman(text)
