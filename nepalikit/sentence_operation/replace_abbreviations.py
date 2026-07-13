import re


class AbbreviationReplacer:
    def __init__(self):
        self.abbreviations = {}
        self.pattern = self._generate_pattern()

    def _generate_pattern(self):
        abbr_patterns = [re.escape(abbr) for abbr in self.abbreviations]
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
        return re.sub(self.pattern, self._replace_match, text, flags=re.UNICODE | re.IGNORECASE)
