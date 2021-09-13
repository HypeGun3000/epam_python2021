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


<<<<<<< HEAD
#if __name__ == '__main__':
    #with Pool(processes=50) as pool:
        #print(pool.map(slow_calculate, [i for i in range(1, 501)]))


def mukti(func):
    start_time = time.time()
    if __name__ == '__main__':
        pool = Pool(processes=50)
        resault = pool.map(func, [i for i in range(1, 501)])
    a = time.time() - start_time
    return a



print(mukti(slow_calculate))

=======
if __name__ == '__main__':
    with Pool(processes=50) as pool:
        print(pool.map(slow_calculate, [i for i in range(1, 501)]))
>>>>>>> 9f264801c0a1ce03d9e8a18400b596c00ba72601
