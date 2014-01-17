from aquarius.output.console.ConsoleStrings import ConsoleStrings


class ConsoleStringsMock(ConsoleStrings):
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

    def get_search_result_title_string(self):
        """Spy for ConsoleStrings.GetSearchResultTitleString"""
        self.getsearchresulttitlestringcalled = True
        return None

    def get_search_result_footer_string(self, numberofresults):
        """Spy for ConsoleStrings.GetSearchResultFooterString"""
        self.getsearchresultfooterstringcalled = True
        return None

    def get_search_string(self):
        """Spy for ConsoleStrings.GetSearchString"""
        self.getsearchstringcalled = True
        return None

    def get_first_letter_string(self):
        """Spy for ConsoleStrings.GetFirstLetterString"""
        self.getfirstletterstringcalled = True
        return None