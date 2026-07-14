# POS Tagger API

## Overview

Dictionary-based part-of-speech tagger for Nepali text with 11 grammatical categories.

## Functions

### `tag_pos(tokens)`

Tag POS for a list of tokens.

```python
from nepalikit.pos_tagger import tag_pos

tokens = ["राम", "स्कूल", "जान्छ"]
tags = tag_pos(tokens)
print(tags)
# [("राम", "N_NN"), ("स्कूल", "N_NN"), ("जान्छ", "V_VM")]
```

## Classes

### `NepaliPOSTagger`

Advanced POS tagger with dictionary support.

```python
from nepalikit.pos_tagger import NepaliPOSTagger

tagger = NepaliPOSTagger()

# Tag tokens
tags = tagger.tag(["म", "घर", "जान्छु"])
print(tags)

# Tag text directly
tags = tagger.tag_text("म घर जान्छु")
print(tags)
```

## POS Tags

| Tag | Description | Example |
|-----|-------------|---------|
| `N_NN` | Common Noun | घर, किताब |
| `N_NNP` | Proper Noun | राम, काठमाडौं |
| `V_VM` | Verb | जान्छ, खान्छ |
| `ADJ` | Adjective | राम्रो, ठूलो |
| `ADV` | Adverb | धेरै, राम्रोसँग |
| `PRON` | Pronoun | म, तिमी, उ |
| `POSTP` | Postposition | मा, बाट, लाई |
| `CONJ` | Conjunction | र, तर, वा |
| `PART` | Particle | पनि, नै, त |
| `INTJ` | Interjection | अहो, ओ |
| `PUNC` | Punctuation | ।, , |

## Methods

### `NepaliPOSTagger.tag(tokens)`

Tag a list of tokens.

**Parameters:**
- `tokens` (list): List of string tokens

**Returns:** List of (token, tag) tuples

### `NepaliPOSTagger.tag_text(text)`

Tokenize and tag text.

**Parameters:**
- `text` (str): Input Nepali text

**Returns:** List of (token, tag) tuples
