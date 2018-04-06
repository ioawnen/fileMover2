"""This class is basically an interface for os library functions."""

import logging
import os
import shutil


def file_exists(path: str) -> bool:
    """Checks if a file exists
    
    Arguments:
        path {str} -- Path of the file
    
    Returns:
        bool -- File exists
    """

    return os.path.exists(path)


def move_file(target_dir, destination_dir, filename):
    """Moves a file from the target directory to the destination directory.
    Creates destination directory if it doesn't already exist.
    
    Arguments:
        target_dir {[type]} -- Target directory
        destination_dir {[type]} -- Destination directory
        filename {[type]} -- Filename
    """

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
    """Changes the target file permissions to an input mode.
    
    Arguments:
        target {[type]} -- Target file
        mode {[type]} -- New permissions
    """

    os.chmod(target, mode)


def get_all_files(path, follow_symlinks=False):
    """Returns all files / directories in an input path.
    
    Arguments:
        path {str} -- Initial path
    
    Keyword Arguments:
        follow_symlinks {bool} -- Should the search include symlinks (default: {False})
    
    Returns:
        [type] -- See os.walk.
    """
    return os.walk(path, followlinks=follow_symlinks)
