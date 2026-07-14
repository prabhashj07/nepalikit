# Complete NLP Pipeline

A full-featured example showing how to combine multiple NepaliKit modules for comprehensive Nepali text analysis.

## Pipeline Code

```python
from nepalikit.normalizer import normalize
from nepalikit.stemmer import stem_text
from nepalikit.pos_tagger import tag_pos
from nepalikit.number_extractor import extract_numbers
from nepalikit.manage_stopwords import remove_stopwords_from_text
from nepalikit.transliterate import devanagari_to_roman
from nepalikit.spell_checker import check_spelling

def analyze_nepali_text(text):
    """Complete NLP analysis of Nepali text."""
    # 1. Normalize
    normalized = normalize(text)

    # 2. Tokenize
    tokens = normalized.split()

    # 3. Remove stopwords
    filtered = remove_stopwords_from_text(normalized)

    # 4. Get POS tags
    pos_tags = tag_pos(tokens)

    # 5. Stem
    stemmed = stem_text(filtered)

    # 6. Extract numbers
    numbers = extract_numbers(text)

    # 7. Transliterate
    roman = devanagari_to_roman(text)

    return {
        'original': text,
        'normalized': normalized,
        'tokens': tokens,
        'pos_tags': pos_tags,
        'filtered': filtered,
        'stemmed': stemmed,
        'numbers': numbers,
        'roman': roman,
    }

# Example
text = "मैले २ लाख रुपैयाँमा किताब किनें।"
result = analyze_nepali_text(text)
for key, value in result.items():
    print(f"{key}: {value}")
```

## Output

```
original: मैले २ लाख रुपैयाँमा किताब किनें।
normalized: मैले २ लाख रुपैयाँमा किताब किनें।
tokens: ['मैले', '२', 'लाख', 'रुपैयाँमा', 'किताब', 'किनें।']
pos_tags: [('मैले', 'PRON'), ('२', 'N_NN'), ('लाख', 'N_NN'), ('रुपैयाँमा', 'N_NN'), ('किताब', 'N_NN'), ('किनें।', 'N_NN')]
filtered: २ रुपैयाँमा किताब किनें।
stemmed: २ रुपैयाँ किताब किनें।
numbers: [('२', 2), ('२ लाख', 200000)]
roman: maailae 2 laaakha raupaaiyaaanmaaa kaitaaaba kainaen
```
