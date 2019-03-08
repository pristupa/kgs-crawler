from .games_storage import GamesStorage
from .players_storage import PlayersStorage
from .sgf import Color
from .sgf import Game


class KGSCollector:

    def store_game(self, game: Game, raw_sgf_content: bytes):
        black_nickname = game.get_player_nickname(Color.BLACK)
        white_nickname = game.get_player_nickname(Color.WHITE)
        PlayersStorage.add_player(black_nickname)
        PlayersStorage.add_player(white_nickname)
        GamesStorage.add_game(game, raw_sgf_content=raw_sgf_content)
