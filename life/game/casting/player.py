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
        self._row = 0           # The current row the player cursor is on.
        self._col = 0           # The current column the player cursor is on.
        self._state = None      # The state the player is in.


    def get_state(self):
        return self._state


    def set_state(self, state):
        self._state = state


    def get_row(self):
        return self._row


    def get_column(self):
        return self._col


    def set_row(self, row):
        self._row = row
    

    def set_column(self, col):
        self._col = col
    

