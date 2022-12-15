import constants
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.banner import Banner
from game.casting.message import Message
from game.casting.world import World
from game.casting.player import Player
from game.scripting.script import Script
from game.scripting.control_cursor_action import ControlCursorAction
from game.scripting.draw_world_action import DrawWorldAction
from game.scripting.generate_new_world_action import GenerateNewWorldAction
from game.scripting.move_cursor_action import MoveCursorAction
from game.scripting.initialize_world_action import InitializeWorldAction
from game.scripting.update_world_action import UpdateWorldAction
from game.shared.color import Color
from game.shared.point import Point


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For providing keyboard input.
        _video_service (VideoService): For providing video output.
    """


    def __init__(self, keyboard_service: KeyboardService, video_service: VideoService):
        """Constructs a new Director using the specified video service.
        Args:
            keyboard_service (KeyboardService): For providing keyboard input.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        

    def start_game(self):
        """Starts the game using the given cast and script. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        cast = self._create_cast()
        script = self._create_script()

        # Open window.
        self._video_service.open_window()

        # Execute any initialize actions.
        self._execute_actions("initialize", cast, script)

        # Now start the loop, doing inputs, updates, and outputs.
        player: Player = cast.get_first_actor("player")
        while self._video_service.is_window_open() and player.get_state() != constants.STATE_QUIT:
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)

        # close window.
        self._video_service.close_window()


    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)          


    def _create_cast(self) -> Cast:
        """Create the cast that will be used in the game."""
        # Player: Set cursor postiion to middle of the screen.
        player = Player()
        row = int(int(constants.ROWS / 2))
        col = int(int(constants.COLUMNS / 2))
        player.set_position(Point(col, row).scale(constants.CELL_SIZE))
        player.set_row(row)
        player.set_column(col)
        player.set_state(constants.STATE_INITIAL)
        player.set_text("@")

        world = World(constants.ROWS, constants.COLUMNS)

        banner = Banner()
        banner.set_text("Life")
        banner.set_color(constants.BLUE)
        # banner.set_position(Point(col, 0).scale(constants.CELL_SIZE))        
        banner.set_font_size(constants.FONT_SIZE * 2)
        banner.set_position(Point(1, 1).scale(constants.CELL_SIZE))     # Place banner on row 1 col 1.

        # Instructional messages.
        message = Message()
        message.set_text(constants.MSG_PAUSED)
        message.set_position(Point(col, constants.ROWS-1).scale(constants.CELL_SIZE) )
        message.set_font_size(int(constants.FONT_SIZE * 1.3))
        message.set_timer(constants.FRAME_RATE * 10)       # Displayes for about a minute.

        # Help display
        message_help = Message()
        message_help.set_color(constants.YELLOW)
        message_help.set_text(constants.MSG_HELP)
        message_help.set_position(Point(1, 3).scale(constants.CELL_SIZE))   # Plase help on row 3 column 1.
        message_help.set_font_size(int(constants.FONT_SIZE*1.3))

        cast = Cast()
        cast.add_actor("player", player)
        cast.add_actor("world", world)
        cast.add_actor("banner", banner)
        cast.add_actor("message", message)
        cast.add_actor("help-display", message_help)

        return cast


    def _create_script(self) -> Script:
        """Create the scriptable actions."""
        iwa = InitializeWorldAction()
        dwa = DrawWorldAction(self._video_service)
        cca = ControlCursorAction(self._keyboard_service)
        mca = MoveCursorAction()
        gnwa = GenerateNewWorldAction()

        script = Script()
        script.add_action("initialize", iwa)
        script.add_action("initialize", dwa)
        script.add_action("input", cca)
        script.add_action("update", mca)
        script.add_action("update", gnwa)
        script.add_action("output", dwa)

        return script

