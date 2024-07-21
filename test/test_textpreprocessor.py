import pytest
from nepalikit.preprocessing.TextProcessor import TextProcessor

@pytest.fixture
def processor():
    return TextProcessor(stopwords=['र', 'छ', 'हो'])

def test_remove_html_tags(processor):
    text = "<p>यो एउटा परीक्षण हो</p>"
    expected = "यो एउटा परीक्षण हो"
    assert processor.remove_html_tags(text) == expected

def test_remove_special_characters(processor):
    text = "नेपाल!@# एक सुन्दर देश हो।"
    expected = "नेपाल एक सुन्दर देश हो"
    assert processor.remove_special_characters(text) == expected

def test_remove_extra_whitespace(processor):
    text = "  नेपाल    एक    सुन्दर    देश   हो  "
    expected = "नेपाल एक सुन्दर देश हो"
    assert processor.remove_extra_whitespace(text) == expected

def test_remove_stopwords(processor):
    text = "नेपाल एक सुन्दर देश हो र यो एउटा परीक्षण छ"
    expected = "नेपाल एक सुन्दर देश यो एउटा परीक्षण"
    assert processor.remove_stopwords(text) == expected

def test_normalize_text(processor):
    text = "नेपाल एक सुन्दर देश हो"
    expected = "नेपाल एक सुन्दर देश हो"  # Nepali text is already lowercase
    assert processor.normalize_text(text) == expected

def test_preprocess_text(processor):
    text = "<p>नेपाल!@# एक    सुन्दर देश हो र www.example.com छ</p>"
    expected = "नेपाल एक सुन्दर देश"
    assert processor.preprocess_text(text) == expected

def test_get_word_frequency(processor):
    tokens = ['नेपाल', 'एक', 'सुन्दर', 'देश', 'नेपाल', 'हो']
    expected = {'नेपाल': 2, 'एक': 1, 'सुन्दर': 1, 'देश': 1, 'हो': 1}
    assert dict(processor.get_word_frequency(tokens)) == expected
