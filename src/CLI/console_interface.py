from config.config_manager import ConfigManager
from localization.localization_manager import LocalizationManager
from CLI.console_manager import ConsoleManager
from CLI.command_processor import CommandProcessor
from core.ohce import Ohce
from translation.translator import TranslatorWrapper

class ConsoleInterface:
    def __init__(self):
        # Configuration et internationalisation
        self.config_manager = ConfigManager()
        self.language = self.config_manager.get_language()
        self.localization_manager = LocalizationManager(language=self.language)
        
        # Création du traducteur
        self.translator = TranslatorWrapper()

        # Gestion de la console et du traitement des commandes
        self.console_manager = ConsoleManager(self.localization_manager)
        self.ohce = Ohce(language=self.language)
        self.command_processor = CommandProcessor(self.ohce, self.console_manager)

    def start(self):
        # Affiche le message de salutation d'Ohce
        print(self.ohce.greet())

        try:
            while True:
                # Obtient l'entrée de l'utilisateur et traite les commandes
                user_input = self.console_manager.get_input('prompt_input', self.translator, self.language)
                should_exit = self.command_processor.process_input(user_input, self.language)
                if should_exit:
                    break
        except KeyboardInterrupt:
            # Gère l'interruption par Ctrl+C proprement
            print(self.ohce.farewell())