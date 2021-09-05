from itertools import product

from typing import (List, Any)


def combinations(*args: List[Any]) -> List[List]:
    """
    Write a function that takes K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so one.
    You may assume that that every list contain at least one element
    Example:
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
    """
    flist = []
    final_list = []
    comb = list(product(*args))
    for i in range(len(comb)):
        for j in range(len(comb[i])):
            flist.append(comb[i][j])
        final_list.append(flist)
        flist = []
    return final_list
