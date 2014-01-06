from aquarius.output.console.consolestrings import consolestrings


class ConsoleStringsMock(consolestrings):

    def __init__(self):
        self.getsearchstringcalled = False
        self.getsearchresulttitlestringcalled = False
        self.getsearchresultfooterstringcalled = False
        self.getfirstletterstringcalled = False

    def verify_printedsearchresults(self):
        return self.getsearchstringcalled and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def verify_printedfirstletterscreen(self):
        return self.getfirstletterstringcalled and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def GetSearchResultTitleString(self):
        self.getsearchresulttitlestringcalled = True
        return None

    def GetSearchResultFooterString(self, numberofresults):
        self.getsearchresultfooterstringcalled = True
        return None

    def GetSearchString(self):
        self.getsearchstringcalled = True
        return None

    def GetFirstLetterString(self):
        self.getfirstletterstringcalled = True
        return None