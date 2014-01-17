from aquarius.output.console.ConsoleStrings import ConsoleStrings
from aquarius.output.console.SearchScreen import SearchScreen
from aquarius.output.console.FirstLetterScreen import FirstLetterScreen


class Console(object):
    """The console output module"""
    __menu_main_search = "1"
    __menu_main_startswith = "2"
    __menu_main_harvest = "3"
    __menu_main_quit = "0"
    
    def __init__(self, app, config):
        """Set initial object state"""
        self.__strings = ConsoleStrings()
        self.__app = app
        self.__config = config
        self.__searchScreen = SearchScreen(self.__app)
        self.__firstLetterScreen = FirstLetterScreen(self.__app)

    def main(self):
        """The entry point for the console output module"""
        try:
            self.__main_menu()
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass
            
    def __main_menu(self):
        print(self.__strings.get_main_menu())
        s = self.input()        
        self.__process_main_menu_input(s)
        
    @staticmethod
    def input():
        return input()
    
    def __process_main_menu_input(self, user_input):
        if user_input == self.__menu_main_search:
            self.__searchScreen.main()
        elif user_input == self.__menu_main_startswith:
            self.__firstLetterScreen.main()
        elif user_input == self.__menu_main_harvest:
            self.__app.HarvestBooks()
        elif user_input == self.__menu_main_quit:
            return
        self.__main_menu()
        
    def set_search_screen(self, search_object):
        """Sets the object that is to be used for the search screen"""
        self.__searchScreen = search_object

    def set_first_letter_screen(self, first_letter_object):
        """Sets the object that is to be used fo the first letter screen"""
        self.__firstLetterScreen = first_letter_object
