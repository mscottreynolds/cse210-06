import constants
from game.scripting.action import Action
from game.casting.player import Player
from game.casting.world import World
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.scripting.script import Script


class ControlCursorAction(Action):
    """
    An input action that controls the player's cursor.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service: KeyboardService):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast: Cast, script: Script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # Get the player
        player: Player = cast.get_first_actor("player")
        player_row = player.get_row()
        player_col = player.get_column()

        message: Actor = cast.get_first_actor("message")

        # Check game state.
        if player.get_state() == constants.STATE_PAUSE:
            # Keys that can be pressed while paused.
            if self._keyboard_service.is_key_down("r") or \
               self._keyboard_service.is_key_down("enter"):
                player.set_state(constants.STATE_RUN)
                message.set_text(constants.MSG_RUNNING)

            
            if self._keyboard_service.is_key_down("i") or \
                self._keyboard_service.is_key_down("up"):
                if player_row > 1:
                    player_row -= 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_row(player_row)
            
            if self._keyboard_service.is_key_down("k") or \
                self._keyboard_service.is_key_down("down"):
                if player_row < constants.ROWS:
                    player_row += 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_row(player_row)
            
            if self._keyboard_service.is_key_down("j") or \
                self._keyboard_service.is_key_down("left"):
                if player_col > 1:
                    player_col -= 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_column(player_col)

            if self._keyboard_service.is_key_down("l") or \
                self._keyboard_service.is_key_down("right"):
                if player_col < constants.COLUMNS:
                    player_col += 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_column(player_col)

            # Check for setting and clearing of cells.
            world: World = cast.get_first_actor("world")
            grid = world.get_grid()
            if self._keyboard_service.is_key_down("s") or \
                self._keyboard_service.is_key_down("space"):
                if grid[player_row][player_col] == 0:
                    world.increment_cell_count()
                    grid[player_row][player_col] = 1
            
            if self._keyboard_service.is_key_down("x"):
                if grid[player_row][player_col] == 1:
                    world.decrement_cell_count()
                    grid[player_row][player_col] = 0

            if self._keyboard_service.is_key_down("q"):
                player.set_state(constants.STATE_QUIT)

            if self._keyboard_service.is_key_down("c"):
                # Clear the grid.
                if world.get_cell_count() > 0:
                    world.reset_world()
        else:
            # keys that can be pressed while running
            if self._keyboard_service.is_key_down("p"):
                player.set_state(constants.STATE_PAUSE)
                message.set_text(constants.MSG_PAUSED)

