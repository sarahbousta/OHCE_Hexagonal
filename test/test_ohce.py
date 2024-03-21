import pytest
import json
from unittest.mock import Mock
from src.core.ohce import Ohce
from src.core.clock import PartOfDay

@pytest.fixture
def mock_clock(mocker):
    clock_mock = Mock()
    mocker.patch('src.core.ohce.Clock', return_value=clock_mock)
    return clock_mock

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

@pytest.fixture
def mock_translator(mocker):
    translator_mock = Mock()
    translator_mock.translate = Mock(side_effect=lambda text, lang: text)
    mocker.patch('src.core.ohce.TranslatorWrapper', return_value=translator_mock)
    return translator_mock
