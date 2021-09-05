from typing import Callable


def cache(func: Callable) -> Callable:
    if func not in cache_dic:
        cache_dic[func] = func
        return func
    else:
        print(cache_dic)



def func1(a, b):
    return (a ** b) ** 2


cache_dic = {}

cache_func = cache(func1)

val_1 = cache_func(100, 200)
val_2 = cache_func(100, 200)
val_3 = cache_func(101, 200)
val_4 = cache_func(135, 351)


print(cache_dic)


