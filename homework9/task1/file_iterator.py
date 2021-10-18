from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    iter_list = []
    for single_file in file_list:
        with open(single_file) as file:
            for i in file.readlines():
                try:
                    iter_list.append(int(i.rstrip()))
                except ValueError:
                    pass

    return sorted(iter_list)
