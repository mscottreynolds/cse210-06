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
            world.wrap_endless_world()
            world.generate_new_world()

            # Now update the banner.
            banner: Banner = cast.get_first_actor("banner")
            banner.set_text(f"Generation: {world.get_generation()}")

