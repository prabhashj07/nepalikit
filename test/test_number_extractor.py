import pytest

from nepalikit.number_extractor import (
    NepaliNumberExtractor,
    convert_number,
    extract_numbers,
)


@pytest.fixture
def extractor():
    return NepaliNumberExtractor()


def test_convert_devanagari_digits(extractor):
    assert extractor.convert("१२३") == 123


def test_convert_zero(extractor):
    assert extractor.convert("०") == 0


def test_convert_number_word(extractor):
    assert extractor.convert("एक") == 1


def test_convert_ten(extractor):
    assert extractor.convert("दस") == 10


def test_convert_hundred(extractor):
    assert extractor.convert("सय") == 100


def test_convert_thousand(extractor):
    assert extractor.convert("हजार") == 1000


def test_convert_lakh(extractor):
    assert extractor.convert("लाख") == 100000


def test_convert_zero_word(extractor):
    assert extractor.convert("शून्य") == 0


def test_convert_empty_string(extractor):
    assert extractor.convert("") is None


def test_convert_none(extractor):
    assert extractor.convert(None) is None


def test_extract_devanagari_numbers(extractor):
    results = extractor.extract("मा ५० किताब छ")
    assert len(results) >= 1
    assert any(v == 50 for _, v in results)


def test_extract_word_numbers(extractor):
    results = extractor.extract("एक दुई तीन")
    assert len(results) >= 1


def test_extract_empty_text(extractor):
    assert extractor.extract("") == []


def test_convenience_extract():
    results = extract_numbers("१०० मानिस")
    assert isinstance(results, list)


def test_convenience_convert():
    assert convert_number("५००") == 500


def test_devanagari_multi_digit(extractor):
    assert extractor.convert("४२") == 42
    assert extractor.convert("१०००") == 1000


def test_convert_compound(extractor):
    assert extractor.convert("२ लाख ५ हजार") == 205000


def test_convert_comma_separated(extractor):
    assert extractor.convert("१,२३,४५६") == 123456


def test_convert_decimal_scale(extractor):
    assert extractor.convert("२.५ लाख") == 250000


def test_convert_teens(extractor):
    assert extractor.convert("एघार") == 11
    assert extractor.convert("बाह्र") == 12
    assert extractor.convert("उन्नाइस") == 19


def test_convert_twenties(extractor):
    assert extractor.convert("एक्काइस") == 21
    assert extractor.convert("चौबीस") == 24
    assert extractor.convert("उनन्तिस") == 29


def test_convert_kharba(extractor):
    assert extractor.convert("१ खर्ब") == 100000000000


def test_extract_multiple_in_text(extractor):
    text = "मसँग १ लाख छ र उसँग ५ हजार"
    results = extractor.extract(text)
    assert len(results) >= 2
