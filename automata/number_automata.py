from .automata import Automata
from dataclasses import dataclass, field


@dataclass
class NumberAutomata(Automata):
    _minus: bool = field(init=False, default=False)
    _dot: bool = field(init=False, default=False)

    def step(self, input_symbol: str):
        super().step(input_symbol)
        if self._current_state == self.State.STOPED:
            return self._current_state

        if self._current_state == self.State.UNDEFINED:
            match input_symbol:
                case ".":
                    if self._dot:
                        self._current_state = self.State.STOPED
                        return self._current_state
                    self._dot = True
                    self._input.append(input_symbol)
                case "-":
                    if not self.first_step():
                        self._current_state = self.State.STOPED
                        return self._current_state
                    self._minus = True
                    self._input.append(input_symbol)
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    self._input.append(input_symbol)
                    self._current_state = self.State.PASSES
                case _:
                    self._current_state = self.State.STOPED
        elif self._current_state == self.State.PASSES:
            match input_symbol:
                case ".":
                    if self._dot:
                        self._current_state = self.State.STOPED
                    else:
                        self._dot = True
                        self._input.append(input_symbol)
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    self._input.append(input_symbol)
                case _:
                    self._current_state = self.State.STOPED
        return self._current_state

    def first_step(self) -> bool:
        return len(self._input) == 0

    def reset(self):
        super().reset()
        self._minus = False
        self._dot = False
