from .players_storage import PlayersStorage
from .sgf import Color
from .sgf import Game


class KGSCollector:

    def store_game(self, game: Game):
        black_nickname = game.get_player_nickname(Color.BLACK)
        white_nickname = game.get_player_nickname(Color.WHITE)
        PlayersStorage.add_player(black_nickname)
        PlayersStorage.add_player(white_nickname)
