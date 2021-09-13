import string

from homework2.task5.custom_range import custom_range


def test_one_char_range_lowercase():
    assert custom_range(string.ascii_lowercase, 'g')\
           == ['a', 'b', 'c', 'd', 'e', 'f']


def test_two_char_range_uppercase():
    assert custom_range(string.ascii_uppercase, 'G', 'P')\
           == ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']


def test_three_char_range_lowercase_back():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2)\
           == ['p', 'n', 'l', 'j', 'h']


def test_three_char_range_lowercase():
    assert custom_range(string.ascii_lowercase, 'g', 'p', 3) == ['g', 'j', 'm']
