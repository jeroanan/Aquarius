from output.console.consolestrings import consolestrings

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
            self.__SearchScreen()
            self.__MainMenu()
        else:
            self.__MainMenu()   
    
    def __SearchScreen(self):
        print(self.__strings.GetSearchString())
        s = input()
        self.__app.SearchBooks(s, self.__SearchResultsScreen)        
        
    def __SearchResultsScreen(self, results):
        print(self.__strings.GetSearchResultTitleString())
        i = 0
        for result in results:
            i += 1
            print(result.Title)    
            
        print(self.__strings.GetSearchResultFooterString(i))
    