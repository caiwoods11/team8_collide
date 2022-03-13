import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):

    gameOver = False

    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_food_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        snake = cast.get_first_actor("player1")
        head = snake.get_segments()[0]
        snake2 = cast.get_first_actor("player2")
        head2 = snake2.get_segments()[0]
        food = cast.get_first_actor("foods")

        if head.get_position().food_equals(food.get_position()):
            points = food.get_points()
            score1.add_points(points, 1)
            food.reset()

        if head2.get_position().food_equals(food.get_position()):
            points = food.get_points()
            score2.add_points(points, 2)
            food.reset()

        segments = snake.get_segments()[1:]
        segments2 = snake2.get_segments()[1:]

        for segment in segments:
            if food.get_position().food_equals(segment.get_position()):
                food.reset()
        for segment in segments2:
            if food.get_position().food_equals(segment.get_position()):
                food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        points = 3
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        snake = cast.get_first_actor("player1")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
                
        snake2 = cast.get_first_actor("player2")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score2.add_points(points, 2)
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score1.add_points(points, 1)
            if head.get_position().equals(head2.get_position()):
                self._is_game_over = True
        for segment in segments2:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score2.add_points(points, 2)
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score1.add_points(points, 1)                
            
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("player1")
            snake2 = cast.get_first_actor("player2")
            segments = snake.get_segments()
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position1 = Point(x, y)
            #position2 = Point(x, y + 20)

            message = Actor()
            message.set_text("Game Over")
            message.set_position(position1)
            message.set_font_size(50)
            message.set_color(constants.RED)
            cast.add_actor("messages", message)

            # message2 = Actor()
            # message2.set_font_size(50) 
            
            # if self._winner == 3:
            #     message.set_text("Draw!")
            #     message2.set_text("You bonked heads")
            #     message2.set_color(constants.YELLOW)
            #     message2.set_font_size(30)  

            # message2.set_position(position2)
                   
            # cast.add_actor("messages", message2)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)


            HandleCollisionsAction.gameOver = True
