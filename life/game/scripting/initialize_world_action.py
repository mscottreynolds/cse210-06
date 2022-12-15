import random
import constants
from game.casting.actor import Actor
from game.casting.world import World
from game.casting.player import Player
from game.scripting.action import Action
from game.shared.point import Point

class InitializeWorldAction(Action):
    """
    Resets the world and new world arrays.
    """

    def __init__(self):
        """ Create action for initializing world. """
        return

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player: Player = cast.get_first_actor("player")
        if player.get_state() == constants.STATE_INITIAL:
            # Initialize and then set state to PAUSE.
            world: World = cast.get_first_actor("world")
            message: Actor = cast.get_first_actor("message")
            world.reset_world()
            # player.set_state(constants.STATE_PAUSE)
            # message.set_text(constants.MSG_PAUSED)

            # Insert a starting pattern at center of screen.
            row = int(world.get_rows() / 2 + 1)
            col = int(world.get_columns() / 2 + 1)
            world.insert_pattern_6(row, col)
            # grid = world.get_grid()
            # grid[offset_row]    [offset_col] = 1
            # grid[offset_row]    [offset_col+1] = 0
            # grid[offset_row]    [offset_col+2] = 0
            # grid[offset_row + 1][offset_col] = 0
            # grid[offset_row + 1][offset_col+1] = 1
            # grid[offset_row + 1][offset_col+2] = 1
            # grid[offset_row + 2][offset_col] = 1
            # grid[offset_row + 2][offset_col+1] = 1
            # grid[offset_row + 2][offset_col+2] = 0
            # world.set_cell_count(5)

            # Now set game to paused.
            player.set_state(constants.STATE_RUN)
            message.set_text(constants.MSG_RUNNING)