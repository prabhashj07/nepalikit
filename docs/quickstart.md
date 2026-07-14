# Quick Start

## Import NepaliKit

```python
import nepalikit as nk
```

## Tokenization

```python
from nepalikit.tokenization import Tokenizer

tokenizer = Tokenizer()
tokens = tokenizer.tokenize("म घर जाँदै छु।", level='word')
print(tokens)  # ['म', 'घर', 'जाँदै', 'छु']
```

## Text Preprocessing

```python
from nepalikit.preprocessing import TextProcessor

processor = TextProcessor()
clean = processor.remove_html_tags("<p>राम्रो दिन</p>")
print(clean)
```

## Stemming

```python
from nepalikit.stemmer import stem, snowball_stem

# Built-in stemmer
root = stem("नेपालमा")
print(root)  # "नेपाल"

# Snowball stemmer (requires: pip install snowballstemmer)
root = snowball_stem("नेपालमा")
print(root)  # "नेपाल"
```

## Normalization

```python
from nepalikit.normalizer import normalize

normalized = normalize("म  नाम   राम हो")
print(normalized)  # "म नाम राम हो"
```

## Script Detection

```python
from nepalikit.normalizer import detect_script

script = detect_script("मेरो नाम राम हो")
print(script)  # "devanagari"
```

## Number Extraction

```python
from nepalikit.number_extractor import extract_numbers

numbers = extract_numbers("मैले २ लाख ५ हजार रुपैयाँ तिरें")
print(numbers)  # [('२ लाख ५ हजार', 205000)]
```

## Stopword Removal

```python
from nepalikit.manage_stopwords import remove_stopwords_from_text

filtered = remove_stopwords_from_text("म घर जाँदै छु")
print(filtered)  # "घर जाँदै"
```

## POS Tagging

```python
from nepalikit.pos_tagger import tag_pos

tokens = ["राम", "स्कूल", "जान्छ"]
tags = tag_pos(tokens)
print(tags)  # [("राम", "N_NN"), ("स्कूल", "N_NN"), ("जान्छ", "V_VM")]
```

## Spell Checking

```python
from nepalikit.spell_checker import check_spelling, suggest_corrections

# Check if word is correct
check_spelling("नेपाल")  # True

# Get suggestions for misspelled word
suggest_corrections("नेपालक")  # ["नेपालको", "नेपालका"]
```

## Transliteration

```python
from nepalikit.transliterate import roman_to_devanagari, devanagari_to_roman

# Roman to Devanagari
devanagari = roman_to_devanagari("namaste")
print(devanagari)  # "नमस्ते"

# Devanagari to Roman
roman = devanagari_to_roman("नमस्ते।")
print(roman)  # "namasatae"
```

## Preeti to Unicode

```python
from nepalikit.transliterate import preeti_to_unicode

# Convert Preeti font text to Unicode Devanagari
unicode_text = preeti_to_unicode("g]kfn")
print(unicode_text)  # "नेपाल"
```

## Complete Example

```python
from nepalikit.stemmer import stem_text
from nepalikit.normalizer import normalize, detect_script
from nepalikit.number_extractor import extract_numbers
from nepalikit.manage_stopwords import remove_stopwords_from_text

# Sample text
text = "नेपालको राजधानी काठमाडौं हो। म  स्कूल जान्छु।"

# Normalize
normalized = normalize(text)
print(f"Normalized: {normalized}")

# Detect script
script = detect_script(text)
print(f"Script: {script}")

# Remove stopwords
filtered = remove_stopwords_from_text(normalized)
print(f"Filtered: {filtered}")

# Stem
stemmed = stem_text(filtered)
print(f"Stemmed: {stemmed}")
```
