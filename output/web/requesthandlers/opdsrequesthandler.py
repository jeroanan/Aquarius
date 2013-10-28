import xml.etree.ElementTree as etree

import uuid

class opdsrequesthandler(object):
       
    def __init__(self, app):
        self.__app = app
        
    def IndexHandler(self):
        doc = self.__constructCommonHeader("Aquarius EBook library")        
        self.__addIndexEntry("List By Letter", "Browse books by title", "/bytitle", doc)
        return doc 
    
    def ByTitleHandler(self):
        doc = self.__constructCommonHeader("Browse books by title")
        
        for i in range(0,10):
            self.__addIndexEntry(str(i), "Titles beginning with %s" % str(i), "/firstletter/%s" % str(i), doc)
        
        for i in range(65, 91):
            self.__addIndexEntry(chr(i), "Titles beginning with %s" % chr(i), "/firstletter/%s" % chr(i), doc)
        
        return doc
    
    def FirstLetterHandler(self, letter):
        doc = self.__constructCommonHeader("Titles beginning with %s" % letter)
        books = self.__app.ListBooksByFirstLetter(letter)
        
        for book in books:
            self.__addIndexEntry(book.Title, "", "/book/%d" % book.Id, doc)
        return doc
    
    def BookHandler(self, bookId):
        doc = self.__constructCommonHeader("Aquarius EBook Library")        
        book = self.__app.GetBookDetails(bookId)
        self._addAcquisitonDetails(book.Title, doc)       
        
        for thisFormat in book.Formats:
            self._addAcqusitionLink(bookId, thisFormat.Format, doc)
        return doc
    
    def DownloadHandler(self, bookId, bookFormat):
        book = self.__app.GetBookDetails(bookId)
        for thisFormat in book.Formats:
            if thisFormat.Format == bookFormat:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()
    
    def __constructCommonHeader(self, title):
        feedElement = etree.Element('feed', attrib={
                                                    "xmlns" : "http://www.w3.org/2005/Atom",  
                                                    "xmlns:opds" : "http://opds-spec.org/2010/catalog"})
        etree.SubElement(feedElement, "id").text=str(uuid.uuid4())        
        etree.SubElement(feedElement, "title").text=title
        etree.SubElement(feedElement, "link").attrib={"href" : "/search/{searchTerms}",
                                                      "type" : "application/atom+xml",
                                                      "rel" : "search",
                                                      "title" : "Search"}        
        return feedElement
    
    def __addIndexEntry(self, title, description, href, doc):        
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = title
        etree.SubElement(entry, "link", attrib={"rel" : "subsection", 
                                                "href" : href, 
                                                "type" : "application/atom+xml;profile=opds-catalog;kind=acquisition"})        
        etree.SubElement(entry, "id").text=str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib= {"content" : "text"}).text=description
    
    def _addAcquisitonDetails(self, title, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text=title
    
    def _addAcqusitionLink(self, bookId, fileExt, doc):
        entry = doc.find("entry")
        booktype = self.__app.GetBookType(fileExt)

        etree.SubElement(entry, "link", attrib={
                "rel" : "http://opds-spec.org/acquisition", 
                "href" : "/download/%s/%s" % (bookId, fileExt),
                "type" : booktype.MimeType })

    
    
    
    
            