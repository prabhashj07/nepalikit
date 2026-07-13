"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("nepalikit")
except PackageNotFoundError:
    __version__ = "0.0.0"

from nepalikit.manage_stopwords import (
    load_stopwords,
    remove_stopwords_from_text,
    get_stopwords,
    is_stopword,
    add_stopwords,
    remove_custom_stopwords,
)
from nepalikit.preprocessing import TextProcessor, urls_emails
from nepalikit.tokenization import Tokenizer, SentencePieceTokenizer
from nepalikit.utils import NepaliTextProcessor
from nepalikit.sentence_operation import (
    extract_sentences,
    load_abbreviations,
    TextNormalizer,
    AbbreviationReplacer,
    segment_sentences,
    SentenceAnalyzer,
)

from nepalikit.stemmer import (
    NepaliStemmer,
    stem,
    stem_text,
    SnowballStemmer,
    snowball_stem,
)
from nepalikit.normalizer import (
    NepaliNormalizer,
    normalize,
    detect_script,
    is_devanagari,
    contains_devanagari,
    contains_latin,
    mixed_script_ratio,
)
from nepalikit.number_extractor import (
    NepaliNumberExtractor,
    extract_numbers,
    convert_number,
)
from nepalikit.pos_tagger import NepaliPOSTagger, tag_pos
from nepalikit.spell_checker import (
    NepaliSpellChecker,
    check_spelling,
    suggest_corrections,
)
from nepalikit.transliterate import (
    NepaliTransliterator,
    roman_to_devanagari,
    devanagari_to_roman,
    PreetiConverter,
    preeti_to_unicode,
)

__all__ = [
    "TextProcessor",
    "urls_emails",
    "remove_stopwords_from_text",
    "Tokenizer",
    "SentencePieceTokenizer",
    "NepaliTextProcessor",
    "extract_sentences",
    "load_abbreviations",
    "TextNormalizer",
    "AbbreviationReplacer",
    "segment_sentences",
    "SentenceAnalyzer",
    "load_stopwords",
    "get_stopwords",
    "is_stopword",
    "add_stopwords",
    "remove_custom_stopwords",
    "NepaliStemmer",
    "stem",
    "stem_text",
    "SnowballStemmer",
    "snowball_stem",
    "NepaliNormalizer",
    "normalize",
    "detect_script",
    "is_devanagari",
    "contains_devanagari",
    "contains_latin",
    "mixed_script_ratio",
    "NepaliNumberExtractor",
    "extract_numbers",
    "convert_number",
    "NepaliPOSTagger",
    "tag_pos",
    "NepaliSpellChecker",
    "check_spelling",
    "suggest_corrections",
    "NepaliTransliterator",
    "roman_to_devanagari",
    "devanagari_to_roman",
    "PreetiConverter",
    "preeti_to_unicode",
]
