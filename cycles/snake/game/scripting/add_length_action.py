from game.scripting.action import Action
import random
class AddLengthAction(Action):
    
    def execute(self, cast, script):
        self._add_tail(cast, script)
        return super().execute(cast, script)

    def _add_tail(self, cast, script):
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        # food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("player1")
        snake2 = cast.get_first_actor("player2")
        head = snake.get_head()

        # if head.get_position().equals(food.get_position()):
        #     points = food.get_points()
        #     snake.grow_tail(points)
        #     snake2.grow_tail(points)
        #     score1.add_points(points)
        #     score2.add_points(points)
        #     # food.reset()
        # if 5 == random.randint(1,5):
        snake.grow_tail(1)
        snake2.grow_tail(1)
