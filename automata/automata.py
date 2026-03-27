from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass
class Automata(ABC):
    class State(Enum):
        UNDEFINED = auto()
        STOPED = auto()
        PASSES = auto()

    _current_state: 'State' = field(init=False)
    _input: list[str] = field(init=False, default_factory=lambda: [])

    def __post_init__(self):
        self._current_state = self.State.UNDEFINED

    def reset(self):
        self.current_state = self.State.UNDEFINED
        self._input = [] 

    @abstractmethod
    def step(self, input_symbol: str):
        assert len(input_symbol) == 1

    def is_accepted(self) -> bool:
        return self.current_state == self.State.PASSES
    
    def stoped(self) -> bool:
        return self.current_state == self.State.STOPED
        
    def still_running(self) -> bool:
        return self.current_state == self.State.UNDEFINED
        
    def extract_value(self) -> str:
        return ''.join(self._input)
    
    def first_step(self) -> bool:
        return len(self._input) == 0