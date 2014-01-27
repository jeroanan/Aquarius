import zipfile

from lxml import etree


class Epub(object):
    """Load metadata from a .epub file. Set object state to that metadata"""
    def __init__(self, filename):
        """Take the filename and load it right away"""
        self.__fileName = filename
        self.__title = ""
        self.__author = ""
        self.__zipFile = None
        self.__bookMetaData = None
        self.__load()
        
    @property
    def title(self):
        """The title of the loaded book"""
        return self.__title    
    
    @property
    def author(self):
        """The author of the loaded book"""
        return self.__author
    
    def __load(self):
        """Load the epub"""
        self.__zipFile = zipfile.ZipFile(self.__fileName, 'r')
        self.__get_book_meta_data()
        self.__set_book_details()
    
    def __get_book_meta_data(self):
        """"Reads the metadata file from the epub"""
        self.__bookMetaData = self.__read_file_from_epub(self.__get_root_file_path())

    
    def __get_root_file_path(self):
        """Locates the metadata file in the epub"""
        container = etree.fromstring(self.__get_container_file_content())
        xp = "//*[local-name()='container']/*[local-name()='rootfiles']/*[local-name()='rootfile']"
        return container.xpath(xp)[0].get("full-path")                

    def __get_container_file_content(self):
        """Get the contents of the container file. The container file contains
    the path to the metadata"""
        return self.__read_file_from_epub("META-INF/container.xml")
        
    def __read_file_from_epub(self, filename):
        """Reads the given file from the epub. Epub files are zip files."""
        with self.__zipFile.open(filename) as f:
            return f.read()
    
    def __set_book_details(self):
        """Sets the object state to reflect the metadata stored in the epub"""
        x = etree.fromstring(self.__bookMetaData)
        self.__get_epub_title(x)
        self.__get_epub_author(x)
        
    def __get_epub_title(self, x):
        """Gets the title from the epub's metadata"""
        self.__title = self.__get_item_from_epub_meta_data(x, "title")

    def __get_epub_author(self, x):
        """Get the author from the epub's metadata"""
        self.__author = self.__get_item_from_epub_meta_data(x, "creator")

    @staticmethod
    def __get_item_from_epub_meta_data(x, attributename):
        """Get the given attribute from the epub's metadata"""
        titlexp = "//*[local-name()='package']/*[local-name()='metadata']/*[local-name()='%s']" \
                  % attributename
        return x.xpath(titlexp)[0].text
