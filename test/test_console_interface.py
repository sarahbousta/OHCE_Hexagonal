import pytest
import json
from unittest.mock import patch, MagicMock
from console_interface import ConsoleInterface

@pytest.fixture
def translator_wrapper_mock():
    mock = MagicMock()
    mock.translate.side_effect = lambda message_key, language: message_key
    return mock

@pytest.fixture
def language_config_mock(tmpdir):
    config_file = tmpdir.join("config.json")
    config_file.write('{"language": "fr"}')
    return str(config_file)

@pytest.fixture
def console_messages_mock(tmpdir):
    messages_file = tmpdir.join("console_messages.json")
    messages_content = {
        "prompt_input": "prompt_input",
        "farewell_message": "farewell_message"
    }
    messages_file.write(json.dumps(messages_content))
    return str(messages_file)

def test_start_console_interface(translator_wrapper_mock, language_config_mock, console_messages_mock, capsys):
    with patch('console_interface.Ohce', autospec=True) as mock_ohce_class, \
         patch('builtins.input', side_effect=["test input", 'exit']):
        
        mock_ohce_class.return_value.greet.return_value = 'Bonjour'
        mock_ohce_class.return_value.echo.return_value = 'bob (Bien dit!)'
        mock_ohce_class.return_value.farewell.return_value = 'Au revoir'
        
        console_interface = ConsoleInterface(translator_wrapper_mock)
        console_interface.config_file = language_config_mock
        console_interface.console_messages_file = console_messages_mock
        console_interface.start()

        captured = capsys.readouterr()
        assert "Bonjour\nbob (Bien dit!)\nAu revoir\n" in captured.out
        assert "bob (Bien dit!)" in captured.out
        assert "Au revoir" in captured.out

