# Transliteration API

## Overview

Character-level transliteration between Romanized and Devanagari Nepali, including Preeti font conversion.

## Functions

### `roman_to_devanagari(text)`

Convert Romanized to Devanagari. Handles exception words (common proper nouns) automatically.

```python
from nepalikit.transliterate import roman_to_devanagari

roman_to_devanagari("namaste")
# "नमस्ते"

roman_to_devanagari("kathmandu")
# "काठमाडौं"

roman_to_devanagari("facebook")
# "फेसबुक"
```

### `devanagari_to_roman(text)`

Convert Devanagari to Romanized.

```python
from nepalikit.transliterate import devanagari_to_roman

devanagari_to_roman("नमस्ते।")
# "namasatae"

devanagari_to_roman("नेपाल")
# "naepaaala"
```

### `preeti_to_unicode(text)`

Convert Preeti font encoded text to Unicode Devanagari.

```python
from nepalikit.transliterate import preeti_to_unicode

preeti_to_unicode("g]kfn")  # "नेपाल"
```

## Classes

### `NepaliTransliterator`

Advanced transliteration with full mapping support and exception words.

```python
from nepalikit.transliterate import NepaliTransliterator

trans = NepaliTransliterator()

# Roman to Devanagari
devanagari = trans.roman_to_devanagari("namaste")
print(devanagari)  # "नमस्ते"

# Devanagari to Roman
roman = trans.devanagari_to_roman("नेपाल")
print(roman)  # "naepaaala"
```

### `PreetiConverter`

Convert Preeti font encoded text to Unicode Devanagari.

```python
from nepalikit.transliterate import PreetiConverter

converter = PreetiConverter()
unicode_text = converter.convert("g]kfn")
print(unicode_text)  # "नेपाल"
```

## Supported Characters

### Roman to Devanagari

- **Vowels**: a, aa, i, ee, u, oo, e, ai, o, au
- **Consonants**: k, kh, g, gh, ng, ch, chh, j, jh, ny, t, th, d, dh, n, p, ph, b, bh, m, y, r, l, v, w, s, h
- **Ligatures**: ksha, tra, gya
- **Numbers**: 0-9

### Exception Words

Common proper nouns are handled automatically:
- **Cities**: kathmandu, patan, bhaktapur, pokhara, chitwan, dhulikhel, nagarkot, janakpur, biratnagar, nepalganj
- **Common words**: namaste, dhanyabad, swagat
- **Deities**: krishna, ganesh, ram, sita, guru
- **Tech brands**: facebook, youtube, google, twitter, whatsapp, instagram

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

### `PreetiConverter.convert(text)`

Convert Preeti-encoded text to Unicode Devanagari.

**Parameters:**
- `text` (str): Preeti-encoded text

**Returns:** Unicode Devanagari text
