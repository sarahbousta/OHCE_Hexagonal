import sys
from API.api_interface import app as api_app
from CLI.console_interface import ConsoleInterface
from translator import TranslatorWrapper

if __name__ == '__main__':
    translator = TranslatorWrapper()
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        api_app.run(debug=True, port=5000)
    else:
        console = ConsoleInterface()
        console.start()