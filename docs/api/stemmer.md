# Stemmer API

## Overview

Rule-based stemmer for Nepali language. Strips common suffixes to reduce words to their root forms. Also includes a Snowball stemmer wrapper for an alternative algorithm.

## Functions

### `stem(word)`

Stem a single Nepali word using the built-in stemmer.

```python
from nepalikit.stemmer import stem

stem("नेपालमा")  # "नेपाल"
stem("मानिसहरू")  # "मानिस"
stem("खान्छु")   # "खान्"
stem("गरेको")    # "गर"
```

### `stem_text(text)`

Stem all words in text.

```python
from nepalikit.stemmer import stem_text

stemmed = stem_text("मानिसहरू खान्छन्")
print(stemmed)  # "मानिस खान्"
```

### `snowball_stem(word)`

Stem a word using the Snowball algorithm (requires `snowballstemmer` package).

```python
from nepalikit.stemmer import snowball_stem

snowball_stem("नेपालमा")  # "नेपाल"
```

## Classes

### `NepaliStemmer`

Built-in rule-based stemmer with configurable minimum residue.

```python
from nepalikit.stemmer import NepaliStemmer

stemmer = NepaliStemmer()
stemmer.stem("नेपालमा")  # "नेपाल"

# With custom minimum residue (default 2)
stemmer = NepaliStemmer(min_residue=3)
```

### `SnowballStemmer`

Wrapper around the Snowball stemmer for Nepali.

```python
from nepalikit.stemmer import SnowballStemmer

sb = SnowballStemmer()
sb.stem("नेपालमा")     # "नेपाल"
sb.stem_words(["मानिस", "खान्छन्"])
sb.stem_text("मानिसहरू खान्छन्")
```

## Suffixes Removed

The stemmer removes common Nepali suffixes including:

- **Case markers**: मा, ले, बाट, लाई
- **Possessives**: को, का, की
- **Plurals**: हरू, हरु
- **Verb endings**: छ, छन्, थियो, गर्
- **Postpositions**: सँग, लागि, तिर
- **Composite forms**: हरूकोलागि, हरूले, तर्फबाट, बीचमा

## Methods

### `NepaliStemmer.stem(word)`

Stem a single word.

**Parameters:**
- `word` (str): Word to stem

**Returns:** Stemmed word

### `NepaliStemmer.stem_text(text)`

Stem all words in text.

**Parameters:**
- `text` (str): Input text

**Returns:** Text with all words stemmed

### `NepaliStemmer.stem_words(words)`

Stem a list of words.

**Parameters:**
- `words` (list): List of words

**Returns:** List of stemmed words

### `SnowballStemmer.stem(word)`

Stem a single word using Snowball algorithm.

**Parameters:**
- `word` (str): Word to stem

**Returns:** Stemmed word

### `SnowballStemmer.stem_words(words)`

Stem a list of words using Snowball algorithm.

**Parameters:**
- `words` (list): List of words

**Returns:** List of stemmed words

### `SnowballStemmer.stem_text(text)`

Stem all words in text using Snowball algorithm.

**Parameters:**
- `text` (str): Input text

**Returns:** Text with all words stemmed
