import string
from collections import defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    """
    list_of_10_words = []
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
    list_of_words_in_text = \
        (''.join(ch for ch in text if ch not in string.punctuation)).split()
    dict_words_and_unique_sym = {i: set(i) for i in list_of_words_in_text}
    for k, v in dict_words_and_unique_sym.items():
        list_of_10_words.append((k, v))
    list_of_10_words = sorted(list_of_10_words,
                              key=lambda x: len(x[1]), reverse=True)

    return [list_of_10_words[x][0] for x in range(10)]


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    """
    dict_of_symbols = defaultdict(int)

    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
    text = text.replace(' ', '')

    for i in text:
        dict_of_symbols[i] += 1

    rarest_char = min(dict_of_symbols, key=dict_of_symbols.get)
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """
    Count every punctuation char
    """
    count_of_punctuation_chars = 0
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
    for i in text:
        if i in string.punctuation:
            count_of_punctuation_chars += 1
    return count_of_punctuation_chars


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char
    """
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read().splitlines()
    count_of_non_ascii_chars = 0
    for i in text:
        if i not in string.ascii_letters:
            count_of_non_ascii_chars += 1
    return count_of_non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    """
    dict_of_non_ascii_chars = defaultdict(int)
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
    list_of_words_in_text =\
        ''.join(ch for ch in text
                if ch not in string.ascii_letters
                and ch != ' ' and ch != '\n')
    for i in list_of_words_in_text:
        dict_of_non_ascii_chars[i] += 1

    return max(dict_of_non_ascii_chars, key=dict_of_non_ascii_chars.get)
