# POS Tagging

The POS tagger assigns part-of-speech labels to Nepali words using a dictionary-based approach with rule-based fallback.

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

## Basic Usage

```python
from nepalikit.pos_tagger import tag_pos

tokens = ["राम", "स्कूल", "जान्छ"]
tags = tag_pos(tokens)
print(tags)
# [("राम", "N_NN"), ("स्कूल", "N_NN"), ("जान्छ", "V_VM")]
```

For unknown words, the tagger assigns `N_NN` (common noun) as the default fallback tag.
