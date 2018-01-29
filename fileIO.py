"""This class is basically an interface for os library functions."""

import os
import logging
import shutil


def file_exists(path) -> bool:
    return os.path.exists(path)


def move_file(target_dir, destination_dir, filename):
    src = os.path.join(target_dir, filename)
    dst = os.path.join(destination_dir, filename)

    logging.out("Moving {0} to {1}".format(src, dst), 2)

    try:
        os.makedirs(destination_dir)
        logging.out("Destination directory did not exist, created one.", 4)
    except OSError:
        pass

    shutil.move(src, dst)


def change_file_permissions(target, mode):
    os.chmod(target, mode)


def get_all_files(path, follow_symlinks=False):
    return os.walk(path, followlinks=follow_symlinks)
