from enum import Enum
from typing import Callable
from functools import cache
import re


class TokenCode(Enum):
    TAG = "TAG"
    LEFT_PARENTESE = "LP"
    RIGHT_PARENTESE = "RP"
    IDENTIFIER = "ID"
    SEPARATOR = "SEP"
    ARGUMENT = "ARG"
    NUMBER = "NUMB"
    STRING = "STR"
    SPACE = "SPACE"
    NEWLINE = "ENDL"

    @cache
    def predicates_for(self) -> Callable[[str], bool]:
        match self:
            case TokenCode.TAG:
                return lambda x: (
                    x in ("RANGE", "MATCH", "ANYOF", "THROWS", "VAR", "FINALCHECK")
                )
            case TokenCode.LEFT_PARENTESE:
                return lambda x: x == "("
            case TokenCode.RIGHT_PARENTESE:
                return lambda x: x == ")"
            case TokenCode.SEPARATOR:
                return lambda x: x == ","
            case TokenCode.ARGUMENT:
                return TokenCode.STRING.predicates_for()
            case TokenCode.NUMBER:
                return lambda x: bool(
                    re.fullmatch(r"-?[0-9]+\.?[0-9]*", x)
                )  # TODO: zastąpić żeby nie było re - bo chyba mnie może być
            case TokenCode.STRING:
                return lambda x: True
            case TokenCode.SPACE:
                return lambda x: x == " "
            case TokenCode.NEWLINE:
                return lambda x: x == "\n"
            case _:
                raise NotImplementedError(f"Unimplemented predicate for token: {self}")

    @cache
    def get_color(self):
        # TODO
        pass

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__


type TokenValue = str | int
type Token = tuple[TokenCode, TokenValue]
