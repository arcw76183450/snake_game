from turtle import Turtle

FONT_TYPE = "Arial"
FONT_SIZE = 12
ALIGNMENT = "center"
POSITION = (0, 285)


class Scoreboard(Turtle):
    """
    The object handling the score of the game
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(POSITION)
        self.score = 0
        self.create_score()

    def create_score(self):
        """
        This function is responsible for updating score
        """
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, "normal"))

    def add_score(self):
        """
        This function is responsible for increasing score when snake gets food
        """
        self.score += 1
        self.create_score()

    def reset_score(self):
        """
        This function is responsible for resetting score when game starts
        """
        self.score = 0
        self.create_score()
