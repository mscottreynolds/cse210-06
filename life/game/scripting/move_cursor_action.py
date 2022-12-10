from game.scripting.action import Action
from game.casting.cast import Cast
from game.scripting.script import Script

# Implement MoveActorsAction class here! 
class MoveActorsAction(Action):

    def __init__(self):
        super().__init__()

    # Override the execute(cast, script) method as follows:
    def execute(self, cast: Cast, script: Script):
        # 1) get all the actors from the cast
        # 2) loop through the actors
        # 3) call the move_next() method on each actor
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

