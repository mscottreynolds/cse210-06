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

            # Insert a glider as a starting point.
            grid = world.get_grid()
            grid[1][1] = 1
            grid[1][2] = 0
            grid[1][3] = 0
            grid[2][1] = 0
            grid[2][2] = 1
            grid[2][3] = 1
            grid[3][1] = 1
            grid[3][2] = 1
            grid[3][3] = 0
            world.set_cell_count(5)

            # Now set game to running.
            player.set_state(constants.STATE_RUN)
            message.set_text(constants.MSG_RUNNING)