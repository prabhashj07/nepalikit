# POS Tagger API

## Overview

Part-of-speech tagging for Nepali text with two taggers:

1. **Dictionary Tagger** — Fast, rule-based with 11 grammatical categories
2. **ML Tagger** — Context-aware using n-gram statistics and Viterbi decoding

## Dictionary Tagger

### Functions

#### `tag_pos(tokens)`

Tag POS for a list of tokens using dictionary rules.

```python
from nepalikit.pos_tagger import tag_pos

tokens = ["राम", "स्कूल", "जान्छ"]
tags = tag_pos(tokens)
print(tags)
# [("राम", "N_NN"), ("स्कूल", "N_NN"), ("जान्छ", "V_VM")]
```

### Classes

#### `NepaliPOSTagger`

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

## ML Tagger (New in v1.0.6)

Context-aware POS tagger using n-gram statistics and Viterbi decoding.

### Features

- **Bigram transition model** — considers tag context
- **Emission probabilities** — word-tag likelihood
- **Suffix rules** — handles unknown words
- **Viterbi decoding** — globally optimal tag sequence
- **Zero dependencies** — pure Python, no ML libraries required

### Classes

#### `MLPOSTagger`

```python
from nepalikit.pos_tagger import MLPOSTagger

tagger = MLPOSTagger()

# Tag tokens
tags = tagger.tag(["म", "नेपाली", "हुँ"])
print(tags)
# [("म", "PRON"), ("नेपाली", "N_NNP"), ("हुँ", "V_VM")]

# Tag text directly
tags = tagger.tag_text("म नेपालमा बस्छु र राम्रो काम गर्छु")
for word, tag in tags:
    print(f"{word} -> {tag}")
```

### Functions

#### `ml_tag_pos(tokens)`

Convenience function for ML POS tagging.

```python
from nepalikit.pos_tagger import ml_tag_pos

tags = ml_tag_pos(["म", "छु"])
print(tags)
# [("म", "PRON"), ("छु", "V_VM")]
```

#### `ml_tag_text(text)`

Convenience function for tagging text.

```python
from nepalikit.pos_tagger import ml_tag_text

tags = ml_tag_text("राम भात खान्छ")
print(tags)
# [("राम", "N_NNP"), ("भात", "N_NN"), ("खान्छ", "V_VM")]
```

### How It Works

The ML tagger uses the Viterbi algorithm to find the most probable sequence of POS tags for a sentence:

1. **Transition probabilities** — probability of tag B following tag A
2. **Emission probabilities** — probability of word W given tag T
3. **Context patterns** — boost common grammatical sequences (e.g., `PRON POSTP V_VM`)
4. **Suffix rules** — fallback for unknown words (e.g., `हरू` → `N_NN`)

### Comparison with Dictionary Tagger

| Feature | Dictionary | ML |
|---------|-----------|-----|
| Speed | Faster | Slightly slower |
| Context | None | Bigram transitions |
| Unknown words | Suffix rules only | Suffix + emission fallback |
| Accuracy | Good for known words | Better for full sentences |

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
| `PUNC` | Punctuation | । , |

## Methods

### `NepaliPOSTagger.tag(tokens)`

Tag a list of tokens using dictionary rules.

**Parameters:**
- `tokens` (list): List of string tokens

**Returns:** List of (token, tag) tuples

### `NepaliPOSTagger.tag_text(text)`

Tokenize and tag text using dictionary rules.

**Parameters:**
- `text` (str): Input Nepali text

**Returns:** List of (token, tag) tuples

### `MLPOSTagger.tag(tokens)`

Tag a list of tokens using Viterbi decoding.

**Parameters:**
- `tokens` (list): List of string tokens

**Returns:** List of (token, tag) tuples

### `MLPOSTagger.tag_text(text)`

Tokenize and tag text using Viterbi decoding.

**Parameters:**
- `text` (str): Input Nepali text

**Returns:** List of (token, tag) tuples
