# Stopwords API

## Overview

Manage and filter Nepali stopwords (340+ curated words).

## Functions

### `get_stopwords()`

Get the current stopword list.

```python
from nepalikit.manage_stopwords import get_stopwords

stopwords = get_stopwords()
print(len(stopwords))  # 340
```

### `is_stopword(word)`

Check if a word is a stopword.

```python
from nepalikit.manage_stopwords import is_stopword

is_stopword("र")       # True
is_stopword("नेपाल")   # False
```

### `add_stopwords(words)`

Add custom stopwords.

```python
from nepalikit.manage_stopwords import add_stopwords, is_stopword

add_stopwords(["नेपाल", "काठमाडौं"])
is_stopword("नेपाल")  # True
```

### `remove_custom_stopwords(words)`

Remove words from custom stopwords (cannot remove defaults).

```python
from nepalikit.manage_stopwords import remove_custom_stopwords

remove_custom_stopwords(["नेपाल"])
```

### `remove_stopwords_from_text(text, stopwords=None)`

Remove stopwords from text.

```python
from nepalikit.manage_stopwords import remove_stopwords_from_text

filtered = remove_stopwords_from_text("म घर जाँदै छु")
print(filtered)  # "घर जाँदै"

# With custom stopwords
filtered = remove_stopwords_from_text("म घर जाँदै छु", stopwords=["घर"])
print(filtered)  # "म जाँदै छु"
```

### `load_stopwords(folder_path)`

Load stopwords from text files (legacy API).

```python
from nepalikit.manage_stopwords import load_stopwords

stopwords = load_stopwords("/path/to/stopwords/")
print(stopwords)
```


