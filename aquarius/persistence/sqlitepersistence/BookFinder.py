from aquarius.objects.Book import Book


class BookFinder(object):

    def convert_search_results_to_books(self, search_result):
        books = []
        for result in search_result:
            self.__convert_search_result_to_book(books, result)
        return books

    def __convert_search_result_to_book(self, books, result):
        b = Book()
        b.id, b.title, b.author = result
        self.__add_formats_to_book(b)
        books.append(b)