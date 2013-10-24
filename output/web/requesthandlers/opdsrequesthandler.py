import xml.etree.ElementTree as etree

import uuid

class opdsrequesthandler(object):
    
    def IndexHandler(self):
        doc = self.__constructCommonHeader()
        self.__addIndexEntry("List By Letter", "Browse books by title", "/bytitle", doc)
        return doc 
    
    def __constructCommonHeader(self):
        feedElement = etree.Element('feed', attrib={
                                                    "xmlns" : "http://www.w3.org/2005/Atom",  
                                                    "xmlns:opds" : "http://opds-spec.org/2010/catalog"})        
        return feedElement
    
    def __addIndexEntry(self, title, description, href, doc):        
        entry = etree.SubElement(doc, "entry")
        etree.SubElement(entry, "title").text = title
        etree.SubElement(entry, "link", attrib={"rel" : "subsection", 
                                                "href" : href, 
                                                "type" : "application/atom+xml;profile=opds-catalog;kind=acquisition"})
        
        etree.SubElement(entry, "id").text=str(uuid.uuid4())
        etree.SubElement(entry, "content", attrib= {"content" : "text"}).text=description