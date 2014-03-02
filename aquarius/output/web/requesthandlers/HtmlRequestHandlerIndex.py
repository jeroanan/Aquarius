class HtmlRequestHandlerIndex(object):

    def __init__(self, app):
        pass

    def handle(self):
        return self.__get_file_contents("aquarius/output/web/html/index.html")

    @staticmethod
    def __get_file_contents(file_name):
        with open(file_name, "r") as f:
            return f.read()