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

# Unicode-only normalization (no ZWNJ/control char stripping)
uni_norm = normalizer.normalize_unicode("text")
print(uni_norm)
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
