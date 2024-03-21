from googletrans import Translator

class TranslatorWrapper:
    def __init__(self):
        self.translator = Translator()
    
    def translate(self, text, target_language):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text