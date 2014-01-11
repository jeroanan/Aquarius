from PyPDF2 import PdfFileReader


class PdfReaderSpy(PdfFileReader):
    """This object acts as a stand-in for PdfReader when running
    unit tests against Pdf. It records which methods were
    called, which the tests can assert on later."""
    def __init__(self, stream):
        """Set the spy's starting state"""
        self.constructor_called = True
        self.get_document_info_called = False

    def getDocumentInfo(self):
        """Record that getDocumentInfo was called. Return a dummy value"""
        self.get_document_info_called = True
        return {"/Author" : "Bob", "/Title" : "Bob's Book"}