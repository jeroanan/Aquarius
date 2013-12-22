from lxml import etree
import zipfile
from objects.book import book
from objects.bookformat import bookformat

class epub(object):
    
    def __init__(self, fileName):
        print(fileName)
        self.__zipFile = zipfile.ZipFile(fileName, 'r')  
        self.__book = book()        
        self.__book.Formats= [self.__getBookFormat(fileName)]                              
        
    def __getBookFormat(self, fileName):
        bf = bookformat()
        bf.Format = "EPUB"
        bf.Location = fileName
        return bf
    
    def Load(self):
        self.__getBookMetaData()
        self.__setBookDetails()        
        return self.__book

    def __getBookMetaData(self):
        with self.__zipFile.open(self.__getRootFilePath()) as f:
            self.__bookMetaData = f.read()
    
    def __getRootFilePath(self):
        container = self.__getContainerFileContent()        
        return self.__getAttributeFromFirstTag(container, "rootfile", "full-path")
                
    def __getAttributeFromFirstTag(self, filecontent, tag, attribute):  
        return self.__getFirstTag(filecontent, tag).get(attribute)
    
    def __getContainerFileContent(self):        
        with self.__zipFile.open("META-INF/container.xml") as f:
            content = f.read()
        return content
            
    def __setBookDetails(self):        
        self.__book.Title = self.__getTextFromFirstTag(self.__bookMetaData, "title")
        self.__book.Author = self.__getTextFromFirstTag(self.__bookMetaData, "creator")
        
    def __getTextFromFirstTag(self, filecontent, tag):
        return self.__getFirstTag(filecontent, tag).text
    
    def __getFirstTag(self, filecontent, tag):        
        xml = etree.fromstring(filecontent)
        
        for el in xml.findall(".//*"):
            thetag = etree.QName(el)
                                    
            if thetag.localname == tag:
                return el