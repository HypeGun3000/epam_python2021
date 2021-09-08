import string
from typing import List
from collections import defaultdict


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    """
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
        list_of_words_in_text = \
        (''.join(ch for ch in text if ch not in string.punctuation)).split()
    list_of_unique_symbols = []
    count_of_unique_symbols = 0
    dict_of_words_unique_sym = {}
    for i in range(len(list_of_words_in_text)):
        for j in list_of_words_in_text[i]:
            if j not in list_of_unique_symbols:
                list_of_unique_symbols.append(j)
                count_of_unique_symbols += 1
        if list_of_words_in_text[i] not in dict_of_words_unique_sym:
            dict_of_words_unique_sym[list_of_words_in_text[i]]\
                = count_of_unique_symbols
        list_of_unique_symbols = []
        count_of_unique_symbols = 0

    list_unique_symbols_dict = []
    for k, v in dict_of_words_unique_sym.items():
        list_unique_symbols_dict.append((k, v))
    sorted_list = \
        sorted(list_unique_symbols_dict, key=lambda x: x[1], reverse=True)

    ten_largest_words = []
    for i in range(10):
        ten_largest_words.append(sorted_list[i][0])

    return ten_largest_words


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    """

    global count_of_symbols

    most_rare_symbols = []
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read().splitlines()
        file = ''.join(ch for ch in text if ch != ' ')
    dict_of_symbols = defaultdict(int)
    for i in file:
        dict_of_symbols[i] += 1

    for o in dict_of_symbols.values():
        count_of_symbols = o
        break

    for k, v in dict_of_symbols.items():
        if v < count_of_symbols:
            count_of_symbols = v
    for k, v in dict_of_symbols.items():
        if v == count_of_symbols:
            most_rare_symbols.append(k)

    return ', '.join(most_rare_symbols)


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
    count_of_every_non_ascii_char = 0
    dict_of_non_ascii_chars = defaultdict(int)
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
        list_of_words_in_text =\
            ''.join(ch for ch in text
                    if ch not in string.ascii_letters
                    and ch != ' ' and ch != '\n')
    for i in list_of_words_in_text:
        dict_of_non_ascii_chars[i] += 1
        count_of_every_non_ascii_char += 1

    def value_getter(a):
        return dict_of_non_ascii_chars.get(a)

    return max(dict_of_non_ascii_chars, key=value_getter)
