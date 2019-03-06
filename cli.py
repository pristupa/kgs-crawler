import click
from src.commands import load_commands
from src.database import Database


@click.group()
def cli():
    pass


if __name__ == '__main__':
    load_commands(cli)
    Database.setup()
    try:
        cli()
    finally:
        Database.teardown()
