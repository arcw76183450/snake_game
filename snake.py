from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """
    The actual player object in the game
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the basic snake when the game starts
        """
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        """
        Creating different turtles to make a snake
        :param position: the position of the smaller turtles which make a snake
        """
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        """
        Adding a turtle in end to make the snake longer
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        This function handles the snake movement
        """
        for t in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[t - 1].xcor()
            new_y = self.segments[t - 1].ycor()
            self.segments[t].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        The change in direction to up when user directs it and it is a valid change
        """
        if self.head.heading() not in [UP, DOWN]:
            self.head.setheading(UP)

    def down(self):
        """
        The change in direction to down when user directs it and it is a valid change
        """
        if self.head.heading() not in [UP, DOWN]:
            self.head.setheading(DOWN)

    def left(self):
        """
        The change in direction to left when user directs it and it is a valid change
        """
        if self.head.heading() not in [LEFT, RIGHT]:
            self.head.setheading(LEFT)

    def right(self):
        """
        The change in direction to right when user directs it and it is a valid change
        """
        if self.head.heading() not in [LEFT, RIGHT]:
            self.head.setheading(RIGHT)
