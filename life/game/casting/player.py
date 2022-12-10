import constants
from game.casting.actor import Actor


class Player(Actor):
    """
    A player in the game.
    Controls the cursor and state of the game.

    _state: The current state of the game.
    """

    def __init__(self, state):
        super().__init__()
        self._state = state


    def get_state(self):
        return self._state

    def set_cycle(self, state):
        self._state = state

