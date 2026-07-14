# Transliteration

Convert text between Roman (Latin) and Devanagari scripts, including Preeti font conversion.

## Features

- **Roman to Devanagari**: Convert romanized Nepali to Devanagari script (e.g., `namaste` → `नमस्ते`)
- **Devanagari to Roman**: Convert Devanagari to romanized form
- **Preeti to Unicode**: Convert text typed in Preeti font to standard Unicode Devanagari

## Basic Usage

```python
from nepalikit.transliterate import (
    roman_to_devanagari,
    devanagari_to_roman,
    preeti_to_unicode,
)

# Roman to Devanagari
devanagari = roman_to_devanagari("namaste")
print(devanagari)  # "नमस्ते"

# Devanagari to Roman
roman = devanagari_to_roman("नमस्ते।")
print(roman)  # "namasatae"

# Preeti font to Unicode
unicode_text = preeti_to_unicode("g]kfn")
print(unicode_text)  # "नेपाल"
```

## Transliteration vs Translation

Transliteration converts characters from one script to another based on pronunciation. It is **not** translation — the meaning stays the same, only the writing system changes.
