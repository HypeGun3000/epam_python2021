from homework2.most_least_common import major_and_minor_elem


def test_max_common_and_min_char_in_list():
    assert major_and_minor_elem([5, 6, 2, 1, 6, 2, 2, 2, 3, 2, 2, 2, 2, 6, 1, 2, 2, 3]) == (2, 5)


def test_max_common_and_min_char_in_list_example():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)
