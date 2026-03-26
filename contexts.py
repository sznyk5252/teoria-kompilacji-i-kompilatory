from enum import Enum
from typing import Callable
from functools import cache

class Context(Enum):
    BASIC = 'BASIC'
    IN_TAG = 'IN_TAG'