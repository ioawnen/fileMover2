import json
import os


class SettingsIface(object):
    def __init__(self, d=None):
        # SETTINGS DEFAULTS
        self.move_tasks_file_path = 'move_tasks.json'
        self.log_level = 2
        # DEFAULTS END
        if d:
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                    setattr(self, a, [SettingsIface(x) if isinstance(x, dict) else x for x in b])
                else:
                    setattr(self, a, SettingsIface(b) if isinstance(b, dict) else b)

    def json(self):
        return json.dumps(self.__dict__)


class Settings:
    SETTINGS_FILE_PATH = 'settings.json'

    def __init__(self):
        self.write_default_settings()

    def settings_file_exists(self):
        return os.path.exists(self.SETTINGS_FILE_PATH)

    def write_default_settings(self, force_overwrite=False):
        """Writes default settings to file as JSON"""
        if self.settings_file_exists() and not force_overwrite:
            return
        settings_json = json.dumps(SettingsIface().__dict__)
        file = open(self.SETTINGS_FILE_PATH, 'w')
        file.write(settings_json)
        file.close()

    def get_settings(self) -> SettingsIface:
        """Returns user settings from file cast into a SettingsIface object"""
        settings_json = open(self.SETTINGS_FILE_PATH, 'r').read()
        return SettingsIface(json.loads(settings_json))
