# Preprocessing API

## Overview

Text preprocessing utilities for cleaning Nepali text.

## Classes

### `TextProcessor`

Main preprocessing class with methods for text cleaning.

```python
from nepalikit.preprocessing import TextProcessor

processor = TextProcessor()

# Remove HTML tags
clean = processor.remove_html_tags("<p>राम्रो दिन</p>")
print(clean)  # "राम्रो दिन"

# Remove special characters
clean = processor.remove_special_characters("नेपाल@#$")
print(clean)  # "नेपाल"

# Remove extra whitespace
clean = processor.remove_extra_whitespace("म  नाम   राम")
print(clean)  # "म नाम राम"

# Full preprocessing
clean = processor.preprocess_text("<p>  नेपाल  </p>")
print(clean)  # "नेपाल"
```

### `urls_emails`

URL and email removal utilities.

```python
from nepalikit.preprocessing import urls_emails

# Replace URLs and emails
text = "Visit https://example.com or email test@example.com"
clean = urls_emails.replace_urls_emails(text)
print(clean)

# Remove URLs and emails
clean = urls_emails.remove_urls_emails(text)
print(clean)
```

## Methods

### `TextProcessor.remove_html_tags(text)`

Remove HTML tags from text.

**Parameters:**
- `text` (str): Input text with HTML tags

**Returns:** Text without HTML tags

### `TextProcessor.remove_special_characters(text)`

Remove special characters, keeping only Devanagari and spaces.

**Parameters:**
- `text` (str): Input text

**Returns:** Text with special characters removed

### `TextProcessor.remove_extra_whitespace(text)`

Remove extra whitespace.

**Parameters:**
- `text` (str): Input text

**Returns:** Text with normalized whitespace

### `TextProcessor.preprocess_text(text)`

Apply all preprocessing steps.

**Parameters:**
- `text` (str): Input text

**Returns:** Fully preprocessed text

### `TextProcessor.remove_stopwords(text)`

Remove stopwords from text using the processor's stopword list.

**Parameters:**
- `text` (str): Input text

**Returns:** Text with stopwords removed

### `TextProcessor.normalize_text(text)`

Convert text to lowercase.

**Parameters:**
- `text` (str): Input text

**Returns:** Lowercased text

### `TextProcessor.get_word_frequency(tokens)`

Count the frequency of each word in a list of tokens.

**Parameters:**
- `tokens` (list): List of token strings

**Returns:** `Counter` object with word frequencies
