# NepaliKit

<div style="text-align:center">
    <em>Comprehensive NLP for the Nepali language</em>
    <br><br>
    <a href="https://pypi.org/project/NepaliKit/" target="_blank">
        <img src="https://img.shields.io/pypi/v/NepaliKit" alt="PyPI">
    </a>
    <a href="https://github.com/prabhashj07/nepalikit/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/prabhashj07/nepalikit" alt="License">
    </a>
</div>

## Overview

NepaliKit is a Python library designed for natural language processing of the Nepali language. It provides a rich set of tools for text tokenization, preprocessing, stemming, POS tagging, spell checking, transliteration, number extraction, and more.

## Features

| Feature | Description | Status |
|---------|-------------|--------|
| Tokenization | Rule-based and SentencePiece tokenization | Stable |
| Text preprocessing | HTML removal, special character cleaning | Stable |
| Normalization | Unicode NFC, ZWNJ/ZWJ stripping | Stable |
| Stemming | Rule-based suffix stripping | Stable |
| POS Tagging | Dictionary-based with fallback, 11 categories | Stable |
| Spell Checking | Levenshtein-based correction | Stable |
| Transliteration | Roman ↔ Devanagari + Preeti | Stable |
| Number Extraction | Parse Nepali numbers | Stable |
| Stopwords | 340+ curated Nepali stopwords | Stable |
| Sentence Ops | Segmentation, extraction, analysis | Stable |

## Quick example

```python
from nepalikit.tokenization import Tokenizer
from nepalikit.normalizer import normalize
from nepalikit.stemmer import stem_text

# Process Nepali text
tokenizer = Tokenizer()
text = "नेपालको राजधानी काठमाडौं हो"

tokens = tokenizer.tokenize(text, level='word')
print(tokens)
# ['नेपालको', 'राजधानी', 'काठमाडौं', 'हो']
```

## Getting Started

- [Installation](installation.md)
- [Quick Start](quickstart.md)
- [Usage Guides](usage/index.md)
- [Examples](examples/index.md)
- [API Reference](api/index.md)

## Project Links

- [GitHub](https://github.com/prabhashj07/nepalikit)
- [Issue Tracker](https://github.com/prabhashj07/nepalikit/issues)
- [PyPI](https://pypi.org/project/NepaliKit/)
- [Changelog](changelog.md)

## License

MIT, see the [LICENSE](https://github.com/prabhashj07/nepalikit/blob/main/LICENSE) file.
