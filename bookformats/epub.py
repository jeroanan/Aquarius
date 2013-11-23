from lxml import etree
import zipfile
from objects.book import book

class epub(object):
    
    def __init__(self, fileName):
        self.__ebook = zipfile.ZipFile(fileName, 'r')  
        self.__book = book()
        
    def Load(self):
        self.__getBookMetaData()
        self.__setBookDetails()
        return self.__book

    def __setBookDetails(self):        
        self.__book.Title = self.__getTextFromFirstTag(self.__bookMetaData, "title")
        self.__book.Author = self.__getTextFromFirstTag(self.__bookMetaData, "creator")
    
    def __getBookMetaData(self):
        with self.__ebook.open(self.__getRootFilePath()) as f:
            self.__bookMetaData = f.read()
    
    def __getRootFilePath(self):
        container = self.__getContainerFileContent()        
        return self.__getAttributeFromFirstTag(container, "rootfile", "full-path")
                
    def __getContainerFileContent(self):        
        with self.__ebook.open("META-INF/container.xml") as f:
            content = f.read()
        return content
    
    def __getAttributeFromFirstTag(self, filecontent, tag, attribute):  
        return self.__getFirstTag(filecontent, tag).get(attribute)
        
    def __getTextFromFirstTag(self, filecontent, tag):
        return self.__getFirstTag(filecontent, tag).text
    
    def __getFirstTag(self, filecontent, tag):        
        xml = etree.fromstring(filecontent)
        
        for el in xml.findall(".//*"):
            thetag = etree.QName(el)
                                    
            if thetag.localname == tag:
                return el