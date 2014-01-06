from aquarius.aquarius import aquarius


class AquariusDummy(aquarius):

    def __init__(self):
        super().__init__("hardcoded", None, None)
        self.searchbookscalled = False
        self.listbooksbyfirstlettercalled = False

    def ListBooksByFirstLetter(self, firstLetter):
        self.listbooksbyfirstlettercalled = True
        return []

    def SearchBooks(self, searchterm):
        self.searchbookscalled = True
        return []
