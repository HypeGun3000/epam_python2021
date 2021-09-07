from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def wrapper(*args, **kwargs):
        nonlocal cache_dictionary
        key = (args, tuple(kwargs.items()))
        if key not in cache_dictionary:
            response = func(*args, **kwargs)
            cache_dictionary[key] = response
        return cache_dictionary[key]
    return wrapper


@cache
def func(a, b):
    return (a ** b) ** 2
