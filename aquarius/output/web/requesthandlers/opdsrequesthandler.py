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
    
    def FirstLetterHandler(self, firstletter):
        doc = self.__constructCommonHeader("Titles beginning with %s" % firstletter)
        books = self.__app.ListBooksByFirstLetter(firstletter)
        
        for book in books:
            self.__addBookIndexEntry(book, "", doc)
        return doc
    
    def BookHandler(self, bookId):
        doc = self.__constructCommonHeader("Aquarius EBook Library")        
        book = self.__app.GetBookDetails(bookId)
        self.__addAcquisitonDetails(book, doc)       
        
        for thisFormat in book.Formats:
            pass
            self.__addAcqusitionLink(book, thisFormat.Format, doc)
        return doc
    
    def DownloadHandler(self, bookId, bookFormat):
        book = self.__app.GetBookDetails(bookId)
        for thisFormat in book.Formats:
            if thisFormat.Format == bookFormat:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()
    
    def Search(self, searchTerm):
        doc = self.__constructCommonHeader("Search results for %s" % searchTerm)       
        books = self.__app.SearchBooks(searchTerm)
        for book in books:
            self.__addBookIndexEntry(book, "",  doc)        
        return doc
    
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
    
    def __addBookIndexEntry(self, book, description, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = book.Title
        etree.SubElement(entry, "link", attrib={"rel" : "subsection", 
                                                "href" :  "/book/%d" % book.Id, 
                                                "type" : "application/atom+xml;profile=opds-catalog;kind=acquisition"})
                
        etree.SubElement(entry, "id").text=str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib= {"content" : "text"}).text=book.Author        
        
    def __addIndexEntry(self, title, description, href, doc):        
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = title
        etree.SubElement(entry, "link", attrib={"rel" : "subsection", 
                                                "href" : href, 
                                                "type" : "application/atom+xml;profile=opds-catalog;kind=acquisition"})        
        etree.SubElement(entry, "id").text=str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib= {"content" : "text"}).text=description
    
    def __addAcquisitonDetails(self, book, doc):
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text=book.Title
        
    def __addAcqusitionLink(self, book, fileExt, doc):
        entry = doc.find("entry")
        booktype = self.__app.GetBookType(fileExt)

        e = etree.SubElement(entry, "link", attrib={
                "rel" : "http://opds-spec.org/acquisition", 
                "href" : "/download/%s/%s" % (book.Id, fileExt),
                "type" : booktype.MimeType })
        author = etree.SubElement(e, "author")
        etree.SubElement(author, "name").text=book.Author
        etree.SubElement(author, "uri").text=book.AuthorUri

    
    
    
    

    
    
    
    
            