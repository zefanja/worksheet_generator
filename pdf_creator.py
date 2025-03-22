from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def html_to_pdf(html_content, output_file):
    HTML(string=html_content).write_pdf(output_file)

def render_template(template_name, context):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    return template.render(context)
