from click import Group

from .load_games_for_month import load_games_for_month
from .start import start


def load_commands(cli: Group):
    cli.add_command(load_games_for_month)
    cli.add_command(start)
