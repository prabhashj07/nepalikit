"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nepalikit")
except PackageNotFoundError:
    __version__ = "0.0.0"

from nepalikit.manage_stopwords import (
    add_stopwords,
    get_stopwords,
    is_stopword,
    load_stopwords,
    remove_custom_stopwords,
    remove_stopwords_from_text,
)
from nepalikit.normalizer import (
    NepaliNormalizer,
    contains_devanagari,
    contains_latin,
    detect_script,
    is_devanagari,
    mixed_script_ratio,
    normalize,
)
from nepalikit.number_extractor import (
    NepaliNumberExtractor,
    convert_number,
    extract_numbers,
)
from nepalikit.pos_tagger import NepaliPOSTagger, tag_pos
from nepalikit.preprocessing import TextProcessor, urls_emails
from nepalikit.sentence_operation import (
    AbbreviationReplacer,
    SentenceAnalyzer,
    TextNormalizer,
    extract_sentences,
    load_abbreviations,
    segment_sentences,
)
from nepalikit.spell_checker import (
    NepaliSpellChecker,
    check_spelling,
    suggest_corrections,
)
from nepalikit.stemmer import (
    NepaliStemmer,
    SnowballStemmer,
    snowball_stem,
    stem,
    stem_text,
)
from nepalikit.lemmatizer import NepaliLemmatizer, lemmatize, lemmatize_text
from nepalikit.tokenization import SentencePieceTokenizer, Tokenizer
from nepalikit.transliterate import (
    NepaliTransliterator,
    PreetiConverter,
    devanagari_to_roman,
    preeti_to_unicode,
    roman_to_devanagari,
)
from nepalikit.utils import NepaliTextProcessor

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
    "NepaliLemmatizer",
    "lemmatize",
    "lemmatize_text",
]
