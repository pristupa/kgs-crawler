import threading

import click

from ..kgs_service import KGSService


@click.command()
def start():
    kgs = KGSService()
    kgs.try_load_games_for_month()

    e = threading.Event()
    while not e.wait(15):
        kgs.try_load_games_for_month()
