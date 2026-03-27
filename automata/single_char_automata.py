from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class SingleCharAutomata(Automata):
    char: str = field(init=True, default=' ')

    def step(self, input_symbol: str):
        assert len(input_symbol) == 1
        if self._current_state == self.State.UNDEFINED:
            if input_symbol == self.char:
                self._input.append(input_symbol)
                self._current_state = self.State.PASSES
            else:
                self._current_state = self.State.STOPED
        else:
            self._current_state = self.State.STOPED
        return self._current_state