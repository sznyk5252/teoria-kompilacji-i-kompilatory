from enum import Enum
from typing import Callable
from functools import cache
from tokens import TokenCode


class Context(Enum):
    BASIC = "BASIC"
    IN_TAG = "IN_TAG"

    def enter_tokens(self) -> list[TokenCode]:
        match self:
            case Context.BASIC:
                return []
            case Context.IN_TAG:
                return [TokenCode.LEFT_PARENTESE]
        raise NotImplementedError(f"Unimplemeted escape char for: {self}")

    def escape_tokens(self) -> list[TokenCode]:
        match self:
            case Context.BASIC:
                return []
            case Context.IN_TAG:
                return [TokenCode.RIGHT_PARENTESE]
        raise NotImplementedError(f"Unimplemeted escape char for: {self}")

    def token_separator(self) -> list[TokenCode]:
        match self:
            case Context.BASIC | Context.IN_TAG:
                return [TokenCode.COMMENT, TokenCode.SPACE, TokenCode.NEWLINE]
        raise NotImplementedError(f"Unimplemeted separator for: {self}")

    def possible_tokens(self) -> list[TokenCode]:
        match self:
            case Context.BASIC:
                return [
                    code
                    for code in TokenCode
                    if code
                    not in (
                        TokenCode.LEFT_PARENTESE,
                        TokenCode.RIGHT_PARENTESE,
                        TokenCode.SEPARATOR,
                    )
                ]
            case Context.IN_TAG:
                return [code for code in TokenCode]
        raise NotImplementedError(f"Unimplemeted possible tokens for: {self}")
