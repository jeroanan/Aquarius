from jinja2 import Environment, PackageLoader


class HtmlRequestHandlerIndex(object):

    def __init__(self, app):
        self.__app = app

    def handle(self):
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("index.html")
        return template.render(app=self.__app)