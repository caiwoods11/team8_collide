from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here!
class MoveActorsAction(Action): 

# Override the execute(cast, script) method as follows:

# 1) get all the actors from the cast
    def execute(self, cast, script):

# 2) loop through the actors
        actors = cast.get_all_actors()
        for actor in actors:
# 3) call the move_next() method on each actor
            actor.move_next()
