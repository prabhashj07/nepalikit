import os
import shutil
import tempfile

from nepalikit.sentence_operation.load_abbreviation import load_abbreviations
from nepalikit.sentence_operation.replace_abbreviations import AbbreviationReplacer


def test_load_abbreviations_empty_file():
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "abbreviation.txt"), "w", encoding="utf-8") as f:
        f.write("")
    result = load_abbreviations(d)
    assert result == {}
    shutil.rmtree(d)


def test_load_abbreviations_value_with_colons():
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "abbreviation.txt"), "w", encoding="utf-8") as f:
        f.write("श्री.:श्रीमान्:उपाधि")
    result = load_abbreviations(d)
    assert "श्री." in result
    assert result["श्री."] == "श्रीमान्:उपाधि"
    shutil.rmtree(d)


def test_load_abbreviations_nonexistent_file():
    result = load_abbreviations("/nonexistent/path/")
    assert result == {}


def test_abbrev_replacer_empty_text():
    replacer = AbbreviationReplacer()
    assert replacer.replace_abbreviations("") == ""


def test_abbrev_replacer_no_abbreviations():
    replacer = AbbreviationReplacer()
    assert replacer.replace_abbreviations("नेपाल एक देश हो") == "नेपाल एक देश हो"
