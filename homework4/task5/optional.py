"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    gen_fizzbuzz = []
    for i in range(1, n+1):
        gen_fizzbuzz.append(str(i))
    for i in range(2, n, 3):
        gen_fizzbuzz[i] = "fizz"
    for i in range(4, n, 5):
        gen_fizzbuzz[i] = "buzz"
    for i in range(14, n, 15):
        gen_fizzbuzz[i] = "fizzbuzz"
    count = 0
    while count != n:
        count += 1
        yield gen_fizzbuzz[count - 1]

print(list(fizzbuzz(25)))
