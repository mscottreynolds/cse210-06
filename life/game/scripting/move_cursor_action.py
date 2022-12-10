from game.scripting.action import Action
from game.casting.cast import Cast
from game.scripting.script import Script

class MoveCursorAction(Action):
    """ Move the players cursor. """

    def __init__(self):
        super().__init__()

    def execute(self, cast: Cast, script: Script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

