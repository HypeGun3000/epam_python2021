from homework1.test2.check_fib import check_fibonacci


def test_fib1():
    assert check_fibonacci([1, 1, 2])


def test_fib2():
    assert check_fibonacci([1])


def test_fib3():
    assert check_fibonacci([])


def test_fib4():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])
