from game.casting.actor import Actor
from game.shared.point import Point


class World(Actor):
    """
    The current world grid and the next world grid. Grids are two dimensional arrays.

    _grid: Two dimensional array.
    _next_grid: Two dimensional array for calculating new world.
    """

    def __init__(self, rows: int, columns: int):
        """
        Initialize world grids and other data.

        rows: Max rows to use in the world grid.
        columns: Max columns to use in the world grid.
        """
        super().__init__()

        self._cell_count = 0            # For keeping track of the number of in game cells.
        self._rows = rows               # Number of available rows.
        self._columns = columns         # Number of available columns.
        self._generation = 0            # Keeps track of the current generation.
        self.reset_world()              # Initialize or reset the world.


    def get_columns(self) -> int:
        """Get the max columns used in the world grid."""
        return self._columns


    def get_rows(self) -> int:
        """Get the max rows used in the world grid. """
        return self._rows


    def get_generation(self) -> int:
        """ Get the current generation count. """
        return self._generation


    def increment_generation(self):
        """ Increment the current generation by one. """
        self._generation += 1


    def get_grid(self):
        """ Get the main world grid."""
        return self._grid


    def get_next_grid(self):
        """ Get the next world grid."""
        return self._next_grid


    def get_cell_count(self):
        """ Get the current active cell count in the grid. """
        return self._cell_count


    def set_cell_count(self, cell_count):
        """ Set the current active cell count in the grid. """
        self._cell_count = cell_count


    def increment_cell_count(self):
        """ Increment the active cell count by one. """
        self._cell_count += 1


    def decrement_cell_count(self):
        """ Decrement the active cell count by on."""
        self._cell_count -= 1
        

    def reset_world(self):
        """
        Initialize the world arrays.
        Includes extra rows and columns for boarders used in wrapping world.
        Set cell count and generation to zero.
        """        
        self._grid =     [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._next_grid = [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._generation = 0
        self._cell_count = 0

