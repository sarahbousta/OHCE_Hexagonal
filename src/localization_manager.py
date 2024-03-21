import json
import os

class LocalizationManager:
    def __init__(self, messages_file=os.path.join('config/console_messages.json'), language='en'):
        self.messages_file = messages_file
        self.language = language
        self.messages = self.load_messages()

    def load_messages(self):
        with open(self.messages_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_message(self, message_key, translator, language):
        message_id = self.messages.get(message_key, message_key)
        return translator.translate(text=message_id, target_language=language)
