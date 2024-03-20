import sys
from api_interface import app as api_app
from console_interface import ConsoleInterface
from translator import TranslatorWrapper

if __name__ == '__main__':
    translator = TranslatorWrapper()
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        api_app.run(debug=True)
    else:
        console = ConsoleInterface()
        console.start()