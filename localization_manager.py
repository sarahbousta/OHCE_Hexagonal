# cette classe encapsule l'internationalisation.
# Cela inclut la charge des messages depuis 
# console_messages.json et leur traduction en 
# fonction de la langue sélectionnée. Une telle 
# classe pourrait s'appeler LocalizationManager.
import json

class LocalizationManager:
    def __init__(self, messages_file='console_messages.json', language='en'):
        self.messages_file = messages_file
        self.language = language
        self.messages = self.load_messages()

    def load_messages(self):
        with open(self.messages_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_message(self, message_key, translator, language):
        message_id = self.messages.get(message_key, message_key)
        return translator.translate(text=message_id, target_language=language)


    