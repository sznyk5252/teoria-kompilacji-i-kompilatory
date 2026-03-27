from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class StringAutomata(Automata):
    end_char: str = field(init= True, default=" ") 
    extra_closure_char: str = field(init= True, default="'") 
    _closures: int = field(init=False, default=0)

    def step(self, input_symbol: str):
        assert len(input_symbol) == 1
        if self._current_state == self.State.STOPED:
            return 

        if self._closures == 2:
            self._current_state = self.State.STOPED
            return

        if self.first_step() and input_symbol == self.extra_closure_char:
            self._in_closure = 1
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)
            return

        if self._in_closure == 1:
            if input_symbol == self.extra_closure_char:
                self._in_closure = 2
                self._current_state = self.State.PASSES
                self._input.append(input_symbol)
            else:
                self._input.append(input_symbol)
            return
            
        if input_symbol == self.end_char:
            self._current_state = self.State.STOPED
        else:
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)