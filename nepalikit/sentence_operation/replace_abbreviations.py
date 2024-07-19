import os
import regex as re
from nepalikit.sentence_operation.load_abbreviation import load_abbreviations

class AbbreviationReplacer:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'data'))  # Adjusted path to data directory
        self.abbreviations = load_abbreviations(data_dir)
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
        return '|'.join(abbr_patterns)

    def _replace_match(self, match):
        matched_text = match.group(0)
        for abbr, full_form in self.abbreviations.items():
            if matched_text.lower() == abbr.lower():
                return full_form
        return matched_text

    def replace_abbreviations(self, text: str) -> str:
        replaced_text = re.sub(self.pattern, self._replace_match, text, flags=re.UNICODE | re.IGNORECASE)
        return replaced_text

if __name__ == "__main__":
    # Example usage
    input_text = "उ.मा.वि. , प्रा."
    replacer = AbbreviationReplacer()
    replaced_text = replacer.replace_abbreviations(input_text)
    
    print("Original text:", input_text)
    print("Replaced text:", replaced_text)

