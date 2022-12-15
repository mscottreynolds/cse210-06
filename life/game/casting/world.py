import random
import constants
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

    
    def set_generation(self, generation: int):
        """ Set the generation count."""
        self._generation = generation


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


    def generate_new_world(self):
        """ Generate a new grid from the existing grid. Then update existing grid.
        """
        grid = self._grid
        next_grid = self._next_grid
        ROWS = self._rows
        COLS = self._columns

        # Compute next state.
        for c in range(1, COLS+1):
            for r in range(1, ROWS+1):                
                # Count neighbors
                n =  grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1] 
                n += grid[r][c-1]                  + grid[r][c+1]  
                n += grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1]

                # Rules
                cell = grid[r][c]
                if cell == 0 and n == 3:        # Birth
                    self.increment_cell_count()
                    cell = 1
                elif cell == 1 and n < 2:       # Lonely
                    self.decrement_cell_count()
                    cell = 0
                elif cell == 1 and n > 3:       # Crowded
                    self.decrement_cell_count()
                    cell = 0
                next_grid[r][c] = cell

        # Update main grid.
        for c in range(1, COLS+1):
            for r in range(1, ROWS+1):
                grid[r][c] = next_grid[r][c]

        # Update generations
        self.increment_generation()


    def wrap_endless_world(self):
        """
        Wrap the borders on the grid for an 'endless' world.
        """
        grid = self._grid
        rows = self._rows
        cols = self._columns

        # Wrap endless world by using borders to mirror the opposite side.
        for c in range(1, cols+1):
            grid[0][c] = grid[rows][c]
            grid[rows+1][c] = grid[1][c]
        
        for r in range(1, rows+1):
            grid[r][0] = grid[r][cols]
            grid[r][cols+1] = grid[r][1]
        
        grid[0][0]             = grid[rows][cols]
        grid[rows+1][cols+1] = grid[1][1]
        grid[rows+1][0]       = grid[1][cols]
        grid[0][cols+1]       = grid[rows][1]



    def randomize_grid(self, count=500):
        """Place a bunch of random cells on the grid.
        count = Number of random cells to place."""
        for i in range(count):
            row = random.randint(1, constants.ROWS)
            col = random.randint(1, constants.COLUMNS)
            self._grid[row][col] = 1
            self.increment_cell_count()


    def insert_glider(self, row, column):
        """ Insert a glider at the specified row and column."""    
        # First count the existing cell count a position.
        grid = self._grid
        offset_row = row
        offset_col = column
        old_cell_count = \
              grid[offset_row]    [offset_col]   \
            + grid[offset_row]    [offset_col+1] \
            + grid[offset_row]    [offset_col+2] \
            + grid[offset_row + 1][offset_col]   \
            + grid[offset_row + 1][offset_col+1] \
            + grid[offset_row + 1][offset_col+2] \
            + grid[offset_row + 2][offset_col]   \
            + grid[offset_row + 2][offset_col+1] \
            + grid[offset_row + 2][offset_col+2]

        grid[offset_row]    [offset_col] = 1
        grid[offset_row]    [offset_col+1] = 0
        grid[offset_row]    [offset_col+2] = 0
        grid[offset_row + 1][offset_col] = 0
        grid[offset_row + 1][offset_col+1] = 1
        grid[offset_row + 1][offset_col+2] = 1
        grid[offset_row + 2][offset_col] = 1
        grid[offset_row + 2][offset_col+1] = 1
        grid[offset_row + 2][offset_col+2] = 0

        self._cell_count += 5 - old_cell_count





