from pathlib import Path
import os


dir = os.path.dirname(__file__)
print(dir)
print(os.getcwd())

for file in os.listdir(Path):
    if file.endswith(".txt"):
        print(file)