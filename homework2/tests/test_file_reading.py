from homework2.task1.file_reading import get_longest_diverse_words,\
                                   get_rarest_char, count_punctuation_chars,\
                                   count_non_ascii_chars,\
                                   get_most_common_non_ascii_char


def test_longest_unique_symbols_words():
    assert get_longest_diverse_words("data.txt") \
           == ['unmißverständliche', 'Bevölkerungsabschub',
               'Kollektivschuldiger','Werkstättenlandschaft',
               'Schicksalsfiguren', 'Selbstverständlich',
               'Fingerabdrucks', 'Friedensabstimmung',
               'außenpolitisch','Seinsverdichtungen']


def test_rarest_char_in_text():
    assert get_rarest_char("data.txt") == "›, ‹, Y, î, ’, X, (, )"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 5305


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") == 3352


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == ","
