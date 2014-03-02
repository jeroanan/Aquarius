class HtmlRequestHandlerDownload(object):

    def __init__(self, app):
        self.__app = app

    def handle(self, book_id, format_code):
        book = self.__app.get_book_details(book_id)
        for thisFormat in book.formats:
            if thisFormat.Format == format_code:
                with open(thisFormat.Location, 'r') as f:
                    return f.read()