# Stemmer API

## Overview

Rule-based stemmer for Nepali language. Strips common suffixes to reduce words to their root forms.

## Functions

### `stem(word)`

Stem a single Nepali word.

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

## Classes

### `NepaliStemmer`

Advanced stemmer with configurable rules.

```python
from nepalikit.stemmer import NepaliStemmer

stemmer = NepaliStemmer()
stemmer.stem("नेपालमा")  # "नेपाल"
```

## Suffixes Removed

The stemmer removes common Nepali suffixes including:

- **Case markers**: मा, ले, बाट, लाई
- **Possessives**: को, का, की
- **Plurals**: हरू, हरु
- **Verb endings**: छ, छन्, थियो, गर्
- **Postpositions**: सँग, लागि, तिर

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
