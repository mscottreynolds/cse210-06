import constants

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.banner import Banner
from game.casting.world import World
from game.casting.player import Player
from game.directing.director import Director
from game.scripting.script import Script
from game.scripting.control_cursor_action import ControlCursorAction
from game.scripting.draw_world_action import DrawWorldAction
from game.scripting.generate_new_world_action import GenerateNewWorldAction
from game.scripting.move_cursor_action import MoveCursorAction
from game.scripting.initialize_world_action import InitializeWorldAction
from game.scripting.update_world_action import UpdateWorldAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    # create the cast
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
    banner.set_position(Point(col, 0).scale(constants.CELL_SIZE))
    banner.set_font_size(constants.FONT_SIZE * 2)

    # Instructional messages.
    message = Actor()
    message.set_text(constants.MSG_PAUSED)
    message.set_position(Point(col, constants.ROWS+1).scale(constants.CELL_SIZE))

    cast = Cast()
    cast.add_actor("player", player)
    cast.add_actor("world", world)
    cast.add_actor("banner", banner)
    cast.add_actor("message", message)
   
    # Services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("initialize", InitializeWorldAction())
    script.add_action("input", ControlCursorAction(keyboard_service))
    script.add_action("update", MoveCursorAction())
    script.add_action("update", GenerateNewWorldAction())
    script.add_action("output", DrawWorldAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
    