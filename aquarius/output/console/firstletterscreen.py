from output.console.consolestrings import consolestrings

class firstletterscreen(object):
    
    def __init__(self, app):
        self.__app = app
        self.__strings = consolestrings()
        
    def Main(self):
        print(self.__strings.GetFirstLetterString())
        s = input()
        result = self.__app.ListBooksByFirstLetter(s)
        self.__FirstLetterResults(result)
        
    def __FirstLetterResults(self, results):
        print(self.__strings.GetSearchResultTitleString())
        
        i = 0
        for result in results:
            i+=1
            print(result.Title)
        print(self.__strings.GetSearchResultFooterString(i))