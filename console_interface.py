import json
import locale
from translator import TranslatorWrapper
from ohce import Ohce

class ConsoleInterface:
    def __init__(self, translator):
        self.config_file = 'config.json'
        self.console_messages_file = 'console_messages.json'
        self.ohce = None
        self.translator = translator
        self.load_messages()
        self.language = self.load_language()
        

    def load_language(self):
        # Essaie de charger la langue du fichier de configuration ou utiliser la langue du système
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('language', locale.getdefaultlocale()[0][:2])
        except FileNotFoundError:
            return locale.getdefaultlocale()[0][:2]

    def load_messages(self):
        # Charge les identifiants de message à partir du fichier JSON
        with open(self.console_messages_file, 'r', encoding='utf-8') as f:
            self.messages = json.load(f)

    def get_message(self, message_key):
        # Obtient'identifiant du message et le traduit
        message_id = self.messages.get(message_key, message_key)
        return self.translator.translate(message_id, self.language)

    def start(self):
        self.ohce = Ohce(language=self.language)
        print(self.ohce.greet())

        input_prompt = self.get_message('prompt_input')
        try:
            while True:
                user_input = input(input_prompt)
                if user_input.lower() == 'exit':
                    print(self.ohce.farewell())
                    break
                else:
                    print(self.ohce.echo(user_input))
        except KeyboardInterrupt:
            farewell_message = self.get_message('farewell_message')
            print(farewell_message + self.ohce.farewell())
