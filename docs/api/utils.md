# Utils API

## Overview

Utility class for basic text processing operations in Nepali language.

## Classes

### `NepaliTextProcessor`

Text processing utilities for merging, splitting, and counting words.

```python
from nepalikit.utils import NepaliTextProcessor

processor = NepaliTextProcessor()

# Merge tokens into text
text = processor.merge_text(["म", "नाम", "राम", "हो"])
print(text)  # "म नाम राम हो"

# Split text into tokens
tokens = processor.split_text("म नाम राम हो")
print(tokens)  # ["म", "नाम", "राम", "हो"]

# Count words
count = processor.count_words("म नाम राम हो")
print(count)  # 4

# Count words in a paragraph (split by ।)
total = processor.count_words_in_paragraph("म नाम राम हो। यो एउटा वाक्य हो।")
print(total)  # 8
```

## Methods

### `NepaliTextProcessor.__init__(delimiter=' ')`

Initialize with a custom delimiter (default: space).

**Parameters:**
- `delimiter` (str): Delimiter for splitting/joining tokens

### `NepaliTextProcessor.merge_text(tokens)`

Merge a list of tokens into a single string.

**Parameters:**
- `tokens` (list): List of token strings

**Returns:** Joined string

### `NepaliTextProcessor.split_text(text)`

Split text into tokens using the delimiter.

**Parameters:**
- `text` (str): Input text

**Returns:** List of tokens

### `NepaliTextProcessor.count_words(text)`

Count the number of words in a text string.

**Parameters:**
- `text` (str): Input text

**Returns:** Word count (int)

### `NepaliTextProcessor.count_words_in_paragraph(paragraph)`

Count total words in a paragraph, splitting on `।` (Devanagari full stop).

**Parameters:**
- `paragraph` (str): Input paragraph

**Returns:** Total word count (int)
