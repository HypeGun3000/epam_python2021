from homework1.test4.sum4 import check_sum_of_four


def test_sum_four1():
    assert check_sum_of_four([1, 2, 3], [4, 5, 6], [-1, -5, -3], [-4, -2, -1]) == 11


def test_sum_four2():
    assert check_sum_of_four([1, 2], [-1, -2], [3, 4], [-3, -4]) == 6
