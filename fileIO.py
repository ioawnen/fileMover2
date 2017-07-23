"""This class is basically an interface for os library functions."""

import os

def file_exists(path) -> bool:
    return os.path.exists(path)

def move_file(target, destination):
    os.rename(target, destination)

def change_file_permissions(target, mode):
    os.chmod(target, mode)


def get_all_files(path, follow_symlinks=False) -> tuple:
    return os.walk(path, followlinks=follow_symlinks)
