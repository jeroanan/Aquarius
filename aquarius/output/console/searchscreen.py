from aquarius.output.console.consolestrings import consolestrings

class searchscreen:
    
    def __init__(self, app):
        self.__app = app
        self.__strings = consolestrings()
        
    def Main(self):
        print(self.__strings.GetSearchString())
        s = input()
        results = self.__app.SearchBooks(s)
        self.__SearchResultsScreen(results)        
        
    def __SearchResultsScreen(self, results):
        print(self.__strings.GetSearchResultTitleString())
        i = 0
        for result in results:
            i += 1
            print(result.Title)
        print(self.__strings.GetSearchResultFooterString(i))