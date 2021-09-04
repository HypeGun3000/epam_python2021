from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    Given an array of size n, find the most common and the least common elements.
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
    checker = {}
    finalanswer = ()
    for i in inp:
        if i not in checker:
            checker[i] = 1
        else:
            checker[i] += 1
    count = 0
    for k, v in checker.items():
        if v > count and v > len(inp) // 2:
            count = v
    for k, v in checker.items():
        if v == count:
            finalanswer += (k, )
    for k, v in checker.items():
        if v < count:
            count = v
    for k, v in checker.items():
        if v == count:
            finalanswer += (k, )
    return finalanswer

print(major_and_minor_elem([5,6,2,1,6,2,2,2,3,2,2,2,2,6,1,2,2]))