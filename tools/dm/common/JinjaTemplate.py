import string
from jinja2 import Environment, FileSystemLoader

class JinjaTemplate:

    def __init__(self, template_path, template_file) -> None:
        self.environment = Environment(loader=FileSystemLoader(template_path))
        self.template = self.environment.get_template(template_file)


    def render(self, value) -> string:
        return self.template.render(value)


if __name__ == '__main__':
    jinja = JinjaTemplate('./tools/dm/common/templates/domain', 'create_database.sql')
    database = {'database': 'source'}

    print(jinja.render(database))

