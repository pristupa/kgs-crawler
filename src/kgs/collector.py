from src.database import Database
from src.kgs.sgf.game import Color
from .sgf import Game


class KGSCollector:

    def store_game(self, game: Game):
        black_name = game.get_player_nickname(Color.BLACK)
        white_name = game.get_player_nickname(Color.WHITE)

        cursor = Database.connection.cursor()
        cursor.execute("INSERT INTO players (nickname) VALUES (%s) ON CONFLICT (nickname) DO NOTHING", (black_name,))
        cursor.execute("INSERT INTO players (nickname) VALUES (%s) ON CONFLICT (nickname) DO NOTHING", (white_name,))
        Database.connection.commit()
