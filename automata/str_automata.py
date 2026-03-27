from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class StringAutomata(Automata):
    extra_closure_char: str = field(init= True, default="'") 
    _closures: int = field(init=False, default=0)

    def step(self, input_symbol: str):
        super().step(input_symbol)
        if self._current_state == self.State.STOPED:
            return self._current_state 

        if self._closures == 2:
            self._current_state = self.State.STOPED
            return self._current_state

        if self.first_step() and input_symbol == self.extra_closure_char:
            self._closures = 1
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)
            return self._current_state

        if self._closures == 1:
            if input_symbol == self.extra_closure_char:
                self._closures = 2
                self._current_state = self.State.PASSES
                self._input.append(input_symbol)
            else:
                self._input.append(input_symbol)
            return self._current_state
            
        if input_symbol in self.end_chars:
            self._current_state = self.State.STOPED
        else:
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)
        return self._current_state