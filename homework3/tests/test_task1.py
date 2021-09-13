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
