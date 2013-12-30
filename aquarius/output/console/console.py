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
        
    def Main(self):
        try:
            self.__MainMenu()
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass
            
    def __MainMenu(self):
        print(self.__strings.GetMainMenu())
        s = self.input()        
        self.__processMainMenuInput(s)
        
    def input(self):
        return input()
    
    def output(self, text):
        print(text)
        
    def __processMainMenuInput(self, userInput):
        if userInput == self.__menu_main_search:
            searchscreen(self.__app).Main()
        elif userInput == self.__menu_main_startswith:
            firstletterscreen(self.__app).Main()
        elif userInput == self.__menu_main_harvest:
            self.__app.HarvestBooks()
        elif userInput == self.__menu_main_quit:
            return
        self.__MainMenu()
        
    