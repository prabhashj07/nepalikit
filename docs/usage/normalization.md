# Normalization

The `normalizer` module provides Unicode normalization, whitespace cleanup, and script detection for Nepali text.

## Features

- **Unicode NFC normalization**: Standardizes composed/decomposed characters
- **ZWNJ/ZWJ stripping**: Removes zero-width joiner/non-joiner characters
- **Control character cleanup**: Strips non-printable characters
- **Script detection**: Identifies Devanagari, Latin, or mixed scripts

## Basic Usage

```python
from nepalikit.normalizer import normalize, detect_script

# Normalize text
text = "म  नाम   राम हो"
normalized = normalize(text)
print(normalized)  # "म नाम राम हो"

# Detect script
script = detect_script("मेरो नाम राम हो")
print(script)  # "devanagari"

script = detect_script("Hello world")
print(script)  # "latin"

script = detect_script("नमस्ते world")
print(script)  # "mixed"
```

## Why Normalize?

Nepali text from different sources may use inconsistent Unicode representations. Normalization ensures consistent processing downstream.
