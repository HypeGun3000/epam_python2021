from homework3.task2.multiprocessing_module import slow_calculate,\
                                                   multiprocessing

import time


def test_of_time_spending():
    start_time = time.time()
    multiprocessing(slow_calculate)
    assert time.time() - start_time < 100
