from aquarius.output.console.consolestrings import consolestrings


class ConsoleStringsMock(consolestrings):
    """A Mock object for the ConsoleStrings class. Verifies that various
    console screens have been rendered based on multiple function calls to
    ConsoleStrings."""
    def __init__(self):
        """Set initial object state"""
        self.getsearchstringcalled = False
        self.getsearchresulttitlestringcalled = False
        self.getsearchresultfooterstringcalled = False
        self.getfirstletterstringcalled = False

    def verify_printedsearchresults(self):
        """Verifies that the search results console screen has been
        fully rendered."""
        return self.getsearchresulttitlestringcalled and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def verify_printedfirstletterscreen(self):
        """Verifies that the first letter console screen has been
        fully rendered."""
        return self.getfirstletterstringcalled and self.getsearchresulttitlestringcalled \
            and self.getsearchresultfooterstringcalled

    def GetSearchResultTitleString(self):
        """Spy for ConsoleStrings.GetSearchResultTitleString"""
        self.getsearchresulttitlestringcalled = True
        return None

    def GetSearchResultFooterString(self, numberofresults):
        """Spy for ConsoleStrings.GetSearchResultFooterString"""
        self.getsearchresultfooterstringcalled = True
        return None

    def GetSearchString(self):
        """Spy for ConsoleStrings.GetSearchString"""
        self.getsearchstringcalled = True
        return None

    def GetFirstLetterString(self):
        """Spy for ConsoleStrings.GetFirstLetterString"""
        self.getfirstletterstringcalled = True
        return None