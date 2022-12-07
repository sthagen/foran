"""In front or behind (Foran eller bagved)? rendering interface for templates."""
from enum import Enum, auto


class Template(Enum):
    NONE = auto()
    STRING = auto()
    F_STRING = auto()
    JINJA_STRING = auto()
    JINJA_PATH = auto()
