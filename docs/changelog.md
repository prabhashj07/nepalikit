# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added
- **ML POS Tagger**: Context-aware POS tagger using n-gram statistics and Viterbi decoding. Bigram transition model, emission probabilities, suffix rules, and context pattern boosting. Zero-dependency pure Python implementation. (`MLPOSTagger`, `ml_tag_pos()`, `ml_tag_text()`)
- **Stemmer**: Rule-based stemming for Nepali words. Strips common suffixes (case markers, possessives, plurals, verb endings) to reduce words to root forms. (`NepaliStemmer`, `stem()`, `stem_text()`)
- **Normalizer**: Unicode normalization, ZWNJ/ZWJ stripping, control character cleanup, and script detection (devanagari/latin/mixed). (`NepaliNormalizer`, `normalize()`, `detect_script()`)
- **Number Extractor**: Parse and convert Nepali numeric expressions including Devanagari digits (0-9) and number words. (`NepaliNumberExtractor`, `extract_numbers()`, `convert_number()`)
- **POS Tagger**: Dictionary-based part-of-speech tagger with rule-based fallback for unknown words. Supports 11 grammatical categories. (`NepaliPOSTagger`, `tag_pos()`)
- **Spell Checker**: Dictionary-based spell checking with Levenshtein edit distance for generating correction suggestions. (`NepaliSpellChecker`, `check_spelling()`, `suggest_corrections()`)
- **Transliteration**: Character-level Roman to Devanagari and Devanagari to Roman conversion. (`NepaliTransliterator`, `roman_to_devanagari()`, `devanagari_to_roman()`)
- **Preeti Converter**: Convert Preeti font encoded text to Unicode Devanagari. (`PreetiConverter`, `preeti_to_unicode()`)
- **Snowball Stemmer**: Wrapper around the `snowballstemmer` package for algorithmic stemming. (`SnowballStemmer`)
- **Sentence Operations**: Sentence extraction, segmentation, abbreviation-aware splitting, and sentence analysis. (`extract_sentences`, `SentenceAnalyzer`)
- **Enhanced Stopwords**: Expanded stopword list to 340+ curated Nepali stopwords. Added `get_stopwords()`, `is_stopword()`, `add_stopwords()`, and `remove_custom_stopwords()` convenience functions.
- **Enhanced Stemmer**: Expanded suffix rules with perfect-aspect forms, composite plurals, additional postpositions, and common verb forms.
- **Enhanced Number Extractor**: Added 0-99 number words, decimal scale support, Indian-style comma handling, larger multipliers, and improved compound expression parsing.
- **POS Dictionary**: Bundled POS dictionary for common Nepali words.
- **Spelling Dictionary**: Bundled word dictionary for spell checking.
- **Stemmer Rules**: Configurable suffix stripping rules.
- **Full API documentation**: MkDocs Material site with usage guides, examples, and API reference.

### Fixed
- Replaced wildcard imports with explicit imports across the codebase.
- Removed unused imports (`os`, `load_abbreviations`, `Counter`).
- Simplified dead branching logic in `AbbreviationReplacer._generate_pattern()`.
- Removed `__main__` blocks from library files.
- Fixed hardcoded `./data` path in `train.py` — now accepts `input_path` argument.
- Replaced broad `except Exception` with specific `FileNotFoundError` in `load_abbreviation.py`.
- Fixed wrong docstring filenames in `sentence_operation` and `urls_emails`.
- Fixed documentation errors across all doc files (wrong outputs, missing parameters, broken links).
- Fixed `test_model_file_not_found` to catch `RuntimeError` (sentencepiece).

### Changed
- Migrated to `setuptools-scm` for dynamic versioning from git tags.
- Loosened `sentencepiece` dependency from `==0.2.0` to `>=0.2.1,<1.0`.
- Added auto GitHub Release creation on tag push via CI.
- All new modules are zero-dependency (Python stdlib only).
- Improved CI/CD: added Python 3.13, uv caching, ruff format check, mypy type checking, pytest-cov, pip-audit security scanning.
- Added GitHub Pages deployment for documentation.
- Added docs build check to CI.
- Added Dependabot for GitHub Actions and pip dependency updates.
- Added pre-commit hooks (trailing whitespace, ruff lint/format, mypy).

## Version 1.0.3 (January 8, 2026)

### Fixed
- Fixed missing comma in `__init__.py` `__all__` causing string concatenation bug.
- Fixed `__init__.py` `__all__` referencing `'remove_stopwords'` instead of `'remove_stopwords_from_text'`.
- Fixed `__init__.py` `__all__` referencing `'load_abbreviation'` instead of `'load_abbreviations'`.
- Fixed `segment_sentences()` calling `load_abbreviations()` without required argument.
- Fixed `segment_sentences()` calling `extract_sentences(text)` as function instead of instantiating class.
- Fixed `SentenceAnalyzer.__init__()` calling `load_stopwords()` without required argument.
- Fixed `preprocess_text()` calling methods in wrong order: URLs removed after special character stripping.
- Fixed `count_words_in_paragraph()` splitting on English `.` instead of Nepali `|`.
- Fixed `SentencePieceTokenizer` printing debug output to stdout on initialization.
- Fixed `SentencePieceTokenizer` reloading SentencePiece model from disk on every `tokenize()`/`detokenize()` call.
- Fixed `tokenizer.tokenize()` not accepting `'character'` as level (only `'characters'` worked).
- Fixed `setup.py` referencing non-existent `nepalikit.__main__:main` entry point.
- Fixed `setup.py` opening `README.md` twice (unused `fh` variable).
- Fixed `load_abbreviations()` using non-standard `__file__`-based path navigation to non-existent `../../data` directory.
- Fixed `load_abbreviations()` crashing when value contains colons (used `split(':')` instead of `split(':', 1)`).
- Fixed `AbbreviationReplacer` crashing on import due to non-existent data directory path.
- Fixed `AbbreviationReplacer.replace_abbreviations()` crashing with error on empty pattern.
- Fixed `load_stopwords()` crashing with `FileNotFoundError` on non-existent directory paths.

### Changed
- Migrated `SentencePieceTokenizer` to use `importlib.resources` instead of `os.path.dirname(__file__)`.
- Added `.vocab` file to `package_data` and `MANIFEST.in`.
- Migrated packaging from `setup.py` + `requirements.txt` + `MANIFEST.in` to `pyproject.toml`.
- Removed unused `torch` dependency (was never imported).
- Replaced `regex` dependency with stdlib `re`.
- Updated GitHub Actions workflow to use `uv` instead of `pip`.
- Bumped minimum Python version to 3.9.

## Version 1.0.2

### Added
- Initial release of `nepalikit` with tokenization and detokenization features.
- Added new model to the project folder.
- Created a `tests` directory with test files.
- Added `replace_abbreviation.py` for replacing abbreviation.
- Added `sentence_stats.py` for showing statistics of sentences.

### Changed
- Updated directory structure for better organization.
- Updated README.md to reflect new structure.
- Changed package name from `NepaliKit` to `nepalikit`.
- Updated `extract_sentences.py` with new functionality.
- Updated `normalize_text.py`.

### Fixed
- Fixed issues in `load_abbreviation.py`.
- Fixed issues in `segment_sentences.py`.
- Corrected errors in the codebase.
