# Preprocessing

The `TextProcessor` class provides methods for cleaning and preparing Nepali text.

## Features

- HTML tag removal
- Special character cleaning
- Whitespace normalization
- Configurable cleaning pipeline

## Basic Usage

```python
from nepalikit.preprocessing import TextProcessor

processor = TextProcessor()

# Remove HTML tags
clean = processor.remove_html_tags("<p>राम्रो दिन</p>")
print(clean)  # "राम्रो दिन"

# Remove special characters
clean = processor.remove_special_characters("नेपाली @भाषा! #महान्")
print(clean)  # "नेपाली भाषा महान्"

# Full pipeline
text = "<div>म  घर   जान्छु।</div>"
clean = processor.remove_html_tags(text)
clean = processor.remove_special_characters(clean)
print(clean)
```

## Configuration

The `TextProcessor` constructor accepts an optional `stopwords` parameter (list) to customize the stopword list used by `remove_stopwords()`. See the [API reference](../api/preprocessing.md) for details.
