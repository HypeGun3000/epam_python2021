from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Given a list of integers numbers "nums".
    You need to find a sub-array with length less equal to "k",
    with maximal sum.
    The written function should return the sum of this sub-array.
    Examples:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        result = 16
    """
    max_fin = 0
    max1 = 0
    for i in range(0, len(nums) - 2, 1):
        for j in range(k):
            max1 += nums[i + j]
        if max1 > max_fin:
            max_fin = max1
            max1 = 0
        else:
            max1 = 0
    return max_fin
