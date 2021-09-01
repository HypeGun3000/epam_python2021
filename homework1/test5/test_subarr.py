from homework1.test5.subarr import find_maximal_subarray_sum


def test_suba1():
    """
    Check array from Example
    """
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_suba2():
    """
    Check my array
    """
    assert find_maximal_subarray_sum([7, 1, -4, 12, 0, 5, 2, -7], 3) == 17
