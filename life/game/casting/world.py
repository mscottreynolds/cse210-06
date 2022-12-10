from game.casting.actor import Actor
from game.shared.point import Point


class World(Actor):
    """
    The current world grid and the new world grid. Grids are two dimensional arrays.

    _world: Two dimensional array.
    _new_world: Two dimensional array for calculating new world.
    """

    def __init__(self, rows: int, columns: int):
        super().__init__()

        self._generation = 0
        self._rows = rows
        self._columns = columns
        self.reset_world()


    def get_generation(self) -> int:
        return self._generation

    def get_world(self):
        return self._world
    
    def get_new_world(self):
        return self._new_world

    def reset_world(self):
        """
        Initialize the world arrays.
        Includes extra rows and columns for boarders used in wrapping world.
        """        

        self._world =     [ [None] * (self._columns+2) for i in range(self._rows+2) ]
        self._new_world = [ [None] * (self._columns+2) for i in range(self._rows+2) ]
        self._generation = 0

    def generate_new_world(self):
        """
        Calculates and generates a new world array.
        """
        return

    
    def update_world(self):
        """
        Updates the world array from the new world array.
        """
        return

