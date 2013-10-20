#!/usr/bin/python3

from book import book

class aquarius(object):    
        
    def __init__(self):
        self.__data = []
        b = book()
        b.Title = "book"
        b.Id = 1
        self.__data.append(b)
    
    def SearchBooks(self, searchString):
        if searchString == "":
            return []
        for book in self.__data:
            if searchString in book.Title:                
                yield book
                
    def ListBooksByFirstLetter(self, firstLetter):
        for book in self.__data:
            if book.Title.startswith(firstLetter):
                yield book
    
    def GetBookDetails(self, bookId):
        for book in self.__data:
            if book.Id == bookId:
                return book
    
    
