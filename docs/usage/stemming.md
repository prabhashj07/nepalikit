# Stemming

The `stemmer` module provides rule-based stemming for Nepali words by stripping common suffixes.

## Features

- **Rule-based stemmer**: Strips case markers, possessives, plurals, verb endings
- **Text-level stemming**: Stem all words in a text at once
- **Configurable rules**: Extensible suffix rules via JSON

## Basic Usage

```python
from nepalikit.stemmer import stem, stem_text

# Stem a single word
root = stem("नेपालमा")
print(root)  # "नेपाल"

root = stem("गाउँहरू")
print(root)  # "गाउँ"

# Stem all words in text
text = "म घरमा छु।"
stemmed = stem_text(text)
print(stemmed)  # "म घर छु।"
```

## How It Works

The stemmer applies suffix stripping rules in order, removing known suffixes from the end of words. Rules are stored in `nepalikit/data/stemmer_rules.json` and can be customized.
