import pytest
from nepalikit.spell_checker import (
    NepaliSpellChecker,
    check_spelling,
    suggest_corrections,
)


@pytest.fixture
def checker():
    return NepaliSpellChecker()


def test_check_known_word(checker):
    assert checker.check("नेपाल") is True


def test_check_unknown_word(checker):
    assert checker.check("xyzabc") is False


def test_suggest_known_word(checker):
    suggestions = checker.suggest("नेपाल")
    assert suggestions == ["नेपाल"]


def test_suggest_misspelled(checker):
    suggestions = checker.suggest("नेपाली", max_distance=2)
    assert isinstance(suggestions, list)


def test_suggest_empty_string(checker):
    assert checker.suggest("") == []


def test_add_word(checker):
    checker.add_word("अनुकूल")
    assert checker.check("अनुकूल") is True


def test_correct_text(checker):
    result = checker.correct("नेपाल एक देश हो")
    assert isinstance(result, str)


def test_correct_no_false_positives(checker):
    text = "नेपाल"
    result = checker.correct(text)
    assert result == text


def test_convenience_check():
    assert check_spelling("नेपाल") is True
    assert check_spelling("xyzabc") is False


def test_convenience_suggest():
    result = suggest_corrections("नेपाल")
    assert isinstance(result, list)


def test_edit_distance_same(checker):
    assert checker._edit_distance("abc", "abc", 3) == 0


def test_edit_distance_one_substitution(checker):
    assert checker._edit_distance("abc", "axc", 3) == 1


def test_edit_distance_one_insertion(checker):
    assert checker._edit_distance("abc", "abxc", 3) == 1


def test_edit_distance_one_deletion(checker):
    assert checker._edit_distance("abc", "ac", 3) == 1


def test_edit_distance_exceeds_max(checker):
    assert checker._edit_distance("abc", "xyz", 1) > 1
