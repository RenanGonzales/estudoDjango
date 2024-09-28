# cli.py

import click

@click.command()
def hello():
    """Exibe uma mensagem de saudação."""
    click.echo("Olá, mundo!")

if __name__ == '__main__':
    hello()
