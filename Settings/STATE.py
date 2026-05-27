from enum import Enum

class State(Enum):
    NEUTRAL = "neutral"
    CLEARING = "clearing inventory"
    UPDATING = "updating inventory"
    DECK_CHECK = "deck check"