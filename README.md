NepaliKit
=========

[![Current Release Version](https://img.shields.io/github/release/prabhashj07/nepalikit.svg?style=flat-square&logo=github)](https://github.com/prabhashj07/nepalikit/releases)
[![pypi Version](https://img.shields.io/pypi/v/nepalikit.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/NepaliKit/)
[![PyPi downloads](https://static.pepy.tech/personalized-badge/NepaliKit?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/NepaliKit/)

NepaliKit is a Python library for natural language processing tasks in the Nepali language.

## Installation

```bash
pip install nepalikit
```

## Quick Start

```python
from nepalikit.tokenization import Tokenizer
from nepalikit.preprocessing import TextProcessor
from nepalikit.manage_stopwords import get_stopwords, remove_stopwords_from_text

# Tokenize text
tokenizer = Tokenizer()
tokens = tokenizer.tokenize("नमस्ते, के छ खबर? यो एउटा वाक्य हो।", level='word')

# Clean text
processor = TextProcessor()
clean = processor.remove_html_tags("<p>नमस्ते</p>")
clean = processor.remove_special_characters(clean)

# Remove stopwords
filtered = remove_stopwords_from_text("म घर जाँदै छु")
```

## Features

- **Tokenization** — Rule-based and SentencePiece tokenizers
- **Preprocessing** — HTML removal, special character cleaning, whitespace normalization
- **Stopword Management** — 340+ curated Nepali stopwords with dynamic add/remove
- **Stemming** — Rule-based suffix stripping
- **Normalization** — Unicode NFC normalization, ZWNJ/ZWJ stripping, script detection
- **POS Tagging** — Dictionary-based tagger with 11 grammatical categories
- **Spell Checking** — Dictionary-based with Levenshtein edit distance suggestions
- **Transliteration** — Roman &harr; Devanagari conversion
- **Number Extraction** — Parse Devanagari digits and Nepali number words to integers

## Documentation

Full documentation is available at [docs/](docs/index.md):

- [Installation Guide](docs/installation.md)
- [Quick Start](docs/quickstart.md)
- [API Reference](docs/api/)
- [Examples](docs/examples/)
- [Contributing](docs/contributing.md)
- [Future Roadmap](docs/future-roadmap.md)

## License

This project is licensed under the MIT License.

## Author

- Prabhash Kumar Jha
- Email: prabhashj07@gmail.com
