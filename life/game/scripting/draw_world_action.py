
import constants
from game.scripting.action import Action
from game.casting.banner import Banner
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.world import World
from game.scripting.script import Script
from game.shared.point import Point
from game.shared.color import Color
import colorsys

def get_N_RGB(N=5):
    HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    rgb_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        # print(rgb)
        rgb_out.append(tuple(rgb))
    return rgb_out

MAX_COLOR_PALETTE = 255

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

        # Create a color palette that will be used when drawing the cells.
        self._color_palette = []
        self._color_palette.append(constants.WHITE)
        self._color_palette.append(constants.WHITE)
        self._color_palette.append(constants.WHITE)
        self._color_palette.append(constants.WHITE)
        self._color_palette.append(constants.RED)
        self._color_palette.append(constants.YELLOW)
        self._color_palette.append(constants.GREEN)
        self._color_palette.append(constants.BLUE)

        # Fill up the rest of the palettte.
        N = MAX_COLOR_PALETTE - len(self._color_palette)
        HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
        for rgb in HSV_tuples:
            rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
            self._color_palette.append(Color(*rgb))


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
        # grid = world.get_grid()

        # Build an array of points, or actors, that represent the cells on the screen.
        # points = []
        for c in range(1, COLS+1):
            for r in range(1, ROWS+1):
                cell = world.get_cell(r, c)
                if cell:
                    actor = Actor()
                    actor.set_text(constants.CELL_CHAR)
                    actor.set_font_size(constants.CELL_SIZE)
                    point = Point(c, r).scale(constants.CELL_SIZE)
                    actor.set_position(point)

                    # Setup the color
                    # if cell > MAX_COLOR_PALETTE:
                    #     cell = MAX_COLOR_PALETTE
                    actor.set_color(self._color_palette[(cell-1) % MAX_COLOR_PALETTE])

                    self._video_service.draw_actor(actor)
                    # points.append(actor)

        # self._video_service.draw_actors(points)

        banner: Banner = cast.get_first_actor("banner")
        self._video_service.draw_actor(banner, False)


        message: Actor = cast.get_first_actor("message")
        self._video_service.draw_actor(message, True)

        if player.get_help():
            msg_help: Actor = cast.get_first_actor("help-display")
            self._video_service.draw_actor(msg_help)

        # Flush buffer to screen.
        self._video_service.flush_buffer()
