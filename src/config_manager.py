import json
import locale
import os

class ConfigManager:
    def __init__(self, config_file=os.path.join('../config/config.json')):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_language(self):
        return self.config.get('language', locale.getdefaultlocale()[0][:2])
