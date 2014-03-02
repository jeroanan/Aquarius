from aquarius.output.console.ConsoleStrings import ConsoleStrings


class ConsoleScreen(object):
    """Superclass for screens in the console output module"""

    def __init__(self, app):
        """Set initial class state"""
        self.__app = app
        self.__strings = ConsoleStrings()

    def input(self):
        """Override for the python input statement"""
        return input()

    def SetStringsObject(self, strings_object):
        """Sets the object that holds the strings to be output"""
        self.__strings = strings_object

    def get_strings(self):
        """Gets the object that holds the strings to be output"""
        return self.__strings

    def get_app(self):
        """Gets the object that's used as the main application"""
        return self.__app
