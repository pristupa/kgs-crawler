from sgfmill.sgf import Sgf_game

from .color import Color
from .color import UnknownColorException


class Game:

    def __init__(self, sgf_content: bytes):
        self._sgf_game = Sgf_game.from_bytes(sgf_content)

    def get_player_nickname(self, color: Color) -> str:
        nickname = self._sgf_game.get_player_name(color.value)
        if nickname is None:
            raise UnknownColorException()
        return nickname
