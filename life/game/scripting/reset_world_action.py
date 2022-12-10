import random
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the cycle collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        for actor in ["player1", "player2"]:
            player = cast.get_first_actor(actor)
            cycle = player.get_cycle()
            cycle.grow_tail(1)

            # score = player.get_score()
            # head = cycle.get_head()

            # food = cast.get_first_actor("foods")
            # if head.get_position().equals(food.get_position()):
            #     points = food.get_points()
            #     cycle.grow_tail(points)
            #     score.add_points(points)
            #     food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        # Get an actor in the list and check for collisions with
        # self and other actors.
        for actor1 in ["player1", "player2"]:
            player1 = cast.get_first_actor(actor1)
            score = player1.get_score()
            head = player1.get_cycle().get_segments()[0]

            for actor2 in ["player1", "player2"]:
                player2 = cast.get_first_actor(actor2)
                segments = player2.get_cycle().get_segments()[2:]
                
                for segment in segments:
                    if head.get_position().equals(segment.get_position()):
                        # Subtract points, i.e. lives.
                        score.sub_points(1)

                        if score.get_points() <= 0:
                            self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # Find out who won by checking who has lives (score) left.
            message = Actor()
            winner = ""
            for actor in ["player1", "player2"]:
                player = cast.get_first_actor(actor)
                score = player.get_score()
                if score.get_points() > 0:
                    winner = player.get_text() + " WINS!"
                    message.set_color(player.get_cycle().get_color())
                    score.set_font_size(constants.FONT_SIZE * 2)    # double score font
                    break

            message.set_text(winner.upper())
            message.set_position(position)
            message.set_font_size(constants.FONT_SIZE * 2)
            cast.add_actor("messages", message)

            # food = cast.get_first_actor("foods")
            # food.set_color(constants.WHITE)

            for actor in ["player1", "player2"]:
                player = cast.get_first_actor(actor)
                segments = player.get_cycle().get_segments()

                for segment in segments:
                    segment.set_color(constants.WHITE)
