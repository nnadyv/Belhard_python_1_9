"""
Написать функцию add_to_path, которая будет добавлять директорию, в которой находится
переданный файл (путь к файлу) в sys.path
"""
import sys


def add_to_path(path_to_file: str):
    return sys.path.append(path_to_file)
