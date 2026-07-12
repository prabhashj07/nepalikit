# Changelog

All notable changes to this project will be documented in this file.

## Version 1.1.0 (January 8, 2026)

### Added
- **Stemmer**: Rule-based stemming for Nepali words. Strips common suffixes (case markers, possessives, plurals, verb endings) to reduce words to root forms. (`NepaliStemmer`, `stem()`, `stem_text()`)
- **Normalizer**: Unicode normalization, ZWNJ/ZWJ stripping, control character cleanup, and script detection (devanagari/latin/mixed). (`NepaliNormalizer`, `normalize()`, `detect_script()`)
- **Number Extractor**: Parse and convert Nepali numeric expressions including Devanagari digits (०-९) and number words (एक, दुई, सय, हजार, लाख, करोड). (`NepaliNumberExtractor`, `extract_numbers()`, `convert_number()`)
- **POS Tagger**: Dictionary-based part-of-speech tagger with rule-based fallback for unknown words. Supports 11 grammatical categories. (`NepaliPOSTagger`, `tag_pos()`)
- **Spell Checker**: Dictionary-based spell checking with Levenshtein edit distance for generating correction suggestions. (`NepaliSpellChecker`, `check_spelling()`, `suggest_corrections()`)
- **Transliteration**: Character-level Roman to Devanagari and Devanagari to Roman conversion. (`NepaliTransliterator`, `roman_to_devanagari()`, `devanagari_to_roman()`)
- **Enhanced Stopwords**: Expanded stopword list to 340+ curated Nepali stopwords in `nepalikit/data/stopwords.txt`. Added `get_stopwords()`, `is_stopword()`, `add_stopwords()`, and `remove_custom_stopwords()` convenience functions. Based on community resources and Nepali grammar references.
- **Enhanced Stemmer**: Expanded suffix rules with perfect-aspect forms (`ेको`/`ेका`/`एको`), composite plurals (`हरूसँग`/`हरूसम्म`/`हरूकोलागि`), additional postpositions (`सँग`/`लागि`/`तिर`), and common verb forms (`गर्छ`/`गर्छन्`/`रहेको`/`भएको`). Suffix list now covers more morphological patterns based on Nepali grammar research.
- **Enhanced Number Extractor**: Added 0–99 number words (was 0–90), decimal scale support (`२.५ लाख` = 250000), Indian-style comma handling (`१,२३,४५६`), larger multipliers (`खर्ब`), and improved compound expression parsing.
- **POS Dictionary**: Bundled POS dictionary for common Nepali words in `nepalikit/data/pos_dictionary.json`.
- **Spelling Dictionary**: Bundled word dictionary for spell checking in `nepalikit/data/spelling_dict.txt`.
- **Stemmer Rules**: Configurable suffix stripping rules in `nepalikit/data/stemmer_rules.json`.
- **86 new tests** across 6 test files (124 total, up from 38).

### Fixed
- **Number Extractor**: `_word_to_int` now correctly returns `0` for शून्य.
- **Stemmer**: Removed typo `'माp'` from fallback suffixes; added `None` guards to `stem_text()` and `stem_words()`.
- **Normalizer**: Added `None` guards to `strip_zwnj()` and `strip_control_chars()`; removed unused compiled regex.
- **POS Tagger**: Fixed `_is_proper_noun()` (removed broken `istitle()` for Devanagari); fixed overlapping words between CONJUNCTIONS and PARTICLES; removed `'को'` from PRONOUNS.
- **Spell Checker**: Removed unused imports (`os`, `defaultdict`).
- **Stemmer**: Removed unused import (`os`).
- **Stopwords**: Deduplicated stopword list and expanded from 191 to 340+ unique entries via community contributions.
- **Transliteration**: Removed consonant+`a` dictionary entries to fix vowel composition; all consonant+vowel pairs now compose correctly via virama-based lookup. Fixed dental/retroflex collision in `devanagari_to_roman` using IAST diacritics.

### Changed
- Updated `__version__` to `"1.1.0"`.
- Updated `pyproject.toml` version to `1.1.0` and added new data files to `package-data`.
- All new modules are zero-dependency (Python stdlib only, no new pip packages required).
- Added 11 new tests across 3 test files (144 total, up from 38).

## Version 1.0.3 (January 8, 2026)

### Fixed
- Fixed missing comma in `__init__.py` `__all__` causing string concatenation bug.
- Fixed `__init__.py` `__all__` referencing `'remove_stopwords'` instead of `'remove_stopwords_from_text'`.
- Fixed `__init__.py` `__all__` referencing `'load_abbreviation'` instead of `'load_abbreviations'`.
- Fixed `segment_sentences()` calling `load_abbreviations()` without required argument.
- Fixed `segment_sentences()` calling `extract_sentences(text)` as function instead of instantiating class.
- Fixed `SentenceAnalyzer.__init__()` calling `load_stopwords()` without required argument.
- Fixed `preprocess_text()` calling methods in wrong order: URLs removed after special character stripping.
- Fixed `count_words_in_paragraph()` splitting on English `.` instead of Nepali `।`.
- Fixed `SentencePieceTokenizer` printing debug output to stdout on initialization.
- Fixed `SentencePieceTokenizer` reloading SentencePiece model from disk on every `tokenize()`/`detokenize()` call.
- Fixed `tokenizer.tokenize()` not accepting `'character'` as level (only `'characters'` worked).
- Fixed `setup.py` referencing non-existent `nepalikit.__main__:main` entry point.
- Fixed `setup.py` opening `README.md` twice (unused `fh` variable).
- Fixed `load_abbreviations()` using non-standard `__file__`-based path navigation to non-existent `../../data` directory. Removed broken path.
- Fixed `load_abbreviations()` crashing when value contains colons (used `split(':')` instead of `split(':', 1)`).
- Fixed `AbbreviationReplacer` crashing on import due to non-existent data directory path.
- Fixed `AbbreviationReplacer.replace_abbreviations()` crashing with error on empty pattern.
- Fixed `load_stopwords()` crashing with `FileNotFoundError` on non-existent directory paths.

### Changed
- Migrated `SentencePieceTokenizer` to use `importlib.resources` instead of `os.path.dirname(__file__)` for loading the model file.
- Added `.vocab` file to `package_data` and `MANIFEST.in`.
- Migrated packaging from `setup.py` + `requirements.txt` + `MANIFEST.in` to `pyproject.toml`.
- Removed unused `torch` dependency (was never imported).
- Replaced `regex` dependency with stdlib `re`.
- Updated GitHub Actions workflow to use `uv` instead of `pip`.
- Bumped minimum Python version to 3.9 (required by `importlib.resources.files()`).

## Version 1.0.2

### Added
- Initial release of `nepalikit` with tokenization and detokenization features.
- Added new model to the project folder.
- Created a `tests` directory with test files to ensure code quality and functionality.
- Added `replace_abbreviation.py` for replacing abbreviation.
- Added `sentence_stats.py` for showing statistics of sentences.

### Changed
- Updated directory structure for better organization.
- Updated README.md file to reflect new structure and added detailed usage instructions.
- Changed package name from `NepaliKit` to `nepalikit`.
- Updated `extract_sentences.py` with new functionality.
- Updated `normalize_text.py`.

### Fixed
- Fixed issues in `load_abbreviation.py`.
- Fixed issues in `segment_sentences.py`.
- Corrected errors in the codebase for improved stability and performance.
