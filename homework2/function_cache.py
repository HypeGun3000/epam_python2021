from typing import Callable


def cache(func: Callable) -> Callable:
    cache_key = {}

    def wrapper(*args, **kwargs):
        nonlocal cache_key
        key = (args, tuple(kwargs.items()))
        if key not in cache_key:
            response = func(*args, **kwargs)
            cache_key[key] = response
        return cache_key[key]
    return wrapper


@cache
def func(a, b):
    return (a ** b) ** 2
