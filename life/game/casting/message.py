from game.casting.actor import Actor
from game.shared.point import Point


class Message(Actor):
    """
    Message to be displayed on the screen with a countdown timer.
    """
    def __init__(self):
        super().__init__()
        self._timer = 0             # The number of times get_text call be called.
        self._timer_reset = 0       # Contains original timer value for resetting.
        self._enable_timer = False  # When true, timer activates.

    
    def set_timer(self, timer: int):
        """ Set and enable the timer. Timer is decremented everytime get_text() is called.
        When the timer reaches zero, the get_text() method will return an empty string.
        """
        self._timer = timer
        self._timer_reset = timer
        self._enable_timer = True


    def get_timer(self) -> int: 
        """Return the current timer value."""
        return self._timer


    def get_timer_reset(self) -> int:
        """ Gets the timer reset value or the value that was set with the last
        set_timer call."""
        return self._timer_reset


    def get_text(self):
        """ Override get_text. Decrements timer everytime this is called. 
        When timer reaches zero, an empty string will be returned."""
        if self._timer > 0:
            self._timer -= 1
            return super().get_text()
        elif self._enable_timer:
            # If timer has been enabled and timer is zero then return empty string.
            return ""
        else:
            return super().get_text()


    def reset_timer(self):
        """ Reset and enable the timer."""
        self._timer = self._timer_reset
        self._enable_timer = True


    def disable_timer(self):
        """ Disable the timer so get_text will behave normally."""
        self._enable_timer = False

    
    def enable_timer(self):
        """Enable the timer. """
        self._enable_timer = True
        