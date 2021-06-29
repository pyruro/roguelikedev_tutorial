"""Holds the different types of actions the player can perform"""


class Action:
    pass


class EscapeAction(Action):
    """Define how to exit the game"""
    pass


class MovementAction(Action):
    """Describe player movement"""
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
