import hashlib
from typing import Optional

import psycopg2

from .database import Database
from .sgf import Color
from .sgf import Game
from .cache import Cache


class GamesStorage:

    @classmethod
    def add_game(cls, game: Game, raw_sgf_content: bytes, year: Optional[int] = None, month: Optional[int] = None):
        sgf_content_hash = hashlib.sha1(raw_sgf_content)
        if Cache.has_game(sgf_content_hash):
            return

        data = {
            'played_at': game.get_date(),
            'yaer': year,
            'month': month,
            'white_nickname': game.get_player_nickname(Color.WHITE),
            'black_nickname': game.get_player_nickname(Color.BLACK),
            'white_rank': game.get_player_rank(Color.WHITE),
            'black_rank': game.get_player_rank(Color.BLACK),
            'white_won': game.get_white_won(),
            'board_size': game.get_board_size(),
            'komi': game.get_komi(),
            'handicap': game.get_handicap(),
            'timelimit': game.get_timelimit(),
            'overtime': game.get_overtime(),
            'sgf_content': psycopg2.Binary(raw_sgf_content),
            'sgf_content_hash': sgf_content_hash.hexdigest(),
        }
        fields = list(data.keys())
        values = list(data.values())
        fields_string = ','.join(fields)
        values_string = ','.join(['%s'] * len(fields))
        Database.execute(
            f"INSERT INTO games ({fields_string}) VALUES ({values_string}) ON CONFLICT (sgf_content_hash) DO NOTHING",
            values,
        )
        Cache.add_game(sgf_content_hash)
