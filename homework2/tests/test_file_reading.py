from homework2.task1.file_reading import (count_non_ascii_chars,
                                          count_punctuation_chars,
                                          get_longest_diverse_words,
                                          get_most_common_non_ascii_char,
                                          get_rarest_char)


def test_longest_unique_symbols_words():
    assert get_longest_diverse_words("C:\\Users\\Danya\\"
                                     "Desktop\\EPAM Python 2021\\"
                                     "homework2\\task1") \
           == ['unmißverständliche', 'Bevölkerungsabschub',
               'Kollektivschuldiger', 'Werkstättenlandschaft',
               'Schicksalsfiguren', 'Selbstverständlich',
               'Fingerabdrucks', 'Friedensabstimmung',
               'außenpolitisch', 'Seinsverdichtungen']


def test_rarest_char_in_text():
    assert get_rarest_char("C:\\Users\\Danya\\Desktop\\"
                           "EPAM Python 2021\\homework2\\"
                           "task1\\data.txt")\
            == "›, ‹, Y, î, ’, X, (, )"


def test_count_punctuation_chars():
    assert count_punctuation_chars("../task1/data.txt") == 5305


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("../task1/data.txt") == 3352


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("../task1/data.txt") == ","
