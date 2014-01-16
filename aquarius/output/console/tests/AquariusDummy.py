from aquarius.Aquarius import Aquarius


class AquariusDummy(Aquarius):
    """A dummy stand-in for Aquarius. Provides canned return
    values for functions and spying capabilities for function calls"""
    def __init__(self):
        """Common setup operations"""
        super().__init__("hardcoded", None, None)
        self.searchbookscalled = False
        self.listbooksbyfirstlettercalled = False

    def ListBooksByFirstLetter(self, firstLetter):
        """Stand-in for Aquarius.ListBooksByFirstLetter"""
        self.listbooksbyfirstlettercalled = True
        return []

    def SearchBooks(self, searchterm):
        """Stand-in for Aquarius.SearchBooks"""
        self.searchbookscalled = True
        return []
