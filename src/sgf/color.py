import enum


class Color(enum.Enum):
    BLACK = 'b'
    WHITE = 'w'


class UnknownColorException(Exception):
    pass
