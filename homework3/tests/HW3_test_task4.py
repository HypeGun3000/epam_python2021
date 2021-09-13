from homework3.task4.Armstrong_number import is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) is True


def test_not_armstrong_number():
    assert is_armstrong(10) is False
