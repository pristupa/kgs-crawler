import psycopg2

from .database import Database
from .sgf import Game
from .sgf import Color


class GamesStorage:

    @classmethod
    def add_game(cls, game: Game, raw_sgf_content: bytes):
        cursor = Database.connection.cursor()
        data = {
            'played_at': game.get_date(),
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
        }
        fields = list(data.keys())
        values = list(data.values())
        fields_string = ','.join(fields)
        values_string = ','.join(['%s'] * len(fields))
        cursor.execute(f"INSERT INTO games ({fields_string}) VALUES ({values_string})", values)
        cursor.close()
        Database.connection.commit()
