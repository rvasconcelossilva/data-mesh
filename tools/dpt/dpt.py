import click
from domain.builders.ConsumerDomain import ConsumerDomain
from domain.builders.ServiceDomain import ServiceDomain

@click.group()
def dpt():
    pass

@click.command("install-domain")
@click.option("--type", "-t", help="Type ")
def instal_domain(type):
    domain_app = ConsumerDomain() if type == "consumer" else ServiceDomain()
    domain_app.build()

dpt.add_command(instal_domain)

if __name__ == '__main__':
    dpt()