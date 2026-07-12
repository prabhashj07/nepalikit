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
        'a': '\u0905', 'aa': '\u0906', 'i': '\u0907', 'ee': '\u0908',
        'u': '\u0909', 'oo': '\u090A', 'e': '\u090F', 'ai': '\u0910',
        'o': '\u0913', 'au': '\u0914',

        'ksha': '\u0915\u094D\u0937', 'tra': '\u0924\u094D\u0930', 'gya': '\u091C\u094D\u091E',

        'kh': '\u0916\u094D', 'gh': '\u0918\u094D', 'ng': '\u0919\u094D',
        'chh': '\u091B\u094D', 'jh': '\u091D\u094D', 'ny': '\u091E\u094D',
        'th': '\u0925\u094D', 'dh': '\u0927\u094D',
        'ph': '\u092B\u094D', 'bh': '\u092D\u094D',
        'sh': '\u0936\u094D', 'shh': '\u0937\u094D',

        'k': '\u0915\u094D', 'g': '\u0917\u094D',
        'ch': '\u091A\u094D', 'j': '\u091C\u094D',
        't': '\u0924\u094D', 'd': '\u0926\u094D', 'n': '\u0928\u094D',
        'p': '\u092A\u094D', 'b': '\u092C\u094D', 'm': '\u092E\u094D',
        'y': '\u092F\u094D', 'r': '\u0930\u094D', 'l': '\u0932\u094D',
        'v': '\u0935\u094D', 'w': '\u0935\u094D',
        's': '\u0938\u094D', 'h': '\u0939\u094D',
    }

    DEVANAGARI_TO_ROMAN = {
        '\u0905': 'a', '\u0906': 'aa', '\u0907': 'i', '\u0908': 'ee',
        '\u0909': 'u', '\u090A': 'oo', '\u090F': 'e', '\u0910': 'ai',
        '\u0913': 'o', '\u0914': 'au',
        '\u090B': 'ri', '\u0972': 'e', '\u0911': 'o',

        '\u0915': 'ka', '\u0916': 'kha', '\u0917': 'ga', '\u0918': 'gha', '\u0919': 'nga',
        '\u091A': 'cha', '\u091B': 'chha', '\u091C': 'ja', '\u091D': 'jha', '\u091E': 'nya',
        '\u091F': '\u1E6Ba', '\u0920': '\u1E6Bha', '\u0921': '\u1E0Da', '\u0922': '\u1E0Dha', '\u0923': '\u1E47a',
        '\u0924': 'ta', '\u0925': 'tha', '\u0926': 'da', '\u0927': 'dha', '\u0928': 'na',
        '\u092A': 'pa', '\u092B': 'pha', '\u092C': 'ba', '\u092D': 'bha', '\u092E': 'ma',
        '\u092F': 'ya', '\u0930': 'ra', '\u0932': 'la', '\u0935': 'va', '\u0936': 'sha',
        '\u0937': 'shha', '\u0938': 'sa', '\u0939': 'ha',

        '\u093E': 'aa', '\u093F': 'i', '\u0940': 'ee', '\u0941': 'u', '\u0942': 'oo',
        '\u0947': 'e', '\u0948': 'ai', '\u094B': 'o', '\u094C': 'au',
        '\u0943': 'ri', '\u0949': 'o', '\u0946': 'e',

        '\u0902': 'n', '\u0903': 'h', '\u0901': 'n',

        '\u094D': '',
        '\u093C': '',
        '\u0965': '', '\u0964': '',
    }

    VOWEL_MARKS = {
        'a': '\u093E',
        'i': '\u093F',
        'ee': '\u0940',
        'u': '\u0941',
        'oo': '\u0942',
        'e': '\u0947',
        'ai': '\u0948',
        'o': '\u094B',
        'au': '\u094C',
        'ri': '\u0943',
    }

    DEVANAGARI_DIGITS = '\u0966\u0967\u0968\u0969\u096A\u096B\u096C\u096D\u096E\u096F'

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
                chunk = text[i:i + length]
                if chunk in self.ROMAN_TO_DEVANAGARI:
                    dev = self.ROMAN_TO_DEVANAGARI[chunk]
                    if dev.endswith('\u094D') and i + length < len(text):
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
                if ch in '0123456789':
                    result.append(self.DEVANAGARI_DIGITS[int(ch)])
                elif ch in ' \t\n':
                    result.append(ch)
                else:
                    result.append(ch)
                i += 1

        return "".join(result)

    def devanagari_to_roman(self, text):
        """
        Convert Devanagari Nepali to Romanized text.

        Uses diacritics for retroflex: \u1E6Ba, \u1E0Da, \u1E47a.

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
            elif '\u0966' <= ch <= '\u096F':
                result.append(str(ord(ch) - 0x966))
            elif ch in ' \t\n':
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
