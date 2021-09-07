from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """
    Classic task, a kind of walnut for you
    Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l)
    there are such that A[i] + B[j] + C[k] + D[l] is zero.
    We guarantee, that all A, B, C, D
    have same length of N where 0 ≤ N ≤ 1000.
    """
    count_of_tuples_is_zero = 0
    dict_of_first_two_sums = {}
    for i in a:
        for j in b:
            if i + j not in dict_of_first_two_sums:
                dict_of_first_two_sums[i + j] = 1
            else:
                dict_of_first_two_sums[i + j] += 1
    for k in c:
        for l in d:
            if -(k + l) in dict_of_first_two_sums:
                count_of_tuples_is_zero += dict_of_first_two_sums.get((-(k+l)), None)
    return count_of_tuples_is_zero
