from homework2.file_reading import get_longest_diverse_words, \
    get_rarest_char, count_punctuation_chars, \
    count_non_ascii_chars, get_most_common_non_ascii_char


def test_longest_unique_symbols_words():
    assert get_longest_diverse_words("data.txt") == ['kalyptischen',
                                                     'Augenblick,',
                                                     'Grundmotiv,',
                                                     'Evangelium,',
                                                     'Deutschland',
                                                     'unsterblich',
                                                     'vorfindet.',
                                                     'Schauspiel',
                                                     'Bolschewik',
                                                     'Sicherung.']


def test_rarest_char_in_text():
    assert get_rarest_char("data.txt") == "Y, X, (, )"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 8277


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") == 15880


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == "0"
