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
