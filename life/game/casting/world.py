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


    # def get_grid(self):
    #     """ Get the main world grid."""
    #     return self._grid


    # def get_next_grid(self):
    #     """ Get the next world grid."""
    #     return self._next_grid


    def get_cell_count(self) -> int:
        """ Counts the number of active cells in the grid and return value. """
        cell_count = 0
        for r in range(1, self._rows):
            for c in range(1, self._columns):
                if self._grid[r][c]:
                    cell_count += 1


    # def set_cell_count(self, cell_count):
    #     """ Set the current active cell count in the grid. """
    #     self._cell_count = cell_count


    # def increment_cell_count(self):
    #     """ Increment the active cell count by one. """
    #     self._cell_count += 1


    # def decrement_cell_count(self):
    #     """ Decrement the active cell count by on."""
    #     self._cell_count -= 1
        

    def reset_world(self):
        """
        Initialize the world arrays.
        Includes extra rows and columns for boarders used in wrapping world.
        Set cell count and generation to zero.
        """        
        self._grid =     [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._next_grid = [ [0] * (self._columns+2) for i in range(self._rows+2) ]
        self._generation = 0


    def get_cell(self, r, c):
        """ Get the cell value at row and column. """
        return self._grid[r][c]


    def set_cell(self, r, c, v):
        """ Set the cell value at row and column. """
        self._grid[r][c] = v


    def generate_new_world(self):
        """ Generate a new grid into next_grid from existing grid.
        grid will be updated from next_grid when get_cell is subsequently called.
        """

        # Compute next state.
        for r in range(1, self._rows+1):                
            for c in range(1, self._columns+1):
                n = self.count_neighbors(r, c)

                # Rules
                cell = self._grid[r][c]
                if cell == 0 and n == 3:        # Birth
                    self._cell_count += 1
                    self._next_grid[r][c] = 1
                elif cell > 0 and n < 2:        # Lonely
                    self._cell_count -= 1
                    self._next_grid[r][c] = 0
                elif cell > 0 and n > 3:        # Crowded
                    self._cell_count -= 1
                    self._next_grid[r][c] = 0
                elif cell > 0:                  # Stable
                    self._next_grid[r][c] = cell + 1
                else:
                    self._next_grid[r][c] = 0

        # Swap the grids.
        temp_grid = self._grid
        self._grid = self._next_grid
        self._next_grid = temp_grid

        # for r in range(1, self._rows+1):
        #     for c in range(1, self._columns+1):
        #         self._grid[r][c] = self._next_grid[r][c]

        # Update generations
        self._generation += 1


    def count_neighbors(self, r, c) -> int:
        """ Count the number of neighbors the specified cell at row and column has and return."""
        n =  (1 if self._grid[r-1][c-1] else 0) + (1 if self._grid[r-1][c] else 0) + (1 if self._grid[r-1][c+1] else 0)
        n += (1 if self._grid[r][c-1] else 0)                                      + (1 if self._grid[r][c+1] else 0)
        n += (1 if self._grid[r+1][c-1] else 0) + (1 if self._grid[r+1][c] else 0) + (1 if self._grid[r+1][c+1] else 0)
        return n


    def wrap_endless_world(self):
        """
        Wrap the borders on the grid for an 'endless' world.
        """

        # Wrap endless world by using borders to mirror the opposite side.
        for r in range(1, self._rows+1):
            self._grid[r][0]               = self._grid[r][self._columns]
            self._grid[r][self._columns+1] = self._grid[r][1]
        
        for c in range(1, self._columns+1):
            self._grid[0][c]            = self._grid[self._rows][c]
            self._grid[self._rows+1][c] = self._grid[1][c]
        
        self._grid[0][0]                          = self._grid[self._rows][self._columns]
        self._grid[self._rows+1][self._columns+1] = self._grid[1][1]
        self._grid[self._rows+1][0]               = self._grid[1][self._columns]
        self._grid[0][self._columns+1]            = self._grid[self._rows][1]


    def randomize_grid(self, count=500):
        """Place a bunch of random cells on the next_grid. """
        for i in range(count):
            row = random.randint(1, self._rows)
            col = random.randint(1, self._columns)
            self._grid[row][col] = 1


    def insert_up_left_glider(self, row, column):
        """ Insert a down left glider at the specified row and column."""
        # **
        # * *
        # *
        if row + 2 > self._rows:
            row -= 2
        if column + 2 > self._columns:
            column -= 2
        self._grid[row]    [column] = 1
        self._grid[row]    [column+1] = 1
        self._grid[row]    [column+2] = 0
        self._grid[row + 1][column] = 1
        self._grid[row + 1][column+1] = 0
        self._grid[row + 1][column+2] = 1
        self._grid[row + 2][column] = 1
        self._grid[row + 2][column+1] = 0
        self._grid[row + 2][column+2] = 0


    def insert_up_right_glider(self, row, column):
        """ Insert an up left glider at the specified row and column."""
        #  **
        # * *
        #   *
        if row + 2 > self._rows:
            row -= 2
        if column + 2 > self._columns:
            column -= 2
        self._grid[row]    [column] = 0
        self._grid[row]    [column+1] = 1
        self._grid[row]    [column+2] = 1
        self._grid[row + 1][column] = 1
        self._grid[row + 1][column+1] = 0
        self._grid[row + 1][column+2] = 1
        self._grid[row + 2][column] = 0
        self._grid[row + 2][column+1] = 0
        self._grid[row + 2][column+2] = 1

    def insert_down_left_glider(self, row, column):
        """ Insert a down left glider at the specified row and column."""    
        # *
        # * *
        # **
        if row + 2 > self._rows:
            row -= 2
        if column + 2 > self._columns:
            column -= 2
        self._grid[row]    [column] = 1
        self._grid[row]    [column+1] = 0
        self._grid[row]    [column+2] = 0
        self._grid[row + 1][column] = 1
        self._grid[row + 1][column+1] = 0
        self._grid[row + 1][column+2] = 1
        self._grid[row + 2][column] = 1
        self._grid[row + 2][column+1] = 1
        self._grid[row + 2][column+2] = 0

    def insert_down_right_glider(self, row, column):
        """ Insert a down left glider at the specified row and column."""    
        #   *
        # * *
        #  **
        if row + 2 > self._rows:
            row -= 2
        if column + 2 > self._columns:
            column -= 2
        self._grid[row]    [column] = 0
        self._grid[row]    [column+1] = 0
        self._grid[row]    [column+2] = 1
        self._grid[row + 1][column] = 1
        self._grid[row + 1][column+1] = 0
        self._grid[row + 1][column+2] = 1
        self._grid[row + 2][column] = 0
        self._grid[row + 2][column+1] = 1
        self._grid[row + 2][column+2] = 1


    def insert_pattern_6(self, row, column):
        """ Insert pattern '6' at the specified row and column."""    
        # *** *
        # *
        #    **
        #  ** *
        # * * *
        if row + 4 > self._rows:
            row -= 4
        if column + 4 > self._columns:
            column -= 4
        self._grid[row]    [column]   = 1
        self._grid[row]    [column+1] = 1
        self._grid[row]    [column+2] = 1
        self._grid[row]    [column+3] = 0
        self._grid[row]    [column+4] = 1
        self._grid[row + 1][column]   = 1
        self._grid[row + 1][column+1] = 0
        self._grid[row + 1][column+2] = 0
        self._grid[row + 1][column+3] = 0
        self._grid[row + 1][column+4] = 0
        self._grid[row + 2][column]   = 0
        self._grid[row + 2][column+1] = 0
        self._grid[row + 2][column+2] = 0
        self._grid[row + 2][column+3] = 1
        self._grid[row + 2][column+4] = 1
        self._grid[row + 3][column]   = 0
        self._grid[row + 3][column+1] = 1
        self._grid[row + 3][column+2] = 1
        self._grid[row + 3][column+3] = 0
        self._grid[row + 3][column+4] = 1
        self._grid[row + 4][column]   = 1
        self._grid[row + 4][column+1] = 0
        self._grid[row + 4][column+2] = 1
        self._grid[row + 4][column+3] = 0
        self._grid[row + 4][column+4] = 1
