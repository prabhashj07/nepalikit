# Number Extractor API

## Overview

Extract and convert Nepali numeric expressions to integers.

## Functions

### `extract_numbers(text)`

Extract all number expressions from text.

```python
from nepalikit.number_extractor import extract_numbers

extract_numbers("मैले २ लाख ५ हजार रुपैयाँ तिरें")
# [('२ लाख ५ हजार', 205000)]

extract_numbers("उनको उमेर २५ वर्ष छ")
# [('२५', 25)]
```

### `convert_number(text)`

Convert a single expression to integer.

```python
from nepalikit.number_extractor import convert_number

convert_number("२ लाख ५ हजार")  # 205000
convert_number("पचास")          # 50
convert_number("१,२३,४५६")     # 123456
convert_number("२.५ लाख")      # 250000
```

## Classes

### `NepaliNumberExtractor`

Advanced extraction with more options.

```python
from nepalikit.number_extractor import NepaliNumberExtractor

extractor = NepaliNumberExtractor()
numbers = extractor.extract("मैले २ लाख तिरें")
print(numbers)

value = extractor.convert("पचास")
print(value)  # 50
```

## Supported Formats

- **Devanagari digits**: ०-९
- **Number words**: एक, दुई, तीन, etc. (0-99)
- **Multipliers**: सय, हजार, लाख, करोड, अर्ब, खर्ब
- **Compound expressions**: २ लाख ५ हजार
- **Decimal scales**: २.५ लाख = 250000
- **Comma-separated**: १,२३,४५६ = 123456

## Methods

### `NepaliNumberExtractor.extract(text)`

Find all number expressions in text.

**Parameters:**
- `text` (str): Input text

**Returns:** List of (expression, value) tuples

### `NepaliNumberExtractor.convert(text)`

Convert a Nepali number expression to integer.

**Parameters:**
- `text` (str): Nepali number expression

**Returns:** Integer value or None
