import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocessing(func):
    list_for_get_res_of_processes = []
    pool = Pool(50)
    pool_res = pool.map(func, [i for i in range(1, 501)])
    list_for_get_res_of_processes.append(pool_res)
    return list_for_get_res_of_processes




