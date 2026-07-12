# Basic Usage Examples

## Text Processing Pipeline

```python
from nepalikit.stemmer import stem_text
from nepalikit.normalizer import normalize, detect_script
from nepalikit.number_extractor import extract_numbers
from nepalikit.manage_stopwords import remove_stopwords_from_text
from nepalikit.pos_tagger import tag_pos

def process_nepali_text(text):
    # Normalize
    normalized = normalize(text)
    
    # Detect script
    script = detect_script(text)
    
    # Remove stopwords
    filtered = remove_stopwords_from_text(normalized)
    
    # Stem
    stemmed = stem_text(filtered)
    
    return {
        'normalized': normalized,
        'script': script,
        'filtered': filtered,
        'stemmed': stemmed
    }

# Example
text = "नेपालको राजधानी काठमाडौं हो।"
result = process_nepali_text(text)
print(result)
```

## Sentiment Analysis Prep

```python
from nepalikit.normalizer import normalize
from nepalikit.pos_tagger import tag_pos
from nepalikit.manage_stopwords import remove_stopwords_from_text

def prepare_for_sentiment(text):
    # Normalize
    normalized = normalize(text)
    
    # Tokenize
    tokens = normalized.split()
    
    # Remove stopwords
    filtered = remove_stopwords_from_text(normalized)
    
    # Get POS tags
    tags = tag_pos(tokens)
    
    return {
        'normalized': normalized,
        'tokens': tokens,
        'filtered': filtered,
        'pos_tags': tags
    }

text = "यो फिल्म धेरै राम्रो छ।"
result = prepare_for_sentiment(text)
print(result)
```

## Number Extraction Example

```python
from nepalikit.number_extractor import extract_numbers, convert_number

# Extract numbers from text
text = "मैले २ लाख ५ हजार रुपैयाँ तिरें।"
numbers = extract_numbers(text)
print(numbers)  # [('२ लाख ५ हजार', 205000)]

# Convert specific expressions
print(convert_number("पचास"))        # 50
print(convert_number("१,२३,४५६"))   # 123456
print(convert_number("२.५ लाख"))    # 250000
```

## Spell Checking Example

```python
from nepalikit.spell_checker import check_spelling, suggest_corrections

# Check spelling
words = ["नेपाल", "राम्रो", "नेपालक"]
for word in words:
    is_correct = check_spelling(word)
    print(f"{word}: {'✓' if is_correct else '✗'}")

# Get suggestions
suggestions = suggest_corrections("नेपालक")
print(f"Suggestions: {suggestions}")
```

## Transliteration Example

```python
from nepalikit.transliterate import roman_to_devanagari, devanagari_to_roman

# Roman to Devanagari
roman_text = "mero naam ram ho"
devanagari = roman_to_devanagari(roman_text)
print(f"Roman: {roman_text}")
print(f"Devanagari: {devanagari}")

# Devanagari to Roman
devanagari_text = "नेपालको राजधानी काठमाडौं हो"
roman = devanagari_to_roman(devanagari_text)
print(f"Devanagari: {devanagari_text}")
print(f"Roman: {roman}")
```

## POS Tagging Example

```python
from nepalikit.pos_tagger import tag_pos

# Tag a sentence
text = "रामले किताब पढ्छ।"
tokens = text.split()
tags = tag_pos(tokens)

for token, tag in tags:
    print(f"{token}: {tag}")
```

## Complete NLP Pipeline

```python
from nepalikit.normalizer import normalize, detect_script
from nepalikit.stemmer import stem, stem_text
from nepalikit.number_extractor import extract_numbers
from nepalikit.manage_stopwords import remove_stopwords_from_text
from nepalikit.pos_tagger import tag_pos
from nepalikit.spell_checker import check_spelling
from nepalikit.transliterate import devanagari_to_roman

def analyze_nepali_text(text):
    """Complete NLP analysis of Nepali text."""
    
    # 1. Normalize
    normalized = normalize(text)
    
    # 2. Detect script
    script = detect_script(text)
    
    # 3. Tokenize
    tokens = normalized.split()
    
    # 4. Remove stopwords
    filtered = remove_stopwords_from_text(normalized)
    filtered_tokens = filtered.split()
    
    # 5. POS tagging
    pos_tags = tag_pos(tokens)
    
    # 6. Stem
    stemmed = stem_text(filtered)
    
    # 7. Extract numbers
    numbers = extract_numbers(text)
    
    # 8. Transliterate to Roman
    roman = devanagari_to_roman(text)
    
    return {
        'original': text,
        'normalized': normalized,
        'script': script,
        'tokens': tokens,
        'filtered': filtered,
        'pos_tags': pos_tags,
        'stemmed': stemmed,
        'numbers': numbers,
        'roman': roman
    }

# Example usage
text = "मैले २ लाख रुपैयाँमा किताब किनें।"
result = analyze_nepali_text(text)
for key, value in result.items():
    print(f"{key}: {value}")
```
