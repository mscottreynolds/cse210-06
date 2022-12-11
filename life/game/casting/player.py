import constants
from game.casting.actor import Actor


class Player(Actor):
    """
    A player in the game.
    Controls the cursor and state of the game.

    _state: The current state of the game.
    """

    def __init__(self):
        super().__init__()


    def get_state(self):
        return self._state


    def set_state(self, state):
        self._state = state

