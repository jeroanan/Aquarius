from aquarius.bookformats.epubcreator import EpubCreator


class EpubCreatorSpy(EpubCreator):
    """This object acts as a stand-in for EpubCreator when running
    unit tests against BookFactory. It records which methods were
    called, which the tests can assert on later."""
    def __init__(self):
        self.createcalled = False

    def create(self, filepath):
        """Spy on the Create method"""
        self.createcalled = True