import constants
from game.casting.actor import Actor
from game.casting.cycle import Cycle
from game.casting.score import Score

from game.shared.point import Point


class Player(Actor):
    """
    A player in the game.
    
    The responsibility of player is to keep track of its own score and cycle.

    Attributes:
        _cycle: The cycle representing this player.
        _score: The score representing this player.
    """
    def __init__(self, cycle: Cycle, score: Score, name: str):
        super().__init__()
        self._cycle = cycle
        self._score = score
        self.set_text(name)

    def get_cycle(self) -> Cycle:
        return self._cycle

    def set_cycle(self, cycle: Cycle):
        self._cycle = cycle

    def get_score(self) -> Score:
        return self._score

    def set_score(self, score) -> Score:
        self._score = score

    def move_next(self):
        self._cycle.move_next()
        