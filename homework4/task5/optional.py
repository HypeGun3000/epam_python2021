"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
#>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str]:
    count = 0
    for number in range(n):

    while count != n:
        if n / 3 == 0:
            count +=1
            yield "fizz"
        elif n/5 == 0:
            yield "buzz"
            count += 1
        elif n/15 == 0:
            yield "fizzbuzz"
            count += 1
        else:
            yield str(count)
            count += 1