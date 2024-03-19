import json
from datetime import datetime
from translator import TranslatorWrapper

class Ohce:
    def __init__(self, language="fr"):
        self.language = language
        self.translator = TranslatorWrapper()
        # Charger les salutations et les phrases depuis le fichier JSON
        with open('greetings.json', 'r', encoding='utf-8') as f:
            self.greetings = json.load(f)

    def greet(self):
        current_hour = datetime.now().hour
        if 6 <= current_hour < 12:
            greeting_key = 'morning'
        elif 12 <= current_hour < 18:
            greeting_key = 'afternoon'
        else:
            greeting_key = 'evening'
        return self.translator.translate(self.greetings[greeting_key], self.language)

    def echo(self, text):
        well_said = self.translator.translate(self.greetings['well_said'], self.language)
        return text + (f" ({well_said})" if self.is_palindrome(text) else "")

    def farewell(self):
        farewell_key = 'farewell'
        return self.translator.translate(self.greetings[farewell_key], self.language)

    @staticmethod
    def is_palindrome(text):
        normalized_text = ''.join(filter(str.isalnum, text)).lower()
        return normalized_text == normalized_text[::-1]
