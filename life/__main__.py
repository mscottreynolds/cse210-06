import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.casting.player import Player
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    # Player 1: Setup initial cycle and score position.
    x = int(0)      # Left side of screen.
    y = int(constants.MAX_Y / 2)
    position1 = Point(x, y)
    velocity1 = Point(constants.CELL_SIZE, 0)
    cycle1 = Cycle(constants.GREEN, position1, velocity1)

    score1 = Score()
    score1.set_color(constants.GREEN)
    score1.set_points(1)        # Start out with three lives.
    score1.set_position(Point(int(constants.MAX_X / 4), 0))
    score1.set_text("GREEN")
    player1 = Player(cycle1, score1, "Green")

    # Player2: Setup initial cycle and score position.
    x = int(constants.MAX_X)     # Right side of screen.
    y = int(constants.MAX_Y / 2)
    position2 = Point(x, y)
    velocity2 = Point(-constants.CELL_SIZE, 0)
    cycle2 = Cycle(constants.BLUE, position2, velocity2)
    score2 = Score()
    score2.set_color(constants.BLUE)
    score2.set_points(1)        # Start out with three lives.
    score2.set_position(Point(int(constants.MAX_X / 4) * 3, 0))
    score2.set_text("BLUE")
    player2 = Player(cycle2, score2, "Blue")

    cast = Cast()
    # cast.add_actor("foods", Food())
    cast.add_actor("player1", player1)
    cast.add_actor("player2", player2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()