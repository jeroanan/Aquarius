from aquarius.output.web.requesthandlers.searchtemplatehelper import searchtemplatehelper


class htmlrequesthandlerfirstletter(object):
       
    def __init__(self, app):
        self.__app = app

    def Handle(self, firstletter):
        searchResults = list(self.__app.ListBooksByFirstLetter(firstletter))
        return searchtemplatehelper.RenderSearchTemplate(searchResults)
