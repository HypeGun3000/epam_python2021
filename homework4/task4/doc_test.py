from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(4)
    ['1', '2', 'fizz', '4']
    >>> fizzbuzz("hello")
    Write number (integer)
    >>> fizzbuzz(10.42)
    Write number (integer)
    >>> fizzbuzz(-20)
    'n' must be more then 0 and integer
    """
    fuzz_buzz_list = []
    try:
        if n <= 0 and isinstance(n, int):
            raise ValueError("n must be more then 0 and integer")
    except ValueError:
        return "'n' must be more then 0 and integer"
    except TypeError:
        return "Write number (integer)"
    for i in range(1, n+1):
        if i % 3 == 0:
            fuzz_buzz_list.append("fizz")
        elif i % 5 == 0:
            fuzz_buzz_list.append("buzz")
        else:
            fuzz_buzz_list.append(str(i))
    return fuzz_buzz_list
