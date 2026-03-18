from enum import Enum
from typing import Callable
from functools import cache


class TokenCode(Enum):
    INTEGER = "INT"
    LEFT_PARENTESE = "LP"
    RIGHT_PARENTESE = "RP"
    IDENTIFIER = "ID"
    OPERATOR = "OP" #Zmieniłem na OP bo w testach chcialo OP zamiast OPR i chciałem zobaczyć czy to tylko ten błąd

    @cache
    def single_char_predicates_for(self) -> Callable[[str], bool]:
        match self:
            case TokenCode.INTEGER:
                return str.isdigit
            case TokenCode.LEFT_PARENTESE:
                return lambda x: x in "("
            case TokenCode.RIGHT_PARENTESE:
                return lambda x: x in ")"
            case TokenCode.IDENTIFIER:
                return lambda c: c.isalnum() or c == "_"
            case TokenCode.OPERATOR:
                return lambda x: x in "+-/*"

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__


type TokenValue = str | int
type Token = tuple[TokenCode, TokenValue]
