from output.console.consolestrings import consolestrings
from output.console.searchscreen import searchscreen

class console(object):      
 
    __menu_main_search = "1"

    def __init__(self, app):
        self.__strings = consolestrings()
        self.__app = app
        
    def Main(self):
        try:
            self.__MainMenu()
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass
            
    def __MainMenu(self):
        print(self.__strings.GetMainMenu())
        s = input()
        self.__processMainMenuInput(s)
        
    def __processMainMenuInput(self, userInput):
        if userInput == self.__menu_main_search:
            searchscreen(self.__app).Main()
        self.__MainMenu()
        
    