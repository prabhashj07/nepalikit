# Number Extraction

Parse Devanagari digits and Nepali number words (written out) into Python integers.

## Features

- Parse Devanagari digits (`०-९`) to integers
- Parse Nepali number words (एक, दुई, सय, हजार, लाख, करोड)
- Support for combined expressions (e.g., "२ लाख ५ हजार")
- Indian-style comma handling in Devanagari numerals

## Basic Usage

```python
from nepalikit.number_extractor import extract_numbers, convert_number

# Extract numbers from text
text = "मैले २ लाख ५ हजार रुपैयाँ तिरें।"
numbers = extract_numbers(text)
print(numbers)  # [('२ लाख ५ हजार', 205000)]

# Convert individual expressions
print(convert_number("पचास"))        # 50
print(convert_number("१,२३,४५६"))   # 123456
print(convert_number("२.५ लाख"))     # 250000
```

## Supported Scales

| Word | Value |
|------|-------|
| सय / सयौं | 100 |
| हजार | 1,000 |
| लाख | 100,000 |
| करोड | 10,000,000 |
