class searchbook(object):
    
    def __init__(self, connection):
        self.__connection = connection
        
    def SearchBooks(self, searchTerm):
        searchTerm = "%s%s%s" % ("%", searchTerm, "%")        
        searchResult = self.__searchByTitle(searchTerm)        
        self.__appendSearchResultIfAny(searchResult, self.__searchByAuthor(searchTerm))                
        return searchResult
    
    def __searchByTitle(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Title LIKE '%s';" % searchTerm
        return self.__connection.ExecuteSqlFetchAll(sql)
    
    def __searchByAuthor(self, searchTerm):
        sql = "SELECT * FROM Book WHERE Author LIKE '%s';" % searchTerm                
        return self.__connection.ExecuteSqlFetchAll(sql)

    def __appendSearchResultIfAny(self, resultSet, searchResult):
        if len(searchResult)>0:
            resultSet.append(searchResult)
        return resultSet  
