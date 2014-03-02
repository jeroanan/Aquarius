class HtmlRequestHandlerDownload(object):

    def __init__(self, app):
        self.__app = app

    def handle(self, book_id, format_code):
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.formats:
            if thisFormat.Format == format_code:
                return self.get_file_contents(thisFormat)

    def get_file_contents(self, format):
        with open(format.Location, 'r') as f:
            return f.read()