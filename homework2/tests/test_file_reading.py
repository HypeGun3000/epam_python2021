from pathlib import Path

from homework2.task1.file_reading import (count_non_ascii_chars,
                                          count_punctuation_chars,
                                          get_longest_diverse_words,
                                          get_most_common_non_ascii_char,
                                          get_rarest_char)

root = Path(__file__).parent
data_file = root / 'data.txt'


def test_longest_unique_symbols_words():
    assert get_longest_diverse_words(data_file) \
           == ['unmißverständliche', 'Bevölkerungsabschub',
               'Kollektivschuldiger', 'Werkstättenlandschaft',
               'Schicksalsfiguren', 'Selbstverständlich',
               'Fingerabdrucks', 'Friedensabstimmung',
               'außenpolitisch', 'Seinsverdichtungen']


def test_rarest_char_in_text():
    assert get_rarest_char(data_file) == "›"


def test_count_punctuation_chars():
    assert count_punctuation_chars(data_file) == 5305


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(data_file) == 3352


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(data_file)\
           == ","
