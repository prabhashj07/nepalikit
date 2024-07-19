import pytest
from nepalikit.utils import NepaliTextProcessor

@pytest.fixture
def text_processor():
    return NepaliTextProcessor(delimiter=' ')

def test_merge_text(text_processor):
    tokens = ['नमस्कार', 'साथी', 'हामी', 'सबै']
    merged_text = text_processor.merge_text(tokens)
    assert merged_text == 'नमस्कार साथी हामी सबै'

def test_split_text(text_processor):
    text = 'नमस्कार साथी हामी सबै'
    tokens = text_processor.split_text(text)
    assert tokens == ['नमस्कार', 'साथी', 'हामी', 'सबै']

def test_count_words(text_processor):
    text = 'नमस्कार साथी हामी सबै'
    word_count = text_processor.count_words(text)
    assert word_count == 4

def test_count_words_in_paragraph(text_processor):
    paragraph = 'नमस्कार साथी। तपाईलाई कस्तो छ?'
    total_words = text_processor.count_words_in_paragraph(paragraph)
    assert total_words == 5  

