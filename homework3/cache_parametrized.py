from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs):
        nonlocal cache_dict
        key = (args, tuple(kwargs.items()))
        if key not in cache_dict:
            response = func(*args, **kwargs)
            cache_dict[key] = response
        return cache_dict[key]
    return wrapper


@cache(time=2)
def f(a, b):
    return a*b

f(10, 2)
print(f(10, 2))