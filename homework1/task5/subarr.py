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
    first_num_for_checking = nums[0]
    len_nums = len(nums)
    if k > len_nums:
        k = len_nums
    for i in range(len_nums):
        for j in range(1, k + 1):
            if sum(nums[i:i + j]) > first_num_for_checking and i + j <= len_nums:
                first_num_for_checking = sum(nums[i:i + j])
    return first_num_for_checking
