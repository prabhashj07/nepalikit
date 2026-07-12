# Transliteration API

## Overview

Character-level transliteration between Romanized and Devanagari Nepali.

## Functions

### `roman_to_devanagari(text)`

Convert Romanized to Devanagari.

```python
from nepalikit.transliterate import roman_to_devanagari

roman_to_devanagari("mero naam ram ho")
# "मेरो नाम राम हो"

roman_to_devanagari("nepal")
# "नेपाल"
```

### `devanagari_to_roman(text)`

Convert Devanagari to Romanized.

```python
from nepalikit.transliterate import devanagari_to_roman

devanagari_to_roman("मेरो नाम राम हो")
# "mero naam raam ho"

devanagari_to_roman("नेपाल")
# "nepaal"
```

## Classes

### `NepaliTransliterator`

Advanced transliteration with full mapping support.

```python
from nepalikit.transliterate import NepaliTransliterator

trans = NepaliTransliterator()

# Roman to Devanagari
devanagari = trans.roman_to_devanagari("nepal")
print(devanagari)  # "नेपाल"

# Devanagari to Roman
roman = trans.devanagari_to_roman("नेपाल")
print(roman)  # "nepaal"
```

## Supported Characters

### Roman to Devanagari

- **Vowels**: a, aa, i, ee, u, oo, e, ai, o, au
- **Consonants**: k, kh, g, gh, ng, ch, chh, j, jh, ny, t, th, d, dh, n, p, ph, b, bh, m, y, r, l, v, w, s, h
- **Ligatures**: ksha, tra, gya
- **Numbers**: 0-9

### Devanagari to Roman

- **All Devanagari vowels and consonants**
- **Vowel marks**
- **Dental/retroflex distinction**: Uses IAST diacritics (ṭa, ḍa, ṇa)

## Methods

### `NepaliTransliterator.roman_to_devanagari(text)`

Convert Romanized text to Devanagari.

**Parameters:**
- `text` (str): Romanized text

**Returns:** Devanagari text

### `NepaliTransliterator.devanagari_to_roman(text)`

Convert Devanagari text to Romanized.

**Parameters:**
- `text` (str): Devanagari text

**Returns:** Romanized text
