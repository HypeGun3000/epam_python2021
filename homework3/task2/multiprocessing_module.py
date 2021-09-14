import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocessing(func):
    with Pool(50) as pool:
        pool_res = pool.map(func, [i for i in range(1, 501)])
    return pool_res
