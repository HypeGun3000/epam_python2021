from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 1 or len(data) == 0:
        return True
    elif len(data) == 2 and data[0] == data[1]:
        return True
    elif len(data) > 2:
        for i in range(2, len(data)):
            if data[i] == data[i-1] + data[i-2]:
                continue
            else:
                return False
        return True
    else:
        return False
