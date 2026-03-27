from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class CommentAutomata(Automata):
    begin_char: str = field(init=True, default='#')
    end_char: str = field(init=True, default='\n')

    def step(self, input_symbol: str):
        super().step(input_symbol)
        if self._current_state == self.State.STOPED:
            return self._current_state
        
        if input_symbol == self.begin_char and self._current_state in (self.State.UNDEFINED, self.State.PASSES):
            self._current_state = self.State.PASSES
            self._input.append(input_symbol)
        elif input_symbol != self.end_char and self._current_state == self.State.PASSES:
            self._input.append(input_symbol)
        else:
            self._current_state = self.State.STOPED
        
        return self._current_state