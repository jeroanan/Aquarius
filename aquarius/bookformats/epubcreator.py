from zipfile import BadZipFile

from aquarius.bookformats.epub import epub
from aquarius.objects.book import book
from aquarius.objects.bookformat import bookformat


class EpubCreator(object):

    def create(self, filepath):
        b = None
        try:
            e = epub(filepath)
            b = book()
            self.__addBookProperties(b, e)
            self.__addEpubFormat(filepath, b)
        except BadZipFile:
            pass
        except OSError:
            pass
        return b

    def __addBookProperties(self, b, epub):
        b.Author = epub.Author
        b.Title = epub.Title

    def __addEpubFormat(self, filepath, b):
        bf = bookformat()
        bf.Format = "EPUB"
        bf.Location = filepath
        b.Formats = [bf]