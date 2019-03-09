from typing import Optional

from sgfmill.sgf import Sgf_game

from .color import Color
from .color import UnknownColorException


class Game:

    def __init__(self, sgf_content: bytes):
        self._sgf_game = Sgf_game.from_bytes(sgf_content)

    def get_date(self) -> str:
        return self._sgf_game.root.get('DT')

    def get_player_nickname(self, color: Color) -> str:
        nickname = self._sgf_game.get_player_name(color.value)
        if nickname is None:
            raise UnknownColorException()
        return nickname

    def get_player_rank(self, color: Color) -> Optional[str]:
        rank_identifier = 'WR' if color == Color.WHITE else 'BR'
        try:
            return self._sgf_game.root.get(rank_identifier)
        except KeyError:
            return None

    def get_white_won(self) -> Optional[bool]:
        winner = self._sgf_game.get_winner()
        if winner is None:
            return None
        return winner == Color.WHITE.value

    def get_board_size(self) -> int:
        return self._sgf_game.get_size()

    def get_komi(self) -> float:
        return self._sgf_game.get_komi()

    def get_handicap(self) -> int:
        handicap = self._sgf_game.get_handicap()
        if handicap is None:
            return 0
        return handicap

    def get_timelimit(self) -> Optional[float]:
        try:
            return self._sgf_game.root.get('TM')
        except KeyError:
            return None

    def get_overtime(self) -> Optional[str]:
        try:
            return self._sgf_game.root.get('OT')
        except KeyError:
            return None
