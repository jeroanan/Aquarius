from aquarius.bookformats.Pdf import Pdf
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class PdfCreator(object):

    def __init__(self):
        pass

    def create(self, filepath):
        p = Pdf(filepath)
        b = book()
        try:
            p.load()
            self.__addFormat(b, filepath)
        except FileNotFoundError:
            b = None
        return b

    def __addFormat(self, b, filepath):
        bf = bookformat()
        bf.Format = "PDF"
        bf.Location = filepath
        b.Formats = [bf]