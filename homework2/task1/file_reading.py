import string
from typing import List
from collections import defaultdict


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    """
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
        list_of_words_in_text = (''.join(ch for ch in text if ch not in string.punctuation)).split()
    print(list_of_words_in_text)
    list_of_unique_symbols = []
    count_of_unique_symbols = 0
    dict_of_words_unique_sym = {}
    for i in range(len(list_of_words_in_text)):
        for j in list_of_words_in_text[i]:
            if j not in list_of_unique_symbols:
                list_of_unique_symbols.append(j)
                count_of_unique_symbols += 1
        if list_of_words_in_text[i] not in dict_of_words_unique_sym:
            dict_of_words_unique_sym[list_of_words_in_text[i]] = count_of_unique_symbols
        list_of_unique_symbols = []
        count_of_unique_symbols = 0

    list_unique_symbols_dict = []
    for k, v in dict_of_words_unique_sym.items():
        list_unique_symbols_dict.append((k, v))
    a = sorted(list_unique_symbols_dict, key=lambda x: x[1], reverse=True)

    ten_largest_words = []
    for i in range(10):
        ten_largest_words.append(a[i][0])

    return ten_largest_words


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    """
    most_rare_symbols = []
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
        file = ''.join(ch for ch in text if ch != ' ' and ch != '\n')
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

    return most_rare_symbols


def count_punctuation_chars(file_path: str) -> int:
    """
    Count every punctuation char
    """
    count_of_punctuation_chars = 0
    with open(file_path) as fi:
        text = fi.read()
        for i in text:
            if i in string.punctuatuin:
                count_of_punctuation_chars += 1
    return count_of_punctuation_chars


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char
    """
    list_of_words_in_text = []
    with open(file_path) as fi:
        for i in fi:
            list_of_words_in_text.extend(i.split())
    count_of_non_ascii_chars = 0
    for k in range(len(list_of_words_in_text)):
        for v in range(len(list_of_words_in_text[k])):
            if list_of_words_in_text[k][v] not in string.ascii_letters:
                count_of_non_ascii_chars += 1
    return count_of_non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    """
    list_of_words_in_text = []
    dict_of_non_ascii_chars = {}
    amount_of_non_ascii_chars = 0
    with open(file_path) as fi:
        for i in fi:
            list_of_words_in_text.extend(i.split())
    for k in range(len(list_of_words_in_text)):
        for v in range(len(list_of_words_in_text[k])):
            if list_of_words_in_text[k][v] not in string.ascii_letters:
                amount_of_non_ascii_chars += 1
                if list_of_words_in_text[k][v] not in dict_of_non_ascii_chars:
                    dict_of_non_ascii_chars[list_of_words_in_text[k][v]] = 1
                else:
                    dict_of_non_ascii_chars[list_of_words_in_text[k][v]] += 1
    count_of_every_non_ascii_char = 0
    for k, v in dict_of_non_ascii_chars.items():
        if v >= count_of_every_non_ascii_char and v > amount_of_non_ascii_chars // 2:
            count_of_every_non_ascii_char = v
    for k, v in dict_of_non_ascii_chars.items():
        if v == count_of_every_non_ascii_char:
            return k
