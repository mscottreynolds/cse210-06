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
            world: World = cast.get_first_actor("player")
            world.reset_world()
            player.set_state(constants.STATE_PAUSE) 

