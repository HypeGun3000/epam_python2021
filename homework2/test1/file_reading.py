from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    lwords = []
    l10words = []
    with open(file_path) as fi:
        for i in fi:
            lwords.extend(i.split())
            lwords = sorted(lwords, key=len, reverse=True)
        for j in range(10):
            l10words.append(lwords[j])
        return l10words


def get_rarest_char(file_path: str) -> str:
    pass


def count_punctuation_chars(file_path: str) -> int:
    pass


def count_non_ascii_chars(file_path: str) -> int:
    pass


def get_most_common_non_ascii_char(file_path: str) -> str:
    pass

print(get_longest_diverse_words("data.txt"))