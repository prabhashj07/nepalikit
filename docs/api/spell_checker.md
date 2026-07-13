# Spell Checker API

## Overview

Dictionary-based spell checking with Levenshtein edit distance for correction suggestions.

## Functions

### `check_spelling(word, dictionary_path=None)`

Check if a word is spelled correctly.

**Parameters:**
- `word` (str): The word to check
- `dictionary_path` (str, optional): Custom dictionary path

**Returns:** True if correct

```python
from nepalikit.spell_checker import check_spelling

check_spelling("नेपाल")   # True
check_spelling("नेपालक")  # False

# With custom dictionary
check_spelling("नेपाल", dictionary_path="/path/to/dict.txt")
```

### `suggest_corrections(word, max_distance=2, dictionary_path=None)`

Get correction suggestions for a misspelled word.

```python
from nepalikit.spell_checker import suggest_corrections

suggest_corrections("नेपालक")  # ["नेपालको", "नेपालका"]
suggest_corrections("राम")     # ["राम"]

# With custom dictionary
suggest_corrections("नेपालक", dictionary_path="/path/to/custom_dict.txt")
```

## Classes

### `NepaliSpellChecker`

Advanced spell checker with custom dictionary support.

```python
from nepalikit.spell_checker import NepaliSpellChecker

# Use bundled dictionary (default)
checker = NepaliSpellChecker()

# Use custom dictionary
checker = NepaliSpellChecker(dictionary_path="/path/to/my_dict.txt")

# Check word
checker.check("नेपाल")  # True

# Get suggestions
checker.suggest("नेपालक")  # ["नेपालको", "नेपालका"]

# Add word to dictionary
checker.add_word("नेपाली")

# Correct text
corrected = checker.correct("मेरो नेपालक नाम छ")
print(corrected)
```

## Methods

### `NepaliSpellChecker.__init__(dictionary_path=None)`

Initialize the spell checker.

**Parameters:**
- `dictionary_path` (str, optional): Path to a custom dictionary file (one word per line). If `None`, uses the bundled dictionary.

### `NepaliSpellChecker.check(word)`

Check if a word is in the dictionary.

**Parameters:**
- `word` (str): Word to check

**Returns:** True if correct

### `NepaliSpellChecker.suggest(word, max_distance=2, max_suggestions=5)`

Suggest corrections for a misspelled word.

**Parameters:**
- `word` (str): Misspelled word
- `max_distance` (int): Maximum edit distance
- `max_suggestions` (int): Maximum suggestions to return

**Returns:** List of suggestions

### `NepaliSpellChecker.correct(text, max_distance=1)`

Correct misspellings in text.

**Parameters:**
- `text` (str): Input text
- `max_distance` (int): Maximum edit distance for corrections

**Returns:** Corrected text

### `NepaliSpellChecker.add_word(word)`

Add a word to the dictionary.

**Parameters:**
- `word` (str): Word to add
