import pytest
import json
from unittest.mock import patch, MagicMock
from src.CLI.console_interface import ConsoleInterface

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

def test_start_console_interface(translator_wrapper_mock, language_config_mock, console_messages_mock, capsys, monkeypatch):
    monkeypatch.setattr("config.config_manager.ConfigManager.__init__", lambda self, config_file=None: None)
    monkeypatch.setattr("config.config_manager.ConfigManager.get_language", lambda self: "fr")
    monkeypatch.setattr("localization.localization_manager.LocalizationManager.__init__", lambda self, messages_file=None, language='en': None)
    monkeypatch.setattr("localization.localization_manager.LocalizationManager.load_messages", lambda self: None)
    monkeypatch.setattr("localization.localization_manager.LocalizationManager.get_message", lambda self, message_key, translator, language: message_key)
    monkeypatch.setattr("core.ohce.Clock.get_hour", lambda *args, **kwargs: 9)

    def echo_side_effect(text):
        if text == "bob":
            return 'bob (Bien dit!)'
        elif text == "test input":
            return 'tupni tset'
        else:
            return text[::-1]

    with patch('src.CLI.console_interface.Ohce', autospec=True) as mock_ohce_class, \
         patch('builtins.input', side_effect=["bob", "test input", 'exit']):
        
        mock_ohce_class.return_value.greet.return_value = 'Bonjour'
        # mock_ohce_class.return_value.echo.return_value = 'bob (Bien dit!)'
        mock_ohce_class.return_value.echo.side_effect = echo_side_effect
        mock_ohce_class.return_value.farewell.return_value = 'Au revoir'
        
        console_interface = ConsoleInterface()
        console_interface.start()

        captured = capsys.readouterr()
        assert "Bonjour\nbob (Bien dit!)\ntupni tset\nfarewell_message\nAu revoir\n" in captured.out
        assert "bob (Bien dit!)" in captured.out
        assert "Au revoir" in captured.out

