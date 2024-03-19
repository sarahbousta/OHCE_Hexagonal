import pytest
from translator import TranslatorWrapper
from ohce import Ohce
from datetime import datetime

class MockTranslator:
    def translate(self, text, dest):

        translations = {
            "Bien dit!": "Bien dit!",

        }

        translation_text = translations.get(text, text[::-1])

        class MockTranslation:
            def __init__(self, text):
                self.text = translation_text

        return MockTranslation(text)

@pytest.fixture(autouse=True)
def mock_translator(monkeypatch):

    monkeypatch.setattr("translator.Translator", MockTranslator)

def test_translator_wrapper():
    translator = TranslatorWrapper()
    assert translator.translate("Hello", "fr") == "olleH", "The translated text should be reversed."

class MockDateTime:
    @staticmethod
    def now():
        return datetime(2021, 1, 1, 7)  

@pytest.fixture(autouse=True)
def mock_datetime(monkeypatch):

    monkeypatch.setattr("ohce.datetime", MockDateTime)

def test_ohce_greet_morning():
    ohce = Ohce("fr")
    assert ohce.greet() == "Bonjour"[::-1]

def test_ohce_echo_palindrome():
    ohce = Ohce("fr")

    assert ohce.echo("level") == "level (Bien dit!)", "Should recognize a palindrome and add the praise."

def test_ohce_farewell():
    ohce = Ohce("fr")
    assert ohce.farewell() == "Au revoir"[::-1], "Should return the farewell text reversed."