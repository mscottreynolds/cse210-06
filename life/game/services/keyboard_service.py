import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

        self._keys['c'] = pyray.KEY_C
        self._keys['h'] = pyray.KEY_H
        self._keys['p'] = pyray.KEY_P
        self._keys['q'] = pyray.KEY_Q
        self._keys['r'] = pyray.KEY_R
        self._keys['x'] = pyray.KEY_X
        self._keys['space'] = pyray.KEY_SPACE
        self._keys['enter'] = pyray.KEY_ENTER
        self._keys['left'] = pyray.KEY_LEFT
        self._keys['right'] = pyray.KEY_RIGHT
        self._keys['up'] = pyray.KEY_UP
        self._keys['down'] = pyray.KEY_DOWN
        self._keys['?'] = pyray.KEY_SLASH
        self._keys['1'] = pyray.KEY_ONE
        self._keys['2'] = pyray.KEY_TWO
        self._keys['3'] = pyray.KEY_THREE
        self._keys['4'] = pyray.KEY_FOUR
        self._keys['5'] = pyray.KEY_FIVE
        self._keys['6'] = pyray.KEY_SIX
        self._keys['7'] = pyray.KEY_SEVEN
        self._keys['8'] = pyray.KEY_EIGHT
        self._keys['9'] = pyray.KEY_NINE
        self._keys['0'] = pyray.KEY_ZERO


    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)

    def is_key_pressed(self, key):
        """ Check to see if the key has been pressed once.
        Args: key (string) to check."""
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_pressed(pyray_key)