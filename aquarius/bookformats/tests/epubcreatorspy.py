class EpubCreatorSpy(object):

    def __init__(self):
        self.createcalled = False

    def create(self, filepath):
        self.createcalled = True