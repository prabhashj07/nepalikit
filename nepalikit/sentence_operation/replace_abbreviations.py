import os
import re
from nepalikit.sentence_operation.load_abbreviation import load_abbreviations


class AbbreviationReplacer:
    def __init__(self):
        self.abbreviations = {}
        self.pattern = self._generate_pattern()

    def _generate_pattern(self):
        abbr_patterns = []
        for abbr in self.abbreviations.keys():
            clean_abbr = abbr.replace('.', '').replace(' ', '')
            if clean_abbr.count('.') == 2:  # x.x.x.
                pattern = r'\b{}\b'.format(re.escape(abbr))
            elif clean_abbr.count('.') == 1:  # x.x.
                pattern = r'\b{}\b'.format(re.escape(abbr))
            elif clean_abbr.count('.') == 0:  # x.
                pattern = r'\b{}\b'.format(re.escape(abbr))
            abbr_patterns.append(pattern)
        return '|'.join(abbr_patterns) if abbr_patterns else None

    def _replace_match(self, match):
        matched_text = match.group(0)
        for abbr, full_form in self.abbreviations.items():
            if matched_text.lower() == abbr.lower():
                return full_form
        return matched_text

    def replace_abbreviations(self, text: str) -> str:
        if not self.pattern:
            return text
        replaced_text = re.sub(self.pattern, self._replace_match, text, flags=re.UNICODE | re.IGNORECASE)
        return replaced_text

if __name__ == "__main__":
    # Example usage
    input_text = "उ.मा.वि. , प्रा."
    replacer = AbbreviationReplacer()
    replaced_text = replacer.replace_abbreviations(input_text)
    
    print("Original text:", input_text)
    print("Replaced text:", replaced_text)

