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


if __name__ == '__main__':
    with Pool(processes=50) as pool:
        print(pool.map(slow_calculate, [i for i in range(1, 51)]))
        print(pool.map(slow_calculate, [i for i in range(51, 101)]))
        print(pool.map(slow_calculate, [i for i in range(101, 151)]))
        print(pool.map(slow_calculate, [i for i in range(151, 201)]))
        print(pool.map(slow_calculate, [i for i in range(201, 251)]))
        print(pool.map(slow_calculate, [i for i in range(251, 301)]))
        print(pool.map(slow_calculate, [i for i in range(301, 351)]))
        print(pool.map(slow_calculate, [i for i in range(351, 401)]))
        print(pool.map(slow_calculate, [i for i in range(401, 451)]))
        print(pool.map(slow_calculate, [i for i in range(451, 501)]))
