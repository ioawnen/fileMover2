import os
import json
from settings import Settings


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

    def move_file_exists(self):
        return os.path.exists(Settings().get_settings().move_tasks_file_path)

    def write_default_move_tasks(self, force_overwrite=False):
        if self.move_file_exists() and not force_overwrite:
            return

        move_tasks_json = json.dumps([MoveTaskIface().__dict__])
        file = open(Settings().get_settings().move_tasks_file_path, 'w')
        file.write(move_tasks_json)
        file.close()

    def get_move_tasks(self) -> list:
        move_tasks_json = open(Settings().get_settings().move_tasks_file_path, 'r').read()
        print(move_tasks_json)
        return json.loads(move_tasks_json)
