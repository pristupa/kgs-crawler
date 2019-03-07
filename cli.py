import click

from src.cache import Cache
from src.commands import load_commands
from src.database import Database


@click.group()
def cli():
    pass


if __name__ == '__main__':
    load_commands(cli)
    Database.setup()
    Cache.warmup()
    try:
        cli()
    finally:
        Database.teardown()
