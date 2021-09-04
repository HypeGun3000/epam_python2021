from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Given a cell with "it's a fib sequence" from slideshow,
        please write function "check_fib",
        which accepts a Sequence of integers, and
        returns if the given sequence is a Fibonacci sequence
    We guarantee, that the given sequence contain >= 0 integers inside.
    """
    ldata = len(data)
    if ldata > 2:
        for i in range(2, ldata):
            if data[i] != data[i-1] + data[i-2]:
                return False
        return True
    else:
        return False
