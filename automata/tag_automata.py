from .automata import Automata
from dataclasses import dataclass, field

@dataclass
class TagAutomata(Automata):
    possible_tags: list[str] = field(init= True, default_factory=lambda: [])

    def step(self, input_symbol: str):
        assert len(input_symbol) == 1
        if self._current_state == self.State.STOPED:
            return

        current_prefix = self.extract_value() + input_symbol
        if any(tag.startswith(current_prefix) for tag in self.possible_tags):
            self._input.append(input_symbol)
            if current_prefix in self.possible_tags:
                self._current_state = self.State.PASSES
            else:
                self._current_state = self.State.UNDEFINED
        else:
            self._current_state = self.State.STOPED
            