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
        self.__bookMetaData = self.__readFileFromZip(self.__getRootFilePath())        
    
    def __getRootFilePath(self):
        container = etree.fromstring(self.__getContainerFileContent())
        xp = "//*[local-name()='container']/*[local-name()='rootfiles']/*[local-name()='rootfile']"
        return container.xpath(xp)[0].get("full-path")                
    
    def __getContainerFileContent(self):
        return self.__readFileFromZip("META-INF/container.xml")
        
    def __readFileFromZip(self, fileName):
        with self.__zipFile.open(fileName) as f:
            return f.read()
    
    def __setBookDetails(self):
        x = etree.fromstring(self.__bookMetaData)
        self.__getEpubTitle(x)        
        self.__getEpubAuthor(x)
        
    def __getEpubTitle(self, x):
        self.__title = self.__getItemFromEpubMetaData(x, "title")

    def __getEpubAuthor(self, x):
        self.__author = self.__getItemFromEpubMetaData(x, "creator")
        
    def __getItemFromEpubMetaData(self, x, attributeName):
        titleXp = "//*[local-name()='package']/*[local-name()='metadata']/*[local-name()='%s']" % attributeName
        return x.xpath(titleXp)[0].text
    