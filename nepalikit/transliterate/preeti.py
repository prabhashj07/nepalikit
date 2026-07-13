"""
preeti.py

Convert legacy Preeti font encoded Nepali text to Unicode Devanagari.

Preeti is a popular Nepali font that maps ASCII characters to Devanagari
glyphs using a custom encoding. This module converts Preeti-encoded text
to proper Unicode Devanagari.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2026
"""

import re


class PreetiConverter:
    """
    Convert Preeti font encoded text to Unicode Devanagari.

    Preeti uses a character-by-character mapping where ASCII characters
    represent Devanagari glyphs. After mapping, regex post-processing rules
    handle conjuncts, vowel reordering, and other Devanagari rendering.

    Usage:
        converter = PreetiConverter()
        unicode_text = converter.convert("s{sf")  # -> नेपाल
    """

    CHAR_MAP = {
        "\u00f7": "/",
        "v": "\u0916",
        "r": "\u091a",
        '"': "\u0942",
        "~": "\u091e\u094d",
        "z": "\u0936",
        "\u00e7": "\u0950",
        "f": "\u093e",
        "b": "\u0926",
        "n": "\u0932",
        "j": "\u0935",
        "\u00d7": "\u00d7",
        "V": "\u0916\u094d",
        "R": "\u091a\u094d",
        "\u00df": "\u0926\u094d\u092e",
        "^": "\u0966",
        "\u00db": "!",
        "Z": "\u0936\u094d",
        "F": "\u0901",
        "B": "\u0926\u094d\u092f",
        "N": "\u0932\u094d",
        "\u00cb": "\u0919\u094d\u0917",
        "J": "\u0935\u094d",
        "6": "\u091f",
        "2": "\u0926\u094d\u0926",
        "\u00bf": "\u0930\u0942",
        ">": "\u0936\u094d\u0930",
        ":": "\u0938\u094d",
        "\u00a7": "\u091f\u094d\u091f",
        "&": "\u096d",
        "\u00a3": "\u0918\u094d",
        "\u2022": "\u0921\u094d\u0921",
        ".": "\u0964",
        "\u00ab": "\u094d\u0930",
        "*": "\u096e",
        "\u201e": "\u0927\u094d\u0930",
        "w": "\u0927",
        "s": "\u0915",
        "g": "\u0928",
        "\u00e6": "\u201c",
        "c": "\u0905",
        "o": "\u092f",
        "k": "\u092a",
        "W": "\u0927\u094d",
        "\u00d6": "=",
        "S": "\u0915\u094d",
        "\u00d2": "\u00a8",
        "_": ")",
        "[": "\u0943",
        "\u00da": "\u2019",
        "G": "\u0928\u094d",
        "\u02c6": "\u092b\u094d",
        "C": "\u090b",
        "O": "\u0907",
        "\u00ce": "\u0919\u094d\u0916",
        "K": "\u092a\u094d",
        "7": "\u0920",
        "\u00b6": "\u0920\u094d\u0920",
        "3": "\u0918",
        "9": "\u0922",
        "?": "\u0930\u0941",
        ";": "\u0938",
        "'": "\u0941",
        "#": "\u0969",
        "\u00a2": "\u0926\u094d\u0918",
        "/": "\u0930",
        "+": "\u0902",
        "\u00aa": "\u0919",
        "t": "\u0924",
        "p": "\u0909",
        "|": "\u094d\u0930",
        "x": "\u0939",
        "\u00e5": "\u0926\u094d\u0935",
        "d": "\u092e",
        "`": "\u091e",
        "l": "\u093f",
        "h": "\u091c",
        "T": "\u0924\u094d",
        "P": "\u090f",
        "\u00dd": "\u091f\u094d\u091f\u094d",
        "\\": "\u094d",
        "\u00d9": ";",
        "X": "\u0939\u094d",
        "\u00c5": "\u0939\u0943",
        "D": "\u092e\u094d",
        "@": "\u0968",
        "\u00cd": "\u0919\u094d\u0915",
        "L": "\u0940",
        "H": "\u091c\u094d",
        "4": "\u0926\u094d\u0927",
        "\u00b1": "+",
        "0": "\u0923\u094d",
        "<": "?",
        "8": "\u0921",
        "\u00a5": "\u0930\u094d\u200d",
        "$": "\u096a",
        "\u00a1": "\u091c\u094d\u091e\u094d",
        ",": ",",
        "\u00a9": "\u0930",
        "(": "\u096f",
        "\u2018": "\u0945",
        "u": "\u0917",
        "q": "\u0924\u094d\u0930",
        "}": "\u0948",
        "y": "\u0925",
        "e": "\u092d",
        "a": "\u092c",
        "i": "\u0937\u094d",
        "\u2030": "\u091d\u094d",
        "U": "\u0917\u094d",
        "Q": "\u0924\u094d\u0924",
        "]": "\u0947",
        "\u02dc": "\u093d",
        "Y": "\u0925\u094d",
        "\u00d8": "\u094d\u092f",
        "E": "\u092d\u094d",
        "A": "\u092c\u094d",
        "M": "\u0903",
        "\u00cc": "\u0928\u094d\u0928",
        "I": "\u0915\u094d\u0937\u094d",
        "5": "\u091b",
        "\u00b4": "\u091d",
        "1": "\u091c\u094d\u091e",
        "\u00b0": "\u0919\u094d\u0922",
        "=": ".",
        "\u00c6": "\u201d",
        "\u2039": "\u0919\u094d\u0918",
        "%": "\u096b",
        "\u00a4": "\u091d\u094d",
        "!": "\u0967",
        "-": "(",
        "\u203a": "\u0926\u094d\u0930",
        ")": "\u0966",
        "\u2026": "\u2018",
        "\u00dc": "%",
    }

    POST_RULES = [
        ["\u094d\u093e", ""],
        [
            "(\u0924\u094d\u0930|\u0924\u094d\u0924)([^\u0909\u092d\u092a]+?)m",
            "\\1m\\2",
        ],
        ["\u0924\u094d\u0930m", "\u0915\u094d\u0930"],
        ["\u0924\u094d\u0924m", "\u0915\u094d\u0924"],
        ["([^\u0909\u092d\u092a]+?)m", "m\\1"],
        ["\u0909m", "\u090a"],
        ["\u092dm", "\u091d"],
        ["\u092am", "\u092b"],
        ["\u0907{", "\u0908"],
        ["\u093f((.\u094d)*[^\u094d])", "\\1\u093f"],
        [
            "(.[\u093e\u093f\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c\u0902\u0903\u0901]*?){",
            "{\\1",
        ],
        ["((.\u094d)*){", "{\\1"],
        ["{", "\u0930\u094d"],
        [
            "([\u093e\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c\u0902\u0903\u0901]+?)(\u094d(.\u094d)*[^\u094d])",
            "\\2\\1",
        ],
        [
            "\u094d([\u093e\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c\u0902\u0903\u0901]+?)((.\u094d)*[^\u094d])",
            "\u094d\\2\\1",
        ],
        [
            "([\u0902\u0901])([\u093e\u093f\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c\u0903]*)",
            "\\2\\1",
        ],
        ["\u0901\u0901", "\u0901"],
        ["\u0902\u0902", "\u0902"],
        ["\u0947\u0947", "\u0947"],
        ["\u0948\u0948", "\u0948"],
        ["\u0941\u0941", "\u0941"],
        ["\u0942\u0942", "\u0942"],
        ["^\u0903", ":"],
        ["\u091f\u0943", "\u091f\u094d\u091f"],
        ["\u0947\u093e", "\u093e\u0947"],
        ["\u0948\u093e", "\u093e\u0948"],
        ["\u0905\u093e\u0947", "\u0913"],
        ["\u0905\u093e\u0948", "\u0914"],
        ["\u0905\u093e", "\u0906"],
        ["\u090f\u0947", "\u0910"],
        ["\u093e\u0947", "\u094b"],
        ["\u093e\u0948", "\u094c"],
    ]

    def convert(self, text):
        """
        Convert Preeti-encoded text to Unicode Devanagari.

        Args:
            text (str): Text encoded in Preeti font.

        Returns:
            str: Unicode Devanagari text.
        """
        if not text:
            return text

        output = []
        for ch in text:
            output.append(self.CHAR_MAP.get(ch, ch))
        result = "".join(output)

        for pattern, replacement in self.POST_RULES:
            result = re.sub(pattern, replacement, result)

        return result


def preeti_to_unicode(text):
    """
    Convenience function to convert Preeti text to Unicode.

    Args:
        text (str): Preeti-encoded text.

    Returns:
        str: Unicode Devanagari text.
    """
    return PreetiConverter().convert(text)
