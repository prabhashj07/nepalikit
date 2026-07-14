# Spell Checking

The spell checker uses a dictionary of known Nepali words and Levenshtein edit distance to detect and suggest corrections for misspelled words.

## Features

- Dictionary-based spell checking
- Levenshtein distance for correction suggestions
- Custom dictionary through stopword management

## Basic Usage

```python
from nepalikit.spell_checker import check_spelling, suggest_corrections

# Check if a word is spelled correctly
print(check_spelling("नेपाल"))   # True
print(check_spelling("नेपालक"))  # False

# Get correction suggestions
suggestions = suggest_corrections("नेपालक")
print(suggestions)  # ["नेपालको", "नेपालका"]
```

## Accuracy Tips

- The dictionary size directly impacts accuracy
- Common misspellings may not have suggestions if too distant
- Consider preprocessing text before spell checking for better results
