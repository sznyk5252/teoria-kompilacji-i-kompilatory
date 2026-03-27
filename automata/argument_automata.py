from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class ArgumentAutomata(Automata):
    end_char: str = field(init=True, default=',')

    def step(self, input_symbol: str):
        assert len(input_symbol) == 1
        if self._current_state == self.State.STOPED:
            return 
        
        if input_symbol == self.end_char:
            self._current_state = self.State.STOPED
        else:
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)
            