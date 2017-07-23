from settings import Settings
from moveTasks import MoveTasks
from fileIO import *


def main():
    print(Settings().get_settings().move_tasks_file_path)

    MoveTasks()
    get_all_files('C:\\')
    exit()


if __name__ == '__main__':
    main()
