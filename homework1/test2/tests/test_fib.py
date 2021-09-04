from homework1.test2.check_fib import check_fibonacci


def test_simple_sequence():
    """
    Sequence of integers 1-2
    """
    assert check_fibonacci([1, 1, 2])


def test_more_then_3_sequence():
    """
    Long sequence of integers
    """
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])
