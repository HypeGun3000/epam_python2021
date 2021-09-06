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
    sum_of_first_two_lists = []
    #sum_of_second_two_lists = []
    count = 0
    for i in a:
        for j in b:
            sum_of_first_two_lists.append(i + j)
    for k in c:
        for p in d:
            if -(k + p) in sum_of_first_two_lists:
                count += 1
    #for o in sum_of_first_two_lists:
        #for q in sum_of_second_two_lists:
            #if o + q == 0:
                #count += 1
    return count
