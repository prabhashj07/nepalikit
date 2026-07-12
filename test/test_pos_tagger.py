import pytest
from nepalikit.pos_tagger import NepaliPOSTagger, tag_pos


@pytest.fixture
def tagger():
    return NepaliPOSTagger()


def test_tag_noun(tagger):
    result = tagger.tag(["किताब"])
    assert result == [("किताब", "N_NN")]


def test_tag_pronoun(tagger):
    result = tagger.tag(["म"])
    assert result == [("म", "PRON")]


def test_tag_postposition(tagger):
    result = tagger.tag(["मा"])
    assert result == [("मा", "POSTP")]


def test_tag_conjunction(tagger):
    result = tagger.tag(["र"])
    assert result == [("र", "CONJ")]


def test_tag_particle(tagger):
    result = tagger.tag(["पनि"])
    assert result == [("पनि", "PART")]


def test_tag_verb(tagger):
    result = tagger.tag(["छन्"])
    assert result == [("छन्", "V_VM")]


def test_tag_punctuation(tagger):
    result = tagger.tag(["।"])
    assert result == [("।", "PUNC")]


def test_tag_proper_noun(tagger):
    result = tagger.tag(["नेपाल"])
    tag = result[0][1]
    assert tag in ("N_NN", "N_NNP")


def test_tag_text(tagger):
    result = tagger.tag_text("म किताब पढ्छु")
    assert len(result) == 3
    tags = [t for _, t in result]
    assert "PRON" in tags


def test_tag_multiple_tokens(tagger):
    tokens = ["म", "र", "तिमी"]
    result = tagger.tag(tokens)
    assert len(result) == 3
    assert result[0] == ("म", "PRON")
    assert result[1] == ("र", "CONJ")
    assert result[2] == ("तिमी", "PRON")


def test_tag_dictionary_entry(tagger):
    result = tagger.tag(["नेपाल"])
    tag = result[0][1]
    assert tag in ("N_NN", "N_NNP")


def test_convenience_tag_pos():
    result = tag_pos(["म", "छ"])
    assert isinstance(result, list)
    assert len(result) == 2


def test_tag_empty_list(tagger):
    assert tagger.tag([]) == []
