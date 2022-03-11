from game.scripting.action import Action
from game.scripting.handle_collisions_action import HandleCollisionsAction
import random

class AddLengthAction(Action):
    
    def execute(self, cast, script):
        self._add_tail(cast, script)
        return super().execute(cast, script)

    def _add_tail(self, cast, script):
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        snake = cast.get_first_actor("player1")
        snake2 = cast.get_first_actor("player2")
        head = snake.get_head()
        
        if HandleCollisionsAction.gameOver == False:
            snake.grow_tail(1, "player1")
            snake2.grow_tail(1, "player2")
