class PdfReaderSpy(object):

    def __init__(self, stream):
        self.constructor_called = True
        self.get_document_info_called = False

    def getDocumentInfo(self):
        self.get_document_info_called = True
        return {"/Author" : "Bob", "/Title" : "Bob's Book"}