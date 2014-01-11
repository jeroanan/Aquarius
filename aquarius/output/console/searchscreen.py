from aquarius.output.console.ConsoleScreen import ConsoleScreen


class searchscreen(ConsoleScreen):

    def __init__(self, app):
        super().__init__(app)

    def Main(self):
        s = self.input()
        results = self.get_app().SearchBooks(s)
        self.__search_results_screen(results)

    def __search_results_screen(self, results):
        print(self.get_strings().GetSearchResultTitleString())
        i = 0
        for result in results:
            i += 1
            print(result.title)
        print(self.get_strings().GetSearchResultFooterString(i))
