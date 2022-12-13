from game.casting.actor import Actor
from game.shared.point import Point


class World(Actor):
    """
    The current world grid and the next world grid. Grids are two dimensional arrays.

    _grid: Two dimensional array.
    _next_grid: Two dimensional array for calculating new world.
    """

    def __init__(self, rows: int, columns: int):
        super().__init__()

        self._cell_count = 0            # For keeping track of the number of in game cells.
        self._rows = rows               # Number of available rows.
        self._columns = columns         # Number of available columns.
        self._generation = 0            # Keeps track of the current generation.
        self.reset_world()              # Initialize or reset the world.


    def get_columns(self) -> int:
        return self._columns


    def get_rows(self) -> int:
        return self._rows


    def get_generation(self) -> int:
        return self._generation


    def increment_generation(self):
        self._generation += 1


    def get_grid(self):
        return self._grid


    def get_next_grid(self):
        return self._next_grid


    def get_cell_count(self):
        return self._cell_count


    def set_cell_count(self, cell_count):
        self._cell_count = cell_count


    def increment_cell_count(self):
        self._cell_count += 1


    def decrement_cell_count(self):
        self._cell_count -= 1
        

    def reset_world(self):
        """
        Initialize the world arrays.
        Includes extra rows and columns for boarders used in wrapping world.
        """        
        self._grid =     [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._next_grid = [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._generation = 0
        self._cell_count = 0

