from objects.book import book
from objects.bookformat import bookformat

class searchbook(object):            
    
    def SearchBooks(self, searchTerm, connection):
        self.__connection = connection
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__doSearch(searchTerm)                
        return self.__convertSearchResultsToBooks(searchResult)
    
    def __doSearch(self, searchTerm):
        searchResult = self.__searchByTitle(searchTerm)
        searchResult = self.__appendSearchResult(searchResult, self.__searchByAuthor(searchTerm))
        return searchResult
    
    def __searchByTitle(self, searchTerm):
        sql = """SELECT b.Id, b.Title, b.Author
               FROM Book as b 
               WHERE Title LIKE '%s';""" % searchTerm
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __searchByAuthor(self, searchTerm):
        sql = """SELECT b.Id, b.Title, b.Author 
                 FROM Book as b 
                 WHERE Author LIKE '%s';""" % searchTerm                
        return self.__connection.ExecuteSqlFetchAll(sql)

    def __appendSearchResult(self, resultSet, searchResult):        
        newList = []
        self.__populateNewListFromOld(resultSet, newList)
        self.__populateNewListFromOld(searchResult, newList)
        return newList

    def __populateNewListFromOld(self, old, new):
        for element in old:
            if element not in new:
                new.append(element)
                
    def GetBookDetails(self, bookId, connection):
        self.__connection = connection
        sql = "SELECT Id, Title, Author FROM Book WHERE Id=%s" % bookId
        b = book()
        books = self.__convertSearchResultsToBooks(connection.ExecuteSqlFetchAll(sql))
        if len(books)>0:
            b = books[0]
        return b
    
    def __convertSearchResultsToBooks(self, searchResult):
        books = []        
        for result in searchResult:            
            self.__convertSearchResultToBook(books, result)
        return books
    
    def __convertSearchResultToBook(self, books, result):
        b = book()
        b.Id, b.Title, b.Author = result        
        self.__addFormatsToBook(b)
        books.append(b)
    
    def __addFormatsToBook(self, book):
        formats = self.__getFormatsForBook(book)
        for f in formats:
            x = f
            bf = bookformat()
            bf.Format = x[0]
            book.Formats.append(bf)
                
    def __getFormatsForBook(self, book):
        sql = "SELECT Format FROM BookFormat WHERE Book=%s" % book.Id
        formats = self.__connection.ExecuteSqlFetchAll(sql)        
        return formats
    
    