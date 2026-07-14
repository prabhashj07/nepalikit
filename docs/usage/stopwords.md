# Stopwords

NepaliKit provides 340+ curated Nepali stopwords with dynamic management capabilities.

## Features

- 340+ curated Nepali stopwords
- Dynamic add/remove custom stopwords
- Filter stopwords from text
- Query stopword status

## Basic Usage

```python
from nepalikit.manage_stopwords import (
    get_stopwords,
    is_stopword,
    add_stopwords,
    remove_custom_stopwords,
    remove_stopwords_from_text,
)

# Get all stopwords
stopwords = get_stopwords()
print(len(stopwords))  # 340+

# Check if word is a stopword
print(is_stopword("र"))     # True
print(is_stopword("नेपाल")) # False

# Remove stopwords from text
filtered = remove_stopwords_from_text("म घर जाँदै छु")
print(filtered)  # "घर जाँदै"

# Add custom stopwords
add_stopwords(["नमस्ते", "धन्यवाद"])
print(is_stopword("नमस्ते"))  # True

# Remove custom stopwords
remove_custom_stopwords(["नमस्ते", "धन्यवाद"])
print(is_stopword("नमस्ते"))  # False
```
