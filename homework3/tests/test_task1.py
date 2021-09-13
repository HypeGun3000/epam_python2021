<<<<<<< HEAD
from homework3.task1.cache_parametrized import cache


counter = 0


@cache(times=2)
def f(a):
    global counter
    counter += 1
    return a, counter


f(2)
f(2)
f(2)


def test_counter_of_cache_func_after_three_calls():
    assert counter == 2



=======
from homework3.task1.cache_parametrized import f, cache


@cache(times=2)
def fu(a):
    global count
    count += 1
    return a


count = 0


def test_func():
    assert fu(1) == 1
    assert fu(1) == 1
>>>>>>> 9f264801c0a1ce03d9e8a18400b596c00ba72601
