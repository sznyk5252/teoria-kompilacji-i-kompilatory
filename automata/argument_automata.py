from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class ArgumentAutomata(Automata):

    def step(self, input_symbol: str):
        super().step(input_symbol)
        if self._current_state == self.State.STOPED:
            return self._current_state 
        
        self._current_state = self.State.PASSES
        self._input.append(input_symbol)

        return self._current_state
            