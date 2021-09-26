from homework4.task5.optional import fizzbuzz
import pytest


class TestFizzBuzz:
    @pytest.fixture
    def create_fizzbuzz_sequence_under_25(self):
        return 25

    def test_list_of_sequence_under_25(self, create_fizzbuzz_sequence_under_25):
        assert list(fizzbuzz(create_fizzbuzz_sequence_under_25)) == ['1', '2', 'fizz', '4', 'buzz',
                                                                     'fizz', '7', '8',
                                                                     'fizz', 'buzz', '11', 'fizz',
                                                                     '13', '14', 'fizzbuzz',
                                                                     '16', '17', 'fizz', '19',
                                                                     'buzz', 'fizz', '22',
                                                                     '23', 'fizz', 'buzz']

