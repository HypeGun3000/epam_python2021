from homework1.task2.check_fib import check_fibonacci


def test_simple_sequence():
    """
    Sequence of integers 1-2
    """
    assert check_fibonacci([1, 1, 2]) is True


def test_more_than_3_sequence():
    """
    Long sequence of integers
    """
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21]) is True


def test_false_sequence():
    """
    Testing False sequence of integers
    :return:
    """
    assert check_fibonacci([1, 2, 3, 4, 5, 6]) is False
