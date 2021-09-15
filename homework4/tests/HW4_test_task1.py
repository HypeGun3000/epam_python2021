from homework4.task1.read_file import read_magic_number
import pytest
from pathlib import Path


root = Path(__file__).parent
data_file = root / 'data.txt'


@pytest.fixture
def fixture_for_all_tests():
    return read_magic_number


def test_file_with_non_int_first_line(fixture_for_all_tests):
    assert fixture_for_all_tests("data.txt") is False


def test_file_with_true_first_line(fixture_for_all_tests):
    assert fixture_for_all_tests("data2.txt") is True


def test_file_false_int(fixture_for_all_tests):
    assert fixture_for_all_tests("data3.txt") is False


def test_empty_file(fixture_for_all_tests):
    assert fixture_for_all_tests("data4.txt") is False
