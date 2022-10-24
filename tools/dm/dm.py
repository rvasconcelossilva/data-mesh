import click

@click.group()
def dm():
    pass

@click.command()
def build_domain():
    print('build_domain')
    pass

dm.add_command(build_domain)

if __name__ == '__main__':
    dm()