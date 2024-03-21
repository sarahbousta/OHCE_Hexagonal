import json
from translation.translator import TranslatorWrapper
from core.clock import Clock
import os

class Ohce:
    def __init__(self, language="fr"):
        self.language = language
        self.translator = TranslatorWrapper()
        self.greetings = self.load_greetings()
        self.clock = Clock()

    @staticmethod
    def load_greetings():
        with open(os.path.join('config/greetings.json'), 'r', encoding='utf-8') as f:
            return json.load(f)


    def translate_message(self, key):
        return self.translator.translate(self.greetings[key], self.language)

    def greet(self):
        current_hour = self.clock.get_hour()
        greeting_key = self.clock.what_part_of_day(current_hour).value
        return self.translate_message(greeting_key)

    def echo(self, text):
        well_said = self.translate_message('well_said')
        reversed_text = text[::-1]
        return reversed_text + (f" ({well_said})" if self.is_palindrome(text) else "")

    def farewell(self):
        return self.translate_message('farewell')

    @staticmethod
    def is_palindrome(text):
        normalized_text = ''.join(filter(str.isalnum, text)).lower()
        return normalized_text == normalized_text[::-1]
