import pytest
import json
from unittest.mock import Mock, patch
from ohce import Ohce

# Préparer un fichier greetings.json mock pour les tests
@pytest.fixture(scope='module')
def mock_greetings_json(tmpdir_factory):
    greetings_content = {
        "morning": "Bonjour",
        "afternoon": "Bon après-midi",
        "evening": "Bonsoir",
        "farewell": "Au revoir",
        "well_said": "Bien dit!"
    }
    file = tmpdir_factory.mktemp("data").join("greetings.json")
    file.write(json.dumps(greetings_content))
    return str(file)

# Initialiser le mock de TranslatorWrapper avant chaque test
@pytest.fixture
def mock_translator(mocker):
    translator_mock = Mock()
    translator_mock.translate = Mock(side_effect=lambda text, lang: text)  # Simule une traduction par identité
    mocker.patch('ohce.TranslatorWrapper', return_value=translator_mock)
    return translator_mock

# Tests pour la méthode greet
def test_greet_morning(mock_translator, mock_greetings_json):
    # Simuler datetime pour retourner une heure du matin
    with patch('ohce.datetime') as mock_datetime:
        mock_datetime.now.return_value.hour = 9
        ohce = Ohce(language="fr")
        assert ohce.greet() == "Bonjour"

def test_greet_afternoon(mock_translator, mock_greetings_json):
    with patch('ohce.datetime') as mock_datetime:
        mock_datetime.now.return_value.hour = 13
        ohce = Ohce(language="fr")
        assert ohce.greet() == "Bon après-midi"

def test_greet_evening(mock_translator, mock_greetings_json):
    with patch('ohce.datetime') as mock_datetime:
        mock_datetime.now.return_value.hour = 19
        ohce = Ohce(language="fr")
        assert ohce.greet() == "Bonsoir"

# Tests pour la méthode echo
def test_echo_with_palindrome(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    assert ohce.echo("kayak") == "kayak (Bien dit!)"

def test_echo_without_palindrome(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    assert ohce.echo("hello") == "hello"

# Test pour la méthode farewell
def test_farewell(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    assert ohce.farewell() == "Au revoir"

# Test pour la méthode is_palindrome
def test_is_palindrome():
    assert Ohce.is_palindrome("kayak") == True
    assert Ohce.is_palindrome("hello") == False
