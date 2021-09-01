import os

from homework1.test3.check_file import find_maximum_and_minimum


def test_minmax():
    """
    Check for minimal and maximum integers in file (.txt) (1 and 5)
    """
    our_dir = os.path.dirname(__file__)
    filename = os.path.join(our_dir, 'some_file(1, 5).txt')
    assert find_maximum_and_minimum(filename) == (1, 5)


def test_minmax1():
    """
    Check for minimal and maximum integers in file (.txt) (6 and 85)
    """
    our_dir = os.path.dirname(__file__)
    filename = os.path.join(our_dir, 'some_file(6, 85).txt')
    assert find_maximum_and_minimum(filename) == (6, 85)
