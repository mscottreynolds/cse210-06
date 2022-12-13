import constants
from game.scripting.action import Action
from game.casting.banner import Banner
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.world import World
from game.scripting.script import Script
from game.shared.point import Point

class DrawWorldAction(Action):
    """
    Draws the new world grid.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast: Cast, script: Script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """


        # Clear internal buffer
        self._video_service.clear_buffer()
        
        # Get the player and if not in RUNNING state, draw it.
        player: Player = cast.get_first_actor("player")
        if player.get_state() != constants.STATE_RUN:
            self._video_service.draw_actor(player)

        # Draw the world grid.
        world: World = cast.get_first_actor("world")
        COLS = world.get_columns()
        ROWS = world.get_rows()
        grid = world.get_grid()

        # Build an array of points, or actors, that represent the cells on the screen.
        points = []
        for c in range(1, COLS+1):
            for r in range(1, ROWS+1):
                if grid[r][c]:
                    actor = Actor()
                    actor.set_text('*')
                    point = Point(c, r).scale(constants.CELL_SIZE)
                    actor.set_position(point)
                    points.append(actor)

        self._video_service.draw_actors(points)

        banner: Banner = cast.get_first_actor("banner")
        self._video_service.draw_actor(banner, False)

        message: Actor = cast.get_first_actor("message")
        self._video_service.draw_actor(message, True)

        # Flush buffer to screen.
        self._video_service.flush_buffer()
