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
        while self._char_iterator < len(self.source):
            curr_char = self.source[self._char_iterator]
            if curr_char.isspace():
                self._char_iterator += 1
            else:
                curr_position = self._char_iterator
                for type in self._expected_after_last():
                    self._fit_from_front(type)
                    if self._char_iterator > curr_position:
                        break

                if curr_position == self._char_iterator:
                    is_correct_char = any(t.single_char_predicates_for()(curr_char) for t in TokenCode)

                    if is_correct_char:
                        raise ScaningError(f"Unexpected character {curr_char} on index {self._char_iterator},"+
                                           f" does not fit in any expected token: {self._expected_after_last()}")
                    else:
                        raise UndefinedCharacterError(f"Unknown character {curr_char} on index {self._char_iterator}")

        self._check_bracketing()

    def _fit_from_front(self, token_type: TokenCode):
        predicate = token_type.single_char_predicates_for()
        single_char = self.source[self._char_iterator]
        val: TokenValue = ""
        while self._char_iterator < len(self.source) and predicate(single_char):
            val += single_char
            self._char_iterator += 1

            if token_type in [TokenCode.OPERATOR, TokenCode.RIGHT_PARENTESE, TokenCode.LEFT_PARENTESE]:
                break

            if self._char_iterator < len(self.source):
                single_char = self.source[self._char_iterator]

        if val != "":
            self._tokens.append((token_type, val))

    def _expected_after_last(self) -> list[TokenCode]:
        if not self._tokens:
            return [TokenCode.LEFT_PARENTESE, TokenCode.INTEGER, TokenCode.IDENTIFIER]

        last_token = self._tokens[-1][0]
        if last_token == TokenCode.LEFT_PARENTESE:
            return [TokenCode.LEFT_PARENTESE, TokenCode.INTEGER, TokenCode.RIGHT_PARENTESE, TokenCode.IDENTIFIER]
        elif last_token == TokenCode.RIGHT_PARENTESE:
            return [TokenCode.RIGHT_PARENTESE, TokenCode.OPERATOR]
        elif last_token == TokenCode.INTEGER:
            return [TokenCode.OPERATOR, TokenCode.RIGHT_PARENTESE]
        elif last_token == TokenCode.IDENTIFIER:
            return [TokenCode.OPERATOR, TokenCode.RIGHT_PARENTESE]
        else:
            return [TokenCode.INTEGER, TokenCode.LEFT_PARENTESE, TokenCode.IDENTIFIER]



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
