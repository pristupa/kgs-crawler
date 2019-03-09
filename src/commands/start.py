import threading

import click

from ..kgs_service import KGSService


@click.command()
def start():
    kgs = KGSService()

    e = threading.Event()
    while not e.wait(15):
        kgs.try_load_games_for_month()
