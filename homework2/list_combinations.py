from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    for i in range(len(args)):
        for j in range(len(args[i])):
            print(args[i][j])

print(combinations([1, 2], [3, 4], [5, 6]))

