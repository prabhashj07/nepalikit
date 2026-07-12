import pytest
from nepalikit.stemmer import NepaliStemmer, stem, stem_text


@pytest.fixture
def stemmer():
    return NepaliStemmer()


def test_stem_single_word(stemmer):
    result = stemmer.stem("नेपालमा")
    assert isinstance(result, str)
    assert len(result) <= len("नेपालमा")


def test_stem_removes_case_marker(stemmer):
    result = stemmer.stem("नेपालले")
    assert result == "नेपाल"


def test_stem_removes_possessive(stemmer):
    result = stemmer.stem("नेपालको")
    assert result == "नेपाल"


def test_stem_removes_locative(stemmer):
    result = stemmer.stem("नेपालमा")
    assert result == "नेपाल"


def test_stem_removes_instrumental(stemmer):
    result = stemmer.stem("नेपालबाट")
    assert result == "नेपाल"


def test_stem_removes_dative(stemmer):
    result = stemmer.stem("नेपाललाई")
    assert result == "नेपाल"


def test_stem_removes_plural(stemmer):
    result = stemmer.stem("किताहरू")
    assert result == "किता"


def test_stem_short_word_unchanged(stemmer):
    assert stemmer.stem("म") == "म"
    assert stemmer.stem("छ") == "छ"


def test_stem_empty_string(stemmer):
    assert stemmer.stem("") == ""


def test_stem_text(stemmer):
    result = stemmer.stem_text("नेपालमा किताहरू छन्")
    assert isinstance(result, str)
    assert len(result.split()) == 3


def test_stem_words(stemmer):
    words = ["नेपालमा", "किताहरू", "छन्"]
    result = stemmer.stem_words(words)
    assert isinstance(result, list)
    assert len(result) == 3


def test_convenience_stem():
    result = stem("नेपालका")
    assert result == "नेपाल"


def test_convenience_stem_text():
    result = stem_text("नेपालमा किताहरू")
    assert isinstance(result, str)


def test_stem_root_word_unchanged(stemmer):
    result = stemmer.stem("नेपाल")
    assert result == "नेपाल"


def test_stem_text_none(stemmer):
    assert stemmer.stem_text(None) is None


def test_stem_words_none(stemmer):
    assert stemmer.stem_words(None) == []


def test_stem_words_empty(stemmer):
    assert stemmer.stem_words([]) == []
