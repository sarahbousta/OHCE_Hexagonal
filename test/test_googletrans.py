import pytest
from unittest.mock import patch, MagicMock
from translator import TranslatorWrapper

# Simuler la réponse de la bibliothèque googletrans
@pytest.fixture
def mock_googletrans_response():
    class MockResponse:
        def __init__(self, text):
            self.text = text
    return MockResponse

# Fonction de test pour vérifier que la traduction est correctement retournée
def test_translate_text(mock_googletrans_response):
    # On crée un mock pour l'objet Translator de googletrans
    with patch('translator.Translator') as MockTranslator:
        # On simule la méthode translate de l'objet Translator
        mock_translator_instance = MockTranslator.return_value
        mock_translator_instance.translate.return_value = mock_googletrans_response("test translation")
        
        # On instancie notre wrapper et on appelle la méthode translate
        translator = TranslatorWrapper()
        translation = translator.translate("test", target_language="en")
        
        # On vérifie que le résultat est celui attendu
        assert translation == "test translation"
        # On vérifie que la méthode translate a été appelée avec les bons paramètres
        mock_translator_instance.translate.assert_called_with("test", dest="en")
