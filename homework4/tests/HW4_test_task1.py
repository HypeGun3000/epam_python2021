from homework4.task1.doc_test import fizzbuzz


def test_fizzbuzz_sequence_until_20():
    assert fizzbuzz(20) == ['1', '2', 'fizz', '4', 'buzz',
                            'fizz', '7', '8', 'fizz',
                            'buzz', '11', 'fizz', '13',
                            '14', 'fizz', '16', '17',
                            'fizz', '19', 'buzz']


def test_fizzbuzz_sequence_until_5():
    assert fizzbuzz(5) == ['1', '2', 'fizz', '4', 'buzz']
