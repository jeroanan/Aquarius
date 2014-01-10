from aquarius.output.console.consolestrings import consolestrings
from aquarius.output.console.searchscreen import searchscreen
from aquarius.output.console.firstletterscreen import firstletterscreen


class console(object):      
 
    __menu_main_search = "1"
    __menu_main_startswith = "2"
    __menu_main_harvest = "3"
    __menu_main_quit = "0"
    
    def __init__(self, app, config):
        self.__strings = consolestrings()
        self.__app = app
        self.__config = config
        self.__searchScreen = searchscreen(self.__app)
        self.__firstLetterScreen = firstletterscreen(self.__app)

    def Main(self):
        try:
            self.__main_menu()
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass
            
    def __main_menu(self):
        print(self.__strings.GetMainMenu())
        s = self.input()        
        self.__process_main_menu_input(s)
        
    def input(self):
        return input()
    
    def __process_main_menu_input(self, userInput):
        if userInput == self.__menu_main_search:
            self.__searchScreen.Main()
        elif userInput == self.__menu_main_startswith:
            self.__firstLetterScreen.Main()
        elif userInput == self.__menu_main_harvest:
            self.__app.HarvestBooks()
        elif userInput == self.__menu_main_quit:
            return
        self.__main_menu()
        
    def SetSearchScreen(self, searchobject):
        self.__searchScreen = searchobject

    def SetFirstLetterScreen(self, firstletterobject):
        self.__firstLetterScreen = firstletterobject
