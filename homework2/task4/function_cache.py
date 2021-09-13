import pickle
from typing import Callable


def cache(function: Callable) -> Callable:
    cache_dictionary = {}

    def wrapper(*args, **kwargs):
        nonlocal cache_dictionary
        key = (args, tuple(kwargs.items()))
        bite_code = pickle.dumps(key)
        if bite_code not in cache_dictionary:
            response = function(*args, **kwargs)
            cache_dictionary[bite_code] = response
        return cache_dictionary[bite_code]
    return wrapper


@cache
def func(a, b):
    return a * b
