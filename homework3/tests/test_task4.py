from homework3.task4.Armstrong_number import is_armstrong


def test_armstrong_number_true():
    assert is_armstrong(153) is True


def test_armstrong_number_false():
    assert is_armstrong(10) is False
