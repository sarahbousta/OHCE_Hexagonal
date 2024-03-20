import json
from datetime import datetime
from enum import Enum
from translator import TranslatorWrapper

class PartOfDay(Enum):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    EVENING = 'evening'

class Ohce:
    def __init__(self, language="fr"):
        self.language = language
        self.translator = TranslatorWrapper()
        self.greetings = self.load_greetings()

    @staticmethod
    def load_greetings():
        with open('greetings.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def get_hour():
        return datetime.now().hour
    
    @staticmethod
    def what_part_of_day(hour):
        if 6 <= hour < 12:
            return PartOfDay.MORNING
        elif 12 <= hour < 18:
            return PartOfDay.AFTERNOON
        else:
            return PartOfDay.EVENING

    def translate_message(self, key):
        return self.translator.translate(self.greetings[key], self.language)

    def greet(self):
        current_hour = self.get_hour()
        greeting_key = self.what_part_of_day(current_hour).value
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
