from homework1.task5.subarr import find_maximal_subarray_sum


def test_array_from_example():
    """
    Check array from Example
    """
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_array_form_myself():
    """
    Check my array
    """
    assert find_maximal_subarray_sum([7, 1, -4, 12, 0, 5, 2, -7], 3) == 17


def test_array_with_k_more_then_len():
    """
    Check array, where k, more then len(list)
    """
    assert find_maximal_subarray_sum([4, 7, -2, 2, 11, 9, -3], 111) == 31
