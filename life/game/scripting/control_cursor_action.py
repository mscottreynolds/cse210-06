import constants
from game.scripting.action import Action
from game.casting.player import Player
from game.casting.world import World
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.banner import Banner
from game.casting.message import Message
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


    def _update_banner(self, cast: Cast, row, col, value):
        """ Update the banner to reflect the row and column the cursor is on. 
        Only used when game is paused."""
        banner: Banner = cast.get_first_actor("banner")
        banner.set_text(f"Cursor Row: {row}  Column: {col}  Cell: {value}")


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

        message: Message = cast.get_first_actor("message")
        world: World = cast.get_first_actor("world")

        # Check game state.
        if player.get_state() == constants.STATE_PAUSE:
            # Keys that can be pressed while paused.

            # Toggle pause
            if self._keyboard_service.is_key_pressed("p") or \
                self._keyboard_service.is_key_pressed("space") or \
                self._keyboard_service.is_key_pressed("enter"):
                player.set_state(constants.STATE_RUN)
                message.set_text(constants.MSG_RUNNING)
                message.reset_timer()
                player.set_help(False)

            # Move cursor up.
            if self._keyboard_service.is_key_pressed("i") or \
                self._keyboard_service.is_key_down("up"):
                if player_row > 1:
                    player_row -= 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_row(player_row)
                    self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))
            
            # Move cursor down.
            if self._keyboard_service.is_key_pressed("k") or \
                self._keyboard_service.is_key_down("down"):
                if player_row < constants.ROWS:
                    player_row += 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_row(player_row)
                    self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))
            
            # Move cursor left.
            if self._keyboard_service.is_key_pressed("j") or \
                self._keyboard_service.is_key_down("left"):
                if player_col > 1:
                    player_col -= 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_column(player_col)
                    self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))

            # Move cursor right.
            if self._keyboard_service.is_key_pressed("l") or \
                self._keyboard_service.is_key_down("right"):
                if player_col < constants.COLUMNS:
                    player_col += 1
                    player.set_position(Point(player_col, player_row).scale(constants.CELL_SIZE))
                    player.set_column(player_col)
                    self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))

            # Check for setting and clearing of cells.
            # Generation count is set back to zero every time a change is made.
            if self._keyboard_service.is_key_down("s"):
                world.set_cell(player_row, player_col, 1)
                # if grid[player_row][player_col] == 0:
                    # world.increment_cell_count()
                    # grid[player_row][player_col] = 1
                self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))
                world.set_generation(0)
            
            # Clear cell.
            if self._keyboard_service.is_key_down("x"):
                # if grid[player_row][player_col] == 1:
                    # world.decrement_cell_count()
                    # grid[player_row][player_col] = 0
                world.set_cell(player_row, player_col, 0)
                self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))
                world.set_generation(0)

            # Insert gliders.
            if self._keyboard_service.is_key_pressed("1"):
                # Insert a glider at cursor position.
                world.insert_down_right_glider(player_row, player_col)
                world.set_generation(0)

            if self._keyboard_service.is_key_pressed("2"):
                # Insert a glider at cursor position.
                world.insert_up_right_glider(player_row, player_col)
                world.set_generation(0)

            if self._keyboard_service.is_key_pressed("3"):
                # Insert a glider at cursor position.
                world.insert_down_left_glider(player_row, player_col)
                world.set_generation(0)

            if self._keyboard_service.is_key_pressed("4"):
                # Insert a glider at cursor position.
                world.insert_up_left_glider(player_row, player_col)
                world.set_generation(0)

            # Insert pattern '6'
            if self._keyboard_service.is_key_pressed("6"):
                world.insert_pattern_6(player_row, player_col)
                world.set_generation(0)

            # Clear screen/grid.
            if self._keyboard_service.is_key_pressed("c"):
                # Clear the grid.
                # player.set_help(False)
                # if world.get_cell_count() > 0:
                world.reset_world()
                self._update_banner(cast, player_row, player_col, world.get_cell(player_row, player_col))
                world.set_generation(0)

            # Display help.
            if self._keyboard_service.is_key_pressed("h"):
                if player.get_help():
                    player.set_help(False)
                else:
                    player.set_help(True)

        else:
            # Keys that can be pressed while running

            # Pause game.
            if self._keyboard_service.is_key_pressed("p") or \
                self._keyboard_service.is_key_pressed("space"):
                player.set_state(constants.STATE_PAUSE)
                message.set_text(constants.MSG_PAUSED)
                message.disable_timer()

        # Randomize screen.
        if self._keyboard_service.is_key_down("5"):
            # Place a bunch of random cells on grid. Use constants.COLUMNS as a count.
            world.randomize_grid(int(constants.COLUMNS))
            world.set_generation(0)

        # quit.
        if self._keyboard_service.is_key_pressed("q"):
            player.set_state(constants.STATE_QUIT)

