# Lemmatization

NepaliKit provides dictionary-based lemmatization for Nepali words, mapping inflected forms to their canonical dictionary form.

## What is Lemmatization?

Unlike stemming (which blindly strips suffixes), lemmatization uses a dictionary to find the actual root form. For example:
- `गर्छन्` → `गर्नु` (infinitive form, not `गर्`)
- `किताहरू` → `किता` (singular form)
- `मैले` → `म` (base pronoun)

## Basic Usage

```python
from nepalikit.lemmatizer import NepaliLemmatizer, lemmatize, lemmatize_text

# Single word
print(lemmatize("गर्छन्"))  # "गर्नु"
print(lemmatize("किताहरू"))  # "किता"
print(lemmatize("मैले"))     # "म"

# Full text
text = "मैले किताहरू पढेको छु"
print(lemmatize_text(text))  # "म किता पढ्नु छु"
```

## Lemmatizer vs Stemmer

| Input | Stemmer | Lemmatizer |
|-------|---------|------------|
| `गर्छन्` | `गर्` | `गर्नु` |
| `किताहरू` | `कित` | `किता` |
| `मैले` | `मै` | `म` |
| `पढेको` | `पढ` | `पढ्नु` |

The stemmer strips suffixes blindly. The lemmatizer returns the actual dictionary form.

## Features

- Dictionary-based lookup for nouns, verbs, pronouns, adjectives
- Handles case markers (ले, को, मा, बाट, लाई)
- Handles plural forms (हरू)
- Handles verb conjugations (present, past, negative)
- Rule-based fallback for unknown words
- Zero dependencies (Python stdlib only)

See the [API reference](../api/lemmatizer.md) for full details.
