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
        self.__getBookMetaData()
        self.__setBookDetails()
    
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
        self.__title = self.__getTextFromFirstTag(self.__bookMetaData, "title")
        self.__author = self.__getTextFromFirstTag(self.__bookMetaData, "creator")
        
    def __getTextFromFirstTag(self, filecontent, tag):
        return self.__getFirstTag(filecontent, tag).text
    
    def __getFirstTag(self, filecontent, tag):        
        xml = etree.fromstring(filecontent)
        
        for el in xml.findall(".//*"):
            thetag = etree.QName(el)                                    
            if thetag.localname == tag:
                return el