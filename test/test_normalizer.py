import pytest

from nepalikit.normalizer import NepaliNormalizer, detect_script, normalize


@pytest.fixture
def normalizer():
    return NepaliNormalizer()


def test_normalize_basic(normalizer):
    text = "नेपाल एक सुन्दर देश हो"
    result = normalizer.normalize(text)
    assert result == "नेपाल एक सुन्दर देश हो"


def test_normalize_strips_zwnj(normalizer):
    text = "नेपाल\u200cएक"
    result = normalizer.normalize(text)
    assert "\u200c" not in result
    assert result == "नेपालएक"


def test_normalize_strips_zwj(normalizer):
    text = "नेपाल\u200dएक"
    result = normalizer.normalize(text)
    assert "\u200d" not in result


def test_normalize_collapses_whitespace(normalizer):
    text = "नेपाल    एक    सुन्दर"
    result = normalizer.normalize(text)
    assert result == "नेपाल एक सुन्दर"


def test_normalize_empty_string(normalizer):
    assert normalizer.normalize("") == ""


def test_normalize_none(normalizer):
    assert normalizer.normalize(None) is None


def test_detect_script_devanagari(normalizer):
    assert normalizer.detect_script("नेपाल एक देश हो") == "devanagari"


def test_detect_script_latin(normalizer):
    assert normalizer.detect_script("Hello World") == "latin"


def test_detect_script_mixed(normalizer):
    assert normalizer.detect_script("नेपाल Nepal") == "mixed"


def test_detect_script_empty(normalizer):
    assert normalizer.detect_script("") == "other"


def test_detect_script_numbers(normalizer):
    assert normalizer.detect_script("12345") == "other"


def test_strip_zwnj(normalizer):
    result = normalizer.strip_zwnj("abc\u200cdef\u200dghi")
    assert result == "abcdefghi"


def test_strip_zwnj_none(normalizer):
    assert normalizer.strip_zwnj(None) is None


def test_strip_control_chars_none(normalizer):
    assert normalizer.strip_control_chars(None) is None


def test_strip_control_chars(normalizer):
    result = normalizer.strip_control_chars("hello\x00world")
    assert "hello" in result
    assert "world" in result


def test_normalize_unicode_form(normalizer):
    result = normalizer.normalize_unicode("नेपाल", form="NFC")
    assert result == "नेपाल"


def test_convenience_normalize():
    result = normalize("नेपाल")
    assert result == "नेपाल"


def test_convenience_detect_script():
    assert detect_script("नेपाल") == "devanagari"
    assert detect_script("hello") == "latin"
