from jinja2 import Environment, PackageLoader


class SearchTemplateHandler(object):
    """Does rendering of the jinja2 template"""
    @staticmethod
    def render_search_template(search_results):
        """Renders a search-result page for the search and
        first letter functions"""
        env = Environment(loader=PackageLoader("aquarius", "output/web/html"))
        template = env.get_template("search.html")
        return template.render(results=search_results, \
                               totalbooks=len(search_results))