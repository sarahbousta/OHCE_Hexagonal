from translator import TranslatorWrapper as translator

class CommandProcessor:
    def __init__(self, ohce, console_manager):
        self.ohce = ohce
        self.console_manager = console_manager
        self.translator = translator()

    def process_input(self, user_input, language):
        if user_input.lower() == 'exit':
            self.console_manager.print_message('farewell_message', self.translator, language)
            print(self.ohce.farewell())
            return True
        else:
            print(self.ohce.echo(user_input))
            return False
