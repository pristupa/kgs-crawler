import click

from ..kgs_service import KGSService


@click.command()
@click.option('--nickname', help='Nickname of the player to download games for')
@click.option('--month', help='Month to download games for in an "MM/YYYY" format')
def load_games_for_month(nickname: str, month: str):
    try:
        month, year = month.split('/', maxsplit=1)
        month = int(month)
        year = int(year)
        if not 1 <= month <= 12 or year < 2000:
            raise ValueError('Invalid month or year')
    except ValueError:
        click.echo('Wrong format for --month is given, use "MM/YYYY" starting from year 2000 (e.g. "05/2018")')
        return

    kgs = KGSService()
    kgs.load_games_for_month(nickname=nickname, year=year, month=month, manual=True)
