from game.scripting.action import Action
from game.casting.cast import Cast
from game.scripting.script import Script

class MoveCursorAction(Action):
    """ Move the players cursor. """

    def __init__(self):
        """ Create action for moving the players cursor and other actors."""
        super().__init__()

    def execute(self, cast: Cast, script: Script):
        """ Call move_next() on all of the actors in the cast. """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

