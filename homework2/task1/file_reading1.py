import string
from typing import List
from collections import defaultdict


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


print(get_rarest_char("data.txt"))
