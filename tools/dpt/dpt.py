import click
from domain.App import App

@click.group()
def dpt():
    pass

@click.command("install-domain")
@click.option("--type", "-t", help="Type ")
def instal_domain(type):
    domain_app = App(type=type)
    domain_app.build()

dpt.add_command(instal_domain)

if __name__ == '__main__':
    dpt()