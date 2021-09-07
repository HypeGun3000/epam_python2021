from homework2.task4.function_cache import func

cache_func = func

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)


def test_function_cache_example():
    assert val_1 is val_2


val_3 = cache_func(150, 200)
val_4 = cache_func(150, 200)


def test_function_cache_myself():
    assert val_3 is val_4
