from lxml import etree
import zipfile


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
        self.__zipFile = zipfile.ZipFile(self.__fileName, 'r')
        self.__get_book_meta_data()
        self.__set_book_details()
    
    def __get_book_meta_data(self):
        self.__bookMetaData = self.__read_file_from_zip(self.__get_root_file_path())
    
    def __get_root_file_path(self):
        container = etree.fromstring(self.__get_container_file_content())
        xp = "//*[local-name()='container']/*[local-name()='rootfiles']/*[local-name()='rootfile']"
        return container.xpath(xp)[0].get("full-path")                
    
    def __get_container_file_content(self):
        return self.__read_file_from_zip("META-INF/container.xml")
        
    def __read_file_from_zip(self, filename):
        with self.__zipFile.open(filename) as f:
            return f.read()
    
    def __set_book_details(self):
        x = etree.fromstring(self.__bookMetaData)
        self.__get_epub_title(x)
        self.__get_epub_author(x)
        
    def __get_epub_title(self, x):
        self.__title = self.__get_item_from_epub_meta_data(x, "title")

    def __get_epub_author(self, x):
        self.__author = self.__get_item_from_epub_meta_data(x, "creator")

    @staticmethod
    def __get_item_from_epub_meta_data(x, attributename):
        titlexp = "//*[local-name()='package']/*[local-name()='metadata']/*[local-name()='%s']" % attributename
        return x.xpath(titlexp)[0].text