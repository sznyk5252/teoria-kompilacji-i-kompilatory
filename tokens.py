from enum import Enum
from functools import cache
# from unittest import case

from automata import (
    Automata,
    StringAutomata,
    NumberAutomata,
    CommentAutomata,
    SingleCharAutomata,
    TagAutomata,
)


# MACRA + PETLEs
class TokenCode(Enum):
    TAG = "TAG"
    LEFT_PARENTESE = "LP"
    RIGHT_PARENTESE = "RP"
    SEPARATOR = "SEP"
    # ARGUMENT = "ARG" - to powinien być po prostu str/numb
    NUMBER = "NUMB"
    STRING = "STR"
    SPACE = "SPACE"
    NEWLINE = "NEWLINE"
    COMMENT = "COM"

    @cache
    def automata_for(self) -> Automata:
        brake_chars = ["\n", " ", "(", ")", ","]
        match self:
            case TokenCode.TAG:
                return TagAutomata(
                    possible_tags=[
                        "RANGE",
                        "MATCH",
                        "ANYOF",
                        "THROWS",
                        "VAR",
                        "FINALCHECK",
                        "DEF",
                        "REP",
                    ],
                    end_chars=brake_chars,
                )
            case TokenCode.LEFT_PARENTESE:
                return SingleCharAutomata(char="(")
            case TokenCode.RIGHT_PARENTESE:
                return SingleCharAutomata(char=")")
            case TokenCode.SEPARATOR:
                return SingleCharAutomata(char=",")
            case TokenCode.NUMBER:
                return NumberAutomata(end_chars=brake_chars)
            case TokenCode.STRING:
                return StringAutomata(end_chars=brake_chars)
            case TokenCode.SPACE:
                return SingleCharAutomata(char=" ")
            case TokenCode.NEWLINE:
                return SingleCharAutomata(char="\n")
            case TokenCode.COMMENT:
                return CommentAutomata(begin_char="#", end_chars=["\n"])
            case _:
                raise NotImplementedError(f"Unimplemented predicate for token: {self}")

    @cache
    def get_color(self):
        match self:
            case TokenCode.TAG:
                return "purple"
            case TokenCode.LEFT_PARENTESE | TokenCode.RIGHT_PARENTESE:
                return "red"
            case TokenCode.SEPARATOR:
                return "white"
            case TokenCode.NUMBER:
                return "orange"
            case TokenCode.STRING:
                return "green"
            case TokenCode.SPACE | TokenCode.NEWLINE:
                return ""
            case TokenCode.COMMENT:
                return "grey"
        print(f"Warning: undefined color for token: {self}")
        return "grey"



    def __str__(self) -> str:
        return self.value

    __repr__ = __str__


type TokenValue = str | int
type Token = tuple[TokenCode, TokenValue]
