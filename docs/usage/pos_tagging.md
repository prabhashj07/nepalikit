# POS Tagging

The POS tagger assigns part-of-speech labels to Nepali words using either a dictionary-based approach or an ML-based approach with n-gram statistics and Viterbi decoding.

## Supported Tags

| Tag | Category | Example |
|-----|----------|---------|
| N_NN | Common Noun | घर, मान्छे |
| N_NNP | Proper Noun | राम, नेपाल |
| V_VM | Main Verb | जान्छ, खान्छ |
| ADJ | Adjective | राम्रो, ठूलो |
| ADV | Adverb | छिटो, धेरै |
| POSTP | Postposition | मा, बाट, को |
| CONJ | Coordinating Conjunction | र, तर |
| PRON | Pronoun | म, तिमी, हामी |
| PART | Particle | पनि, नै, मात्र |
| INTJ | Interjection | अहो, वाह |
| PUNC | Punctuation | ।, ?, ! |

## Dictionary Tagger

Fast, rule-based tagging using a dictionary of 2000+ words.

```python
from nepalikit.pos_tagger import tag_pos

tokens = ["राम", "स्कूल", "जान्छ"]
tags = tag_pos(tokens)
print(tags)
# [("राम", "N_NN"), ("स्कूल", "N_NN"), ("जान्छ", "V_VM")]
```

For unknown words, the tagger assigns `N_NN` (common noun) as the default fallback tag.

## ML Tagger (New in v1.0.6)

Context-aware tagging using n-gram statistics and Viterbi decoding.

```python
from nepalikit.pos_tagger import MLPOSTagger

tagger = MLPOSTagger()

# Tag a sentence
tags = tagger.tag_text("म नेपाली हुँ")
for word, tag in tags:
    print(f"{word} -> {tag}")
```

Output:

```
म -> PRON
नेपाली -> N_NNP
हुँ -> V_VM
```

### How It Works

The ML tagger uses the Viterbi algorithm to find the most probable sequence of POS tags for a sentence:

1. **Transition probabilities** — probability of tag B following tag A
2. **Emission probabilities** — probability of word W given tag T
3. **Context patterns** — boost common grammatical sequences
4. **Suffix rules** — fallback for unknown words

### When to Use Which

| Feature | Dictionary | ML |
|---------|-----------|-----|
| Speed | Faster | Slightly slower |
| Context | None | Bigram transitions |
| Unknown words | Suffix rules only | Suffix + emission fallback |
| Accuracy | Good for known words | Better for full sentences |

### Convenience Functions

```python
from nepalikit.pos_tagger import ml_tag_pos, ml_tag_text

# Tag tokens
tags = ml_tag_pos(["म", "छु"])
print(tags)

# Tag text
tags = ml_tag_text("राम भात खान्छ")
print(tags)
```
