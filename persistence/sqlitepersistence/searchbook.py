from objects.book import book

class searchbook(object):
    
    def __init__(self, connection):
        self.__connection = connection
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__searchByTitle(searchTerm)
        searchResult = self.__appendSearchResult(searchResult, self.__searchByAuthor(searchTerm))                
        return self.__convertSearchResultsToBooks(searchResult)
    
    def __searchByTitle(self, searchTerm):
        sql = "SELECT Title, Author FROM Book WHERE Title LIKE '%s';" % searchTerm
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __searchByAuthor(self, searchTerm):
        sql = "SELECT Title, Author FROM Book WHERE Author LIKE '%s';" % searchTerm                
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
        
    def __convertSearchResultsToBooks(self, searchResult):
        books = []        
        for result in searchResult:            
            b = book()
            b.Title, b.Author = result            
            books.append(b)
        return books