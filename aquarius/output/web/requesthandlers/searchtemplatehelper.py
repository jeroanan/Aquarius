from jinja2 import Environment, PackageLoader

class searchtemplatehelper(object):

    @staticmethod    
    def RenderSearchTemplate(searchResults):
        env = Environment(loader = PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("search.html")
        return template.render(results = searchResults, totalbooks = len(searchResults))