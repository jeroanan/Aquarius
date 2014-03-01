from jinja2 import Environment, PackageLoader


class SearchTemplateHandler(object):

    def render_search_template(self, search_results):
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("search.html")
        return template.render(results=search_results, \
                               totalbooks=len(search_results))