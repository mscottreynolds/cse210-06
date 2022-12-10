import constants

from game.casting.cast import Cast
from game.casting.banner import Banner
from game.casting.world import World
from game.casting.player import Player
from game.directing.director import Director
from game.scripting.script import Script
from game.scripting.control_cursor_action import ControlCursorAction
from game.scripting.draw_new_world_action import DrawNewWorldAction
from game.scripting.generate_new_world_action import GenerateNewWorldAction
from game.scripting.move_cursor_action import MoveCursorAction
from game.scripting.reset_world_action import ResetWorldAction
from game.scripting.update_world_action import UpdateWorldAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    # create the cast
    # Player: Set cursor postiion to middle of the screen.
    player = Player()
    x = int(constants.MAX_X / 2)      # Left side of screen.
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    player.set_position(position)
    # Set initial state.
    player.set_state(constants.STATE_INITIAL)

    world = World()
    banner = Banner()

    cast = Cast()
    cast.add_actor("player", player)
    cast.add_actor("world", world)
    cast.add_actor("banner", banner)
   
    # Services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("initialize", ResetWorldAction())
    script.add_action("input", ControlCursorAction(keyboard_service))
    script.add_action("update", MoveCursorAction())
    script.add_action("update", GenerateNewWorldAction())
    script.add_action("output", DrawNewWorldAction(video_service))
    script.add_action("output", UpdateWorldAction())
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()