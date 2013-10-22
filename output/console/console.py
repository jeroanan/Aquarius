from output.console.consolestrings import consolestrings

class console(object):      
 
    __menu_main_search = "1"

    def __init__(self, app):
        self.__strings = consolestrings()
        
    def Main(self):
        self.__MainMenu()
        
    def __MainMenu(self):
        print(self.__strings.GetMainMenu())
        s = input()
        self.__processMainMenuInput(s)
        
    def __processMainMenuInput(self, userInput):
        if userInput == self.__menu_main_search:
            self.__SearchScreen()
        else:
            self.__MainMenu()
        
    def __SearchScreen(self):
        print(self.__strings.GetSearchString())
        s = input()
        self.__MainMenu()

    

    