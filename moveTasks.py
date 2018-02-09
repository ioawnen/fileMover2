import os
import json
from settings import Settings
import re
import logging
from fileIO import *


class MoveTaskIface(object):
    def __init__(self, d=None):
        self.search_path = 'example'
        self.save_path = 'example'
        self.filename_regex = 'example.abc'

        if d:
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                    setattr(self, a, [MoveTaskIface(x) if isinstance(x, dict) else x for x in b])
                else:
                    setattr(self, a, MoveTaskIface(b) if isinstance(b, dict) else b)

    def json(self):
        return json.dumps(self.__dict__)


class MoveTasks:
    def __init__(self):
        self.write_default_move_tasks()

    @staticmethod
    def move_file_exists():
        return os.path.exists(Settings().get_settings().move_tasks_file_path)

    def write_default_move_tasks(self, force_overwrite=False):
        if self.move_file_exists() and not force_overwrite:
            logging.out("Move tasks file found / force_overwrite not enabled, skipping step.", 4)
            return
        logging.out("Move tasks file not found / force_overwrite enabled, creating default as {0}"
                    .format(Settings().get_settings().move_tasks_file_path), 3)
        move_tasks_json = json.dumps([MoveTaskIface().__dict__])
        file = open(Settings().get_settings().move_tasks_file_path, 'w')
        file.write(move_tasks_json)
        file.close()

    @staticmethod
    def get_move_tasks() -> list:
        move_tasks_json = open(Settings().get_settings().move_tasks_file_path, 'r').read()
        move_tasks = json.loads(move_tasks_json)
        logging.out("Tasks found: ", 3)
        logging.out(move_tasks, 3)
        return move_tasks
