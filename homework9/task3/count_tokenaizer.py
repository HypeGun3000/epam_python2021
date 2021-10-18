from pathlib import Path
from typing import Optional, Callable

import os


dir_path = os.getcwd()


def get_files_with_extension(dir_path: Path, file_extension: str):
    files_with_extension = []
    try:
        for file in os.listdir(dir_path):
            if file.endswith(file_extension):
                files_with_extension.append(file)
        return files_with_extension
    except NotADirectoryError:
        return "Wrong path"

def using_tokenizer(dir_path: Path, file_extension: str):
    print(get_files_with_extension(dir_path, file_extension))

print(using_tokenizer(dir_path, ".txt"))





def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Write a function that takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.
    For dir with two files from hw1.py:
    >>> universal_file_counter(test_dir, "txt")
    6
    >>> universal_file_counter(test_dir, "txt", str.split)
    6
    """
    count = 0
    files_with_extension = []
    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            files_with_extension.append(file)
    print(files_with_extension)

print(universal_file_counter(dir_path, "txt", str.split))
