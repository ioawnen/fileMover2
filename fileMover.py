import re
from fileIO import *
from moveTasks import MoveTasks, MoveTaskIface
from logging import out


def get_matching_files(move_task: MoveTaskIface) -> list:
    pattern = re.compile(move_task.filename_regex)
    matches = []

    for root, dirs, files in get_all_files(move_task.search_path):
        out("Found {0} files in {1} subdirectories".format(len(files), len(dirs)), 2)
        for file in files:
            if re.search(pattern, file):
                matches.append((root, file))

    return matches


def perform_check():
    # STEP 1: GET ALL MOVE TASKS
    move_tasks = MoveTasks().get_move_tasks()
    out("Found {0} Move Task(s)".format(len(move_tasks)), 2)

    # STEP 2: WORK EACH TASK
    for move_task in move_tasks:
        move_task = MoveTaskIface(move_task)
        out("Working task: {0} {1} -> {2}".format(move_task.search_path, move_task.filename_regex, move_task.save_path),
            2)

        # STEP 3: GET FILES FOR TASK, MOVE EACH
        for path, file in get_matching_files(move_task):
            move_file(path, move_task.save_path, file)


def main():
    print("   __   _   _          __  __                                 ____   \n" +
          "  / _| (_) | |   ___  |  \/  |   ___   __   __   ___   _ __  |___ \  \n" +
          " | |_  | | | |  / _ \ | |\/| |  / _ \  \ \ / /  / _ \ | '__|   __) | \n" +
          " |  _| | | | | |  __/ | |  | | | (_) |  \ V /  |  __/ | |     / __/  \n" +
          " |_|   |_| |_|  \___| |_|  |_|  \___/    \_/    \___| |_|    |_____| \n" +
          " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n" +
          "     IN DEVELOPMENT. DO NOT TRUST THIS TO ACTUALLY WORK. ENJOY.      \n\n")

    perform_check()
    print("\nTasks Completed, exiting....")
    exit()


if __name__ == '__main__':
    main()
