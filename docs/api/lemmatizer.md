# Lemmatizer API

## Overview

Dictionary-based lemmatizer for Nepali words. Maps inflected forms to their canonical lemma (dictionary form).

## Classes

### `NepaliLemmatizer`

```python
from nepalikit.lemmatizer import NepaliLemmatizer

lemmatizer = NepaliLemmatizer()

# Single word
lemma = lemmatizer.lemmatize("गर्छन्")
print(lemma)  # "गर्नु"

# Full text
text = lemmatizer.lemmatize_text("मैले किताहरू पढेको छु")
print(text)  # "म किता पढ्नु छु"

# List of words
words = lemmatizer.lemmatize_words(["मैले", "किताहरू", "पढेको"])
print(words)  # ["म", "किता", "पढ्नु"]
```

**Constructor:**
- `NepaliLemmatizer(dictionary_path=None, min_residue=2)` — Optional custom dictionary path and minimum stem length.

## Functions

### `lemmatize(word)`

Lemmatize a single word using the default lemmatizer.

```python
from nepalikit.lemmatizer import lemmatize

print(lemmatize("घरले"))     # "घर"
print(lemmatize("गर्छन्"))    # "गर्नु"
print(lemmatize("मैले"))     # "म"
```

### `lemmatize_text(text)`

Lemmatize all words in a text string.

```python
from nepalikit.lemmatizer import lemmatize_text

print(lemmatize_text("मैले किताहरू पढेको छु"))  # "म किता पढ्नु छु"
```

## Methods

### `NepaliLemmatizer.lemmatize(word)`

Find the lemma for a single word. Checks dictionary first, falls back to rule-based suffix stripping.

**Parameters:**
- `word` (str): A Nepali word

**Returns:** str — The lemma of the word

### `NepaliLemmatizer.lemmatize_text(text)`

Lemmatize all words in a text string.

**Parameters:**
- `text` (str): Nepali text

**Returns:** str — Text with each word replaced by its lemma

### `NepaliLemmatizer.lemmatize_words(words)`

Lemmatize a list of words.

**Parameters:**
- `words` (list): List of Nepali word strings

**Returns:** list — List of lemma strings
