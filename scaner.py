from tokens import TokenCode, TokenValue, Token
from dataclasses import dataclass, field
from typing import Callable, ClassVar, Self


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

    def tokenize(self):
        self._char_iterator = 0
        self._tokens = []
        # TODO:
        # pętla po wszystkich typach i dla każdego zrobić _fit_from_front()
        # sprawdzaj błędy, jak się pojawią to w komentarzu powinien być self._char_iterator
        # sprawdzaj czy następny znak jest spodziewanym

        self._check_bracketing()

    def _fit_from_front(self, token_type: TokenCode):
        predicate = token_type.single_char_predicates_for()
        single_char = self.source[self._char_iterator]
        val: TokenValue = ""
        while self._char_iterator < len(self.source) and predicate(single_char):
            val += single_char
            self._char_iterator += 1
            single_char = self.source[self._char_iterator]

        if val != "":
            self._tokens.append((token_type, val))

    def _expected_after_last(self) -> list[TokenCode]:
        # TODO:
        # w szczególności na start jest cokolwiek
        # resztę obczaisz
        # () - są zawsze ok
        pass

    def _check_bracketing(self):
        left_count = 0
        right_count = 0
        for token_id, _ in self._tokens:
            if token_id == TokenCode.LEFT_PARENTESE:
                left_count += 1
            elif token_id == TokenCode.RIGHT_PARENTESE:
                right_count += 1
        if left_count != right_count:
            raise ParenthesizingError(
                f"Unbalanced bracketing, Left: {left_count}, Right: {right_count}"
            )

    def __str__(self) -> str:
        buff = ""
        for el in self._tokens:
            buff += str(el) + "\n"
        return buff
