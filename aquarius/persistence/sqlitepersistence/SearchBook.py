from aquarius.persistence.sqlitepersistence.BookFinder import BookFinder


class SearchBook(BookFinder):

    def __init__(self, connection):
        self.connection = connection

    def execute(self, search_term):
        search_result = self.__do_search(search_term)
        return self.convert_search_results_to_books(search_result)
    
    def __do_search(self, search_term):
        search_term = "%" + search_term + "%"
        search_result = self.__search_by_title(search_term)
        search_result = self.__append_search_result(search_result, self.__search_by_author(search_term))
        return search_result
    
    def __search_by_title(self, search_term):
        sql = """SELECT b.Id, b.Title, b.Author
               FROM Book as b
               WHERE Title LIKE ?;"""
        return self.connection.execute_sql_fetch_all_with_params(sql, (search_term,))
    
    def __append_search_result(self, result_set, search_result):
        new_list = []
        self.__populate_new_list_from_old(result_set, new_list)
        self.__populate_new_list_from_old(search_result, new_list)
        return new_list

    def __populate_new_list_from_old(self, old, new):
        for element in old:
            if element not in new:
                new.append(element)

    def __search_by_author(self, search_term):
        sql = """SELECT b.Id, b.Title, b.Author FROM Book as b WHERE Author LIKE ?;"""
        return self.connection.execute_sql_fetch_all_with_params(sql, (search_term,))


