# Cette classe est responsable de lire, 
# écrire et fournir des accès aux différentes 
# configurations de l'application, comme la langue par défaut.

import json
import locale

class ConfigManager:
    def __init__(self, config_file='config.json'):
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
