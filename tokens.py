from enum import Enum
from typing import Callable
from functools import cache
from automata import Automata, StringAutomata, NumberAutomata, CommentAutomata, SingleCharAutomata, TagAutomata
import re

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
    NEWLINE = "ENDL"
    COMMENT = "COM"

    @cache
    def automata_for(self) -> Automata:
        match self:
            case TokenCode.TAG:
                return TagAutomata(possible_tags= ["RANGE", "MATCH", "ANYOF", "THROWS", "VAR", "FINALCHECK", "DEF", "REP"] )
            case TokenCode.LEFT_PARENTESE:
                return SingleCharAutomata(char='(')
            case TokenCode.RIGHT_PARENTESE:
                return SingleCharAutomata(char=')')
            case TokenCode.SEPARATOR:
                return SingleCharAutomata(char=',')
            case TokenCode.NUMBER:
                return NumberAutomata()
            case TokenCode.STRING:
                return StringAutomata(end_char=' ')
            case TokenCode.SPACE:
                return SingleCharAutomata(char=' ')
            case TokenCode.NEWLINE:
                return SingleCharAutomata(char='\n')
            case TokenCode.COMMENT:
                return CommentAutomata(begin_char='#', end_char='\n0')
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
