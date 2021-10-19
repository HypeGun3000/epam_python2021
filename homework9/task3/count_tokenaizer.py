import os
from pathlib import Path
from typing import Callable, Optional


def get_files_with_extension(dir_path: Path, file_extension: str):
    if not os.path.isdir(dir_path):
        raise NotADirectoryError("It's not a directory")
    p = Path('.')
    files_list = list(p.glob(f"**/*.{file_extension}"))
    return files_list


def universal_file_counter(dir_path: Path, file_extension: str,
                           tokenizer: Optional[Callable] = None):
    count_of_lines = 0
    count_of_tokens = 0
    if tokenizer is None:
        for i in get_files_with_extension(dir_path, file_extension):
            with open(os.path.join(dir_path, i)) as file:
                count_of_lines += len(file.readlines())
        return count_of_lines

    for i in get_files_with_extension(dir_path, file_extension):
        with open(os.path.join(dir_path, i)) as file:
            for line in file.readlines():
                if tokenizer(line):
                    count_of_tokens += 1
    return count_of_tokens
