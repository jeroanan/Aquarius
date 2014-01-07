from aquarius.output.console.consolestrings import consolestrings


class ConsoleScreen(object):

    def __init__(self, app):
        self.__app = app
        self.__strings = consolestrings()

    @staticmethod
    def input():
        return input()

    def SetStringsObject(self, stringsobject):
        self.__strings = stringsobject

    def get_strings(self):
        return self.__strings

    def get_app(self):
        return self.__app
