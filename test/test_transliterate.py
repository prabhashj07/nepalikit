import pytest

from nepalikit.transliterate import (
    NepaliTransliterator,
    devanagari_to_roman,
    roman_to_devanagari,
)


@pytest.fixture
def transliterator():
    return NepaliTransliterator()


def test_roman_to_devanagari_ka(transliterator):
    result = transliterator.roman_to_devanagari("ka")
    assert result == "का"


def test_roman_to_devanagari_ki(transliterator):
    result = transliterator.roman_to_devanagari("ki")
    assert result == "कि"


def test_roman_to_devanagari_ku(transliterator):
    result = transliterator.roman_to_devanagari("ku")
    assert result == "कु"


def test_roman_to_devanagari_nepal(transliterator):
    result = transliterator.roman_to_devanagari("nepal")
    assert "न" in result and "पा" in result and "ल" in result


def test_roman_to_devanagari_empty(transliterator):
    assert transliterator.roman_to_devanagari("") == ""


def test_roman_to_devanagari_none(transliterator):
    assert transliterator.roman_to_devanagari(None) is None


def test_devanagari_to_roman_ka(transliterator):
    result = transliterator.devanagari_to_roman("क")
    assert result == "ka"


def test_devanagari_to_roman_dental_vs_retroflex(transliterator):
    dental = transliterator.devanagari_to_roman("त")
    retroflex = transliterator.devanagari_to_roman("ट")
    assert dental != retroflex


def test_devanagari_to_roman_empty(transliterator):
    assert transliterator.devanagari_to_roman("") == ""


def test_devanagari_to_roman_none(transliterator):
    assert transliterator.devanagari_to_roman(None) is None


def test_devanagari_to_roman_nepal(transliterator):
    result = transliterator.devanagari_to_roman("नेपाल")
    assert isinstance(result, str)
    assert len(result) > 0


def test_roundtrip_basic(transliterator):
    original = "ka"
    dev = transliterator.roman_to_devanagari(original)
    roman = transliterator.devanagari_to_roman(dev)
    assert "ka" in roman.lower()


def test_convenience_roman_to_devanagari():
    result = roman_to_devanagari("ka")
    assert result == "का"


def test_convenience_devanagari_to_roman():
    result = devanagari_to_roman("क")
    assert result == "ka"


def test_roman_to_devanagari_numbers(transliterator):
    result = transliterator.roman_to_devanagari("123")
    assert "१" in result and "२" in result and "३" in result


def test_devanagari_to_roman_digits(transliterator):
    result = transliterator.devanagari_to_roman("१२३")
    assert "1" in result and "2" in result and "3" in result
