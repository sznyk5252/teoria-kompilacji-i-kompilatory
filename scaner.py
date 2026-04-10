from dataclasses import dataclass, field
from typing import Callable, ClassVar, Self
from automata.automata import Automata
from tokens import TokenCode, TokenValue, Token
from contexts import Context


class ScaningError(Exception):
    """
    This is thrown when an error occur while scanning the input string
    """


class ParenthesizingError(ScaningError):
    """
    This is thrown when Parenthesization is wrong
    """


class UndefinedCharacterError(ScaningError):
    """
    This is thrown when undefined character occur
    """

@dataclass
class Scaner:
    source: str
    _tokens: list[Token] = field(init=False, default_factory=lambda: [])
    _char_iterator: int = field(init=False, default=0)
    _current_context: Context = field(init=False, default_factory=lambda: Context.BASIC)

    def tokenize(self):
        self._char_iterator = 0
        self._tokens = []
        prioritised_tokens = [
            TokenCode.TAG,
            TokenCode.COMMENT,
            TokenCode.LEFT_PARENTESE,
            TokenCode.RIGHT_PARENTESE,
            TokenCode.SEPARATOR,
            TokenCode.NUMBER,
        ]

        while self._char_iterator < len(self.source):
            best_match: tuple[TokenCode, str] | None = None
            longest_match_len = 0

            for token_code in TokenCode:
                automata = token_code.automata_for()
                automata.reset()
                temp_iterator = self._char_iterator
                last_accepted_len = 0

                while temp_iterator < len(self.source):
                    char = self.source[temp_iterator]
                    # if token_code == TokenCode.SPACE:
                    #     print(f"token: {token_code}, char: {char}, automata: {automata}")
                    if automata.step(char) == Automata.State.STOPED or (
                        char == "\n" and token_code != TokenCode.NEWLINE
                    ):
                        break
                    temp_iterator += 1
                    if automata.is_accepted():
                        last_accepted_len = temp_iterator - self._char_iterator
                if last_accepted_len > 0 and token_code in prioritised_tokens:
                    best_match = (
                        token_code,
                        self.source[
                            self._char_iterator : self._char_iterator
                            + last_accepted_len
                        ],
                    )
                    longest_match_len = last_accepted_len
                    break
                if last_accepted_len > longest_match_len:
                    longest_match_len = last_accepted_len
                    best_match = (
                        token_code,
                        self.source[
                            self._char_iterator : self._char_iterator
                            + last_accepted_len
                        ],
                    )

            if not best_match or longest_match_len == 0:
                raise UndefinedCharacterError(
                    f"No valid token found at position {self._char_iterator}: '{self.source[self._char_iterator : self._char_iterator + 10]}...' last char: '{char}'"
                )

            token_code, token_value = best_match

            self._tokens.append((token_code, token_value))
            self._char_iterator += longest_match_len

    # def _fit_from_front(self, token_type: TokenCode) -> int:
    #     automata = token_type.automata_for()
    #     iterator = self._char_iterator
    #     single_char = self.source[iterator]

    #     while iterator < len(self.source) and (automata.still_running() or automata.is_accepted()):
    #         automata.step(single_char)
    #         iterator += 1
    #         if iterator < len(self.source):
    #             single_char = self.source[iterator]

    #     return iterator

    # def _expected_after_last(self) -> list[TokenCode]:
    #     if not self._tokens:
    #         return [TokenCode.LEFT_PARENTESE, TokenCode.INTEGER, TokenCode.IDENTIFIER]

    #     last_token = self._tokens[-1][0]
    #     if last_token == TokenCode.LEFT_PARENTESE:
    #         return [TokenCode.LEFT_PARENTESE, TokenCode.INTEGER, TokenCode.RIGHT_PARENTESE, TokenCode.IDENTIFIER]
    #     elif last_token == TokenCode.RIGHT_PARENTESE:
    #         return [TokenCode.RIGHT_PARENTESE, TokenCode.OPERATOR]
    #     elif last_token == TokenCode.INTEGER:
    #         return [TokenCode.OPERATOR, TokenCode.RIGHT_PARENTESE]
    #     elif last_token == TokenCode.IDENTIFIER:
    #         return [TokenCode.OPERATOR, TokenCode.RIGHT_PARENTESE]
    #     else:
    #         return [TokenCode.INTEGER, TokenCode.LEFT_PARENTESE, TokenCode.IDENTIFIER]

    # def _check_bracketing(self):
    #     left_count = 0
    #     right_count = 0
    #     for token_id, _ in self._tokens:
    #         if token_id == TokenCode.LEFT_PARENTESE:
    #             left_count += 1
    #         elif token_id == TokenCode.RIGHT_PARENTESE:
    #             right_count += 1
    #     if left_count != right_count:
    #         raise ParenthesizingError(
    #             f"Unbalanced bracketing, Left: {left_count}, Right: {right_count}"
    #         )

    def __str__(self) -> str:
        buff = ""
        for el in self._tokens:
            buff += str(el) + "\n"
        return buff
