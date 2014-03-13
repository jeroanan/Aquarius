from jinja2 import Environment, PackageLoader


class Jinja2Loader(object):

    def load_template(self, application_name, template_directory, template_filename, **args):
        env = Environment(loader=PackageLoader(application_name, template_directory))
        template = env.get_template(template_filename)
        return template.render(args)