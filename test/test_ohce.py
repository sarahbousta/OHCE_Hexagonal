import pytest
import json
from unittest.mock import Mock, patch
from ohce import Ohce
from clock import Clock, PartOfDay

# Fixture pour mocker Clock et configurer les retours nécessaires pour les tests
@pytest.fixture
def mock_clock(mocker):
    clock_mock = Mock(spec=Clock)
    # Pas besoin de mocker get_hour directement puisqu'on mocke what_part_of_day qui utilise cette valeur
    mocker.patch('ohce.Clock', return_value=clock_mock)
    return clock_mock

# Fixture pour créer un fichier de salutations mocké
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

# Fixture pour mocker TranslatorWrapper
@pytest.fixture
def mock_translator(mocker):
    translator_mock = Mock()
    translator_mock.translate = Mock(side_effect=lambda text, lang: text)
    mocker.patch('ohce.TranslatorWrapper', return_value=translator_mock)
    return translator_mock

# Test greet après-midi
def test_greet_afternoon(mock_translator, mock_greetings_json, mock_clock):
    mock_clock.what_part_of_day.return_value = PartOfDay.AFTERNOON
    ohce = Ohce(language="fr")
    ohce.greetings = json.load(open(mock_greetings_json))
    assert ohce.greet() == "Bon après-midi"

# Test greet soir
def test_greet_evening(mock_translator, mock_greetings_json, mock_clock):
    mock_clock.what_part_of_day.return_value = PartOfDay.EVENING
    ohce = Ohce(language="fr")
    ohce.greetings = json.load(open(mock_greetings_json))
    assert ohce.greet() == "Bonsoir"

# Test echo avec palindrome
def test_echo_with_palindrome(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    ohce.greetings = json.load(open(mock_greetings_json))
    assert ohce.echo("kayak") == "kayak (Bien dit!)"

# Test echo sans palindrome
def test_echo_without_palindrome(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    ohce.greetings = json.load(open(mock_greetings_json))
    assert ohce.echo("bonjour") == "ruojnob"

# Test farewell
def test_farewell(mock_translator, mock_greetings_json):
    ohce = Ohce(language="fr")
    ohce.greetings = json.load(open(mock_greetings_json))
    assert ohce.farewell() == "Au revoir"

# Test is_palindrome
def test_is_palindrome_true():
    assert Ohce.is_palindrome("kayak") == True

def test_is_palindrome_false():
    assert Ohce.is_palindrome("python") == False
