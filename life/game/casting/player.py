import constants
from game.casting.actor import Actor


class Player(Actor):
    """
    A player in the game.
    Controls the cursor and state of the game.

    _state: The current state of the game.
    """

    def __init__(self):
        """ Initialize row, col, and state. """
        super().__init__()
        self._row = 0               # The current row the player cursor is on.
        self._col = 0               # The current column the player cursor is on.
        self._state = None          # The state the player is in.
        self._display_help = False  # True if help is being displayed for the user.


    def get_state(self):
        """Get player's state. """
        return self._state


    def set_state(self, state):
        """Set player's state."""
        self._state = state


    def get_row(self):
        """Get the row the player's cursor is on."""
        return self._row


    def get_column(self):
        """Get the column the player's cursor is on."""
        return self._col


    def set_row(self, row):
        """Set the row the player's cursor is on."""
        self._row = row
    

    def set_column(self, col):
        """Set the column the player's cursor is on."""
        self._col = col

    def set_help(self, display_help):
        """Set the flag for displaying help to the user."""    
        self._display_help = display_help

    def get_help(self):
        """Get the flag for displaying help to the user."""
        return self._display_help

