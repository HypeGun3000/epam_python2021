import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    """
    list_of_words_in_text = []
    ten_longest_words = []
    words_with_unique_symbols = []
    amount_of_unique_symbols = {}
    with open(file_path) as fi:
        for i in fi:
            list_of_words_in_text.extend(i.split())
            for k in range(len(list_of_words_in_text)):
                for o in range(len(list_of_words_in_text[k])):
                    if list_of_words_in_text[k][o] not in amount_of_unique_symbols:
                        amount_of_unique_symbols[list_of_words_in_text[k][o]] = 1
                    else:
                        amount_of_unique_symbols[list_of_words_in_text[k][o]] += 1
                flag = True
                for u in amount_of_unique_symbols.values():
                    if u > 1:
                        flag = False
                        break
                if flag is True:
                    words_with_unique_symbols.append(list_of_words_in_text[k])
            amount_of_unique_symbols = {}
            list_of_words_in_text = []

        words_with_unique_symbols = sorted(words_with_unique_symbols, key=len, reverse=True)
        amount_of_longest_words = 10
        if len(words_with_unique_symbols) < amount_of_longest_words:
            amount_of_longest_words = len(words_with_unique_symbols)
        [ten_longest_words.append(words_with_unique_symbols[j]) for j in range(amount_of_longest_words)]
        return ten_longest_words


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document
    """
    list_of_words_in_text = []
    dict_of_symbols = {}
    most_rare_symbols = []
    with open(file_path) as fi:
        for i in fi:
            list_of_words_in_text.extend(i.split())
        for j in range(len(list_of_words_in_text)):
            for k in range(len(list_of_words_in_text[j])):
                if list_of_words_in_text[j][k] not in dict_of_symbols:
                    dict_of_symbols[list_of_words_in_text[j][k]] = 1
                else:
                    dict_of_symbols[list_of_words_in_text[j][k]] += 1
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
    list_of_words_in_text = []
    count_of_punctuation_chars = 0
    with open(file_path) as fi:
        for i in fi:
            list_of_words_in_text.extend(i.split())
        for k in range(len(list_of_words_in_text)):
            for j in range(len(list_of_words_in_text[k])):
                if list_of_words_in_text[k][j] in string.punctuation:
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
