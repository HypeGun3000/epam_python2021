from typing import List
from collections import defaultdict
import string

def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document
    """
    count_of_every_non_ascii_char = 0
    dict_of_non_ascii_chars = defaultdict(int)
    with open(file_path, 'r', encoding="unicode-escape") as fi:
        text = fi.read()
        list_of_words_in_text = ''.join(ch for ch in text if ch not in string.ascii_letters and ch != ' ' and ch != '\n')
    for i in list_of_words_in_text:
        dict_of_non_ascii_chars[i] += 1
        count_of_every_non_ascii_char += 1

    def value_getter(a):
        return dict_of_non_ascii_chars.get(a)

    return max(dict_of_non_ascii_chars, key=value_getter)

print(get_most_common_non_ascii_char("../tests/data.txt"))
