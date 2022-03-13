import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Poin


class restart(Action):

    def __init__(self):
        self._is_game_over = False

    def _handle_game_over(self, cast):
        pass