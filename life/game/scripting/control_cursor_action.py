import constants
from game.scripting.action import Action
from game.casting.player import Player
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        # self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # Player 1
        player1 = cast.get_first_actor("player1")
        cycle1 = player1.get_cycle()
        direction1 = cycle1.get_head().get_velocity()

        # left
        if self._keyboard_service.is_key_down('a'):
            direction1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            direction1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            direction1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            direction1 = Point(0, constants.CELL_SIZE)
        
        cycle1.turn_head(direction1)

        # Player 2
        player2 = cast.get_first_actor("player2")
        cycle2 = player2.get_cycle()
        direction2 = cycle2.get_head().get_velocity()

        # left
        if self._keyboard_service.is_key_down('j'):
            direction2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            direction2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            direction2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            direction2 = Point(0, constants.CELL_SIZE)
        
        cycle2.turn_head(direction2)
