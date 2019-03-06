from src.database import Database
from src.kgs.sgf.game import Color
from .sgf import Game


class KGSCollector:

    def store_game(self, game: Game):
        black_nickname = game.get_player_nickname(Color.BLACK)
        white_nickname = game.get_player_nickname(Color.WHITE)

        cursor = Database.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO players (nickname) VALUES (?)", (black_nickname,))
        cursor.execute("INSERT OR IGNORE INTO players (nickname) VALUES (?)", (white_nickname,))
        Database.connection.commit()
