import pickle
from typing import Callable


def cache(times):
    count = times

    def func(function: Callable) -> Callable:
        cache_dictionary = {}

        def wrapper(*args, **kwargs):
            nonlocal times
            nonlocal count
            nonlocal cache_dictionary
            if count == 0:
                cache_dictionary = {}
                count = times
            key = (args, tuple(kwargs.items()))
            bite_code = pickle.dumps(key)
            if bite_code not in cache_dictionary:
                response = function(*args, **kwargs)
                cache_dictionary[bite_code] = response
            print(cache_dictionary[bite_code])
            count -= 1
            return cache_dictionary
        return wrapper
    return func
