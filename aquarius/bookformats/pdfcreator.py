from aquarius.bookformats.Pdf import Pdf
from aquarius.objects.Book import Book
from aquarius.objects.BookFormat import BookFormat


class PdfCreator(object):
    """Loads a pdf file into a book object"""
    def create(self, filepath):
        """Load the given file. Return a book object."""
        p = Pdf(filepath)
        b = Book()
        try:
            p.load()
            b.title = p.title
            b.author = p.author
            self.__add_format(b, filepath)
        except FileNotFoundError:
            b = None
        return b

    @staticmethod
    def __add_format(b, filepath):
        bf = BookFormat()
        bf.Format = "PDF"
        bf.Location = filepath
        b.formats = [bf]