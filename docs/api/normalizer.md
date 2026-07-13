# Normalizer API

## Overview

Unicode normalization, ZWNJ/ZWJ stripping, and script detection for Nepali text.

## Functions

### `normalize(text, form="NFC")`

Normalize text with all options enabled.

```python
from nepalikit.normalizer import normalize

normalize("म  नाम   राम हो")  # "म नाम राम हो"
normalize("म\u200Cनाम")       # "मनाम"
```

### `detect_script(text)`

Detect the script of the text.

```python
from nepalikit.normalizer import detect_script

detect_script("मेरो नाम राम हो")  # "devanagari"
detect_script("mero naam ram ho")  # "latin"
detect_script("मेरो name ram")     # "mixed"
detect_script("12345")              # "other"
```

### `is_devanagari(text)`

Check if text is purely Devanagari (ignoring whitespace/punctuation).

```python
from nepalikit.normalizer import is_devanagari

is_devanagari("नेपाल")      # True
is_devanagari("नेपाल a")    # False
```

### `contains_devanagari(text)`

Check if text contains at least one Devanagari character.

```python
from nepalikit.normalizer import contains_devanagari

contains_devanagari("Hello नमस्ते")  # True
contains_devanagari("Hello")          # False
```

### `contains_latin(text)`

Check if text contains at least one Latin character.

```python
from nepalikit.normalizer import contains_latin

contains_latin("Hello नमस्ते")  # True
contains_latin("नेपाल")          # False
```

### `mixed_script_ratio(text)`

Compute Devanagari fraction over Devanagari + Latin characters.

```python
from nepalikit.normalizer import mixed_script_ratio

mixed_script_ratio("नेपाल Hello")  # 0.5
mixed_script_ratio("नेपाल")          # 1.0
mixed_script_ratio("Hello")          # 0.0
```

## Classes

### `NepaliNormalizer`

Advanced normalizer with configurable options.

```python
from nepalikit.normalizer import NepaliNormalizer

normalizer = NepaliNormalizer()
normalized = normalizer.normalize("म  नाम")
print(normalized)  # "म नाम"

script = normalizer.detect_script("मेरो नाम")
print(script)  # "devanagari"

# Check if text is purely Devanagari
normalizer.is_devanagari("नेपाल")  # True

# Get Devanagari fraction
normalizer.mixed_script_ratio("नेपाल Hello")  # 0.5
```

## Methods

### `NepaliNormalizer.normalize(text, form="NFC")`

Apply full normalization pipeline.

**Parameters:**
- `text` (str): Input text
- `form` (str): Unicode normalization form ('NFC' or 'NFKC')

**Returns:** Normalized text

### `NepaliNormalizer.detect_script(text)`

Detect the script of text.

**Parameters:**
- `text` (str): Input text

**Returns:** 'devanagari', 'latin', 'mixed', or 'other'

### `NepaliNormalizer.is_devanagari(text)`

Check if every non-whitespace, non-punctuation character is Devanagari.

**Parameters:**
- `text` (str): Input text

**Returns:** bool

### `NepaliNormalizer.contains_devanagari(text)`

Check if text contains at least one Devanagari character.

**Parameters:**
- `text` (str): Input text

**Returns:** bool

### `NepaliNormalizer.contains_latin(text)`

Check if text contains at least one Latin character.

**Parameters:**
- `text` (str): Input text

**Returns:** bool

### `NepaliNormalizer.mixed_script_ratio(text)`

Compute Devanagari fraction over Devanagari + Latin characters.

**Parameters:**
- `text` (str): Input text

**Returns:** float (0.0 to 1.0)

### `NepaliNormalizer.strip_zwnj(text)`

Remove zero-width joiners and non-joiners.

**Parameters:**
- `text` (str): Input text

**Returns:** Text without ZWNJ/ZWJ

### `NepaliNormalizer.strip_control_chars(text)`

Remove Unicode control characters.

**Parameters:**
- `text` (str): Input text

**Returns:** Cleaned text

### `NepaliNormalizer.normalize_unicode(text, form="NFC")`

Apply Unicode normalization only (without ZWNJ stripping or control char cleanup).

**Parameters:**
- `text` (str): Input text
- `form` (str): Normalization form ('NFC' or 'NFKC')

**Returns:** Unicode-normalized text
