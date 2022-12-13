import random
import constants
from game.casting.actor import Actor
from game.casting.player import Player
from game.casting.world import World
from game.casting.banner import Banner
from game.scripting.action import Action
from game.shared.point import Point

class GenerateNewWorldAction(Action):
    """
    Generates a new world array from the world array.
    """

    def __init__(self):
        """Create action that will generate a new grid from the existing world grid."""
        pass

    def execute(self, cast, script):
        """Executes the generate new world action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # Get the player and check the run state.
        player: Player = cast.get_first_actor("player")
        if player.get_state() == constants.STATE_RUN:
            world: World = cast.get_first_actor("world")
            self._wrap_endless_world(world)
            self._generate_new_world(world)

            # Now update the banner.
            banner: Banner = cast.get_first_actor("banner")
            banner.set_text(f"Generation: {world.get_generation()}")


    def _wrap_endless_world(self, world: World):
        """
        Wrap the borders on the grid for an 'endless' world.
        """
        grid = world.get_grid()
        rows = world.get_rows()
        cols = world.get_columns()

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


    def _generate_new_world(self, world: World):
        """ Generate a new grid from the existing grid. Then update existing grid.
        """
        grid = world.get_grid()
        next_grid = world.get_next_grid()
        ROWS = world.get_rows()
        COLS = world.get_columns()

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
                    world.increment_cell_count()
                    cell = 1
                elif cell == 1 and n < 2:       # Lonely
                    world.decrement_cell_count()
                    cell = 0
                elif cell == 1 and n > 3:       # Crowded
                    world.decrement_cell_count()
                    cell = 0
                next_grid[r][c] = cell

        # Update main grid.
        for c in range(1, COLS+1):
            for r in range(1, ROWS+1):
                grid[r][c] = next_grid[r][c]

        # Update generations
        world.increment_generation()
