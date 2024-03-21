class ConsoleManager:
    def __init__(self, localization_manager):
        self.localization_manager = localization_manager

    def print_message(self, message_key, translator, language):
        print(self.localization_manager.get_message(message_key, translator, language))

    def get_input(self, prompt_key, translator, language):
        input_prompt = self.localization_manager.get_message(prompt_key, translator, language)
        return input(input_prompt)
