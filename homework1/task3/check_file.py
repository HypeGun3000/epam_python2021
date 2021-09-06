from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    Write down the function, which reads input line-by-line,
    and find maximum and minimum values.
    Function should return a tuple with the max and min values.
    For example for [1, 2, 3, 4, 5], function should return [1, 5]
    We guarantee, that file exists and contains line-delimited integers.
    To read file line-by-line you can use this snippet:
    with open("some_file.txt") as fi:
        for line in fi:
            ...
    """
    list_of_num_from_file = []
    with open(file_name) as fi:
        for line in fi:
            list_of_num_from_file.extend(line.split())
        min_max_list = [int(list_of_num_from_file[i])
                        for i in range(len(list_of_num_from_file))]
        return min(min_max_list), max(min_max_list)
