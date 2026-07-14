import os
import shutil
import tempfile

from nepalikit.manage_stopwords.manage_stopwords import (
    add_stopwords,
    get_stopwords,
    is_stopword,
    load_stopwords,
    remove_custom_stopwords,
    remove_stopwords_from_text,
)


def test_load_stopwords_nonexistent_directory():
    result = load_stopwords("/nonexistent/dir/")
    assert result == []


def test_load_stopwords_empty_file():
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "stop.txt"), "w", encoding="utf-8") as f:
        f.write("")
    result = load_stopwords(d)
    assert result == []
    shutil.rmtree(d)


def test_load_stopwords_filters_non_txt():
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "stop.csv"), "w", encoding="utf-8") as f:
        f.write("should_not_appear")
    result = load_stopwords(d)
    assert result == []
    shutil.rmtree(d)


def test_get_stopwords_returns_set():
    result = get_stopwords()
    assert isinstance(result, set)
    assert len(result) > 300


def test_get_stopwords_common_words():
    stopwords = get_stopwords()
    for word in ["र", "मा", "को", "ले", "लाई", "छ", "हो", "पनि"]:
        assert word in stopwords


def test_is_stopword():
    assert is_stopword("र") is True
    assert is_stopword("मा") is True
    assert is_stopword("नेपाल") is False


def test_add_stopwords():
    add_stopwords(["नेपाल", "काठमाडौं"])
    assert is_stopword("नेपाल") is True
    assert is_stopword("काठमाडौं") is True
    remove_custom_stopwords(["नेपाल", "काठमाडौं"])


def test_add_stopwords_string():
    add_stopwords("परीक्षण")
    assert is_stopword("परीक्षण") is True
    remove_custom_stopwords("परीक्षण")


def test_remove_custom_stopwords():
    add_stopwords(["अस्थायी"])
    assert is_stopword("अस्थायी") is True
    remove_custom_stopwords(["अस्थायी"])
    assert is_stopword("अस्थायी") is False


def test_remove_custom_stopwords_cannot_remove_default():
    assert is_stopword("र") is True
    remove_custom_stopwords(["र"])
    assert is_stopword("र") is True


def test_remove_stopwords_from_text():
    result = remove_stopwords_from_text("म घर जाँदै छु")
    assert "घर" in result
    assert "जाँदै" in result
    assert "म" not in result
    assert "छु" not in result


def test_remove_stopwords_from_text_empty():
    assert remove_stopwords_from_text("") == ""
    assert remove_stopwords_from_text("   ") == "   "


def test_remove_stopwords_from_text_none_stopwords():
    result = remove_stopwords_from_text("म घर छु", stopwords=None)
    assert "घर" in result


def test_remove_stopwords_from_text_custom_stopwords():
    result = remove_stopwords_from_text("म घर जाँदै छु", stopwords={"घर"})
    assert "घर" not in result
    assert "म" in result
