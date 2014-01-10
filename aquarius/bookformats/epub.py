from lxml import etree
import zipfile


class epub(object):
    
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__title = ""
        self.__author = ""          
        self.__load()
        
    @property
    def Title(self):
        return self.__title    
    
    @property
    def Author(self):
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
        
    def __read_file_from_zip(self, fileName):
        with self.__zipFile.open(fileName) as f:
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
    def __get_item_from_epub_meta_data(x, attributeName):
        titlexp = "//*[local-name()='package']/*[local-name()='metadata']/*[local-name()='%s']" % attributeName
        return x.xpath(titlexp)[0].text
