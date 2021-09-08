from typing import List, Tuple

from collections import defaultdict


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    Given an array of size n, find the most common
    and the least common elements.
    The most common element is the element that appears more than n // 2 times.
    The least common element is the element that appears fewer than other.
    You may assume that the array is non-empty and the most common element
    always exist in the array.

    Example 1:
    Input: [3,2,3]
    Output: 3, 2
    Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2, 1

    """
    dict_amount_of_symbols = defaultdict(int)

    def value_getter(a):
        return dict_amount_of_symbols.get(a)

    for i in inp:
        dict_amount_of_symbols[i] += 1
    most_and_least_common_elements = (max(dict_amount_of_symbols, key=value_getter),
                                      min(dict_amount_of_symbols, key=value_getter))
    return most_and_least_common_elements
