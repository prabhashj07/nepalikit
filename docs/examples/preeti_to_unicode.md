# Preeti to Unicode Conversion

The Preeti font is a popular typing font for Nepali used in the early days of Nepali computing. NepaliKit can convert Preeti-encoded text to Unicode.

## What is Preeti?

Preeti is a custom encoding for Devanagari characters, similar to how Wingdings encodes symbols. Each character in Preeti maps to a specific Devanagari letter, but the mapping is based on QWERTY keyboard positions.

## Conversion Example

```python
from nepalikit.transliterate import preeti_to_unicode

# Convert Preeti-encoded text to Unicode Devanagari
preeti_text = "h{ aahg hh ! ah$#"
unicode_text = preeti_to_unicode(preeti_text)
print(unicode_text)

# More examples
examples = [
    ("tUfuf", "नेपाल"),
    ("cGo", "अन्य"),
]

for preeti, expected in examples:
    result = preeti_to_unicode(preeti)
    print(f"{preeti} -> {result}")
```

## When to use Preeti conversion

- You have existing Nepali text in Preeti encoding
- You need to process legacy Nepali documents
- You want to normalize Preeti text to standard Unicode Devanagari
