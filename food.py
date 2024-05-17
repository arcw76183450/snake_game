from turtle import Turtle
import random


class Food(Turtle):
    """
    Food for the snake to grow
    """
    def __init__(self):
        super().__init__()
        self.setup_food()
        self.choose_random_place()

    def setup_food(self):
        """
        Creating the food turtle with all the settings
        """
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def choose_random_place(self):
        """
        Choosing the random location for food to go to
        """
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
