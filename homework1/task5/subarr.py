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
    for i in range(k):
        for j in range(len_nums - i):
            sum_of_sequence_less_then_k = nums[j]
            for p in range(1, i + 1):
                sum_of_sequence_less_then_k += nums[j + p]
            if sum_of_sequence_less_then_k > first_num_for_checking:
                first_num_for_checking = sum_of_sequence_less_then_k
    return first_num_for_checking
