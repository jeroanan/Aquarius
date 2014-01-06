from aquarius.output.console.consolestrings import consolestrings


class searchscreen:
    
    def __init__(self, app):
        self.__app = app
        self.__strings = consolestrings()
        
    def Main(self):
        print(self.__strings.GetSearchString())
        s = self.input()
        results = self.__app.SearchBooks(s)
        self.__SearchResultsScreen(results)

    def input(self):
        return input()

    def __SearchResultsScreen(self, results):
        print(self.__strings.GetSearchResultTitleString())
        i = 0
        for result in results:
            i += 1
            print(result.Title)
        print(self.__strings.GetSearchResultFooterString(i))

    def SetStringsObject(self, stringsobject):
        self.__strings = stringsobject