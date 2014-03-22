import zipfile

from lxml import etree


class Epub(object):

    def __init__(self, filename):
        self.__fileName = filename
        self.__title = ""
        self.__author = ""
        self.__rights = ""
        self.__identifier = ""
        self.__language = ""
        self.__zipFile = None
        self.__bookMetaData = None
        self.__load()

    @property
    def title(self):
        return self.__title    
    
    @property
    def author(self):
        return self.__author

    @property
    def rights(self):
        return self.__rights

    @property
    def identifier(self):
        return self.__identifier

    @property
    def language(self):
        return self.__language

    def __load(self):
        self.__zipFile = zipfile.ZipFile(self.__fileName, 'r')
        self.__get_book_meta_data()
        self.__set_book_details()
    
    def __get_book_meta_data(self):
        self.__bookMetaData = self.__read_file_from_epub(self.__get_root_file_path())
    
    def __get_root_file_path(self):
        container = etree.fromstring(self.__get_container_file_content())
        xp = "//*[local-name()='container']/*[local-name()='rootfiles']/*[local-name()='rootfile']"
        return container.xpath(xp)[0].get("full-path")                

    def __get_container_file_content(self):
        return self.__read_file_from_epub("META-INF/container.xml")
        
    def __read_file_from_epub(self, filename):
        with self.__zipFile.open(filename) as f:
            return f.read()
    
    def __set_book_details(self):
        x = etree.fromstring(self.__bookMetaData)
        self.__title = self.__get_item_from_epub_meta_data(x, "title")
        self.__author = self.__get_item_from_epub_meta_data(x, "creator")
        self.__rights = self.__get_item_from_epub_meta_data(x, "rights")
        self.__identifier = self.__get_item_from_epub_meta_data(x, "identifier")
        self.__language = self.__get_item_from_epub_meta_data(x, "language")

    @staticmethod
    def __get_item_from_epub_meta_data(x, attributename):
        titlexp = "//*[local-name()='package']/*[local-name()='metadata']/*[local-name()='%s']" \
                  % attributename
        return x.xpath(titlexp)[0].text
