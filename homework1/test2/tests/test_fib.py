from homework1.test2.check_fib import check_fibonacci


def test_fib1():
    """
    Sequence of integers 1-2
    """
    assert check_fibonacci([1, 1, 2])


def test_fib2():
    """
    Sequence of one integer
    """
    assert check_fibonacci([1])


def test_fib3():
    """
    Sequence of empty integers
    """
    assert check_fibonacci([])


def test_fib4():
    """
    Long sequence of integers
    """
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])
