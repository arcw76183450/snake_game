from __future__ import annotations

import time
from turtle import Screen
from tkinter import messagebox
from sys import exit

from food import Food
from scoreboard import Scoreboard
from snake import Snake

segments = []
screen = Screen()
snake: None | Snake = None
food: None | Food = None
score: None | Scoreboard = None
is_game_on = True


def setup_screen():
    """
    Function for creating the screen on which game will be played
    :return:
    """
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)


def create_game():
    """
    Function for initialising game elements
    """
    global snake
    global food
    global score
    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen.update()


def listen_keystrokes():
    """
    Listener function to run snake functions when keys are pressed
    """
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake_game, "r")


def check_collision():
    """
    Checks all the collisions on the snake
    """
    # collision with food
    if snake.head.distance(food) < 15:
        food.choose_random_place()
        score.add_score()
        snake.extend()

    # collision with wall
    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        global is_game_on
        is_game_on = False

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False


def run_snake():
    """
    Responsible for in game actions and post game info display
    """
    global is_game_on
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        listen_keystrokes()
        check_collision()
    if messagebox.askyesno("Game Over", f"You have score of {score.score}. Do you want to play again?"):
        snake_game()
    else:
        exit(0)


def snake_game():
    """
    Driver method of the snake game
    """
    screen.clear()
    setup_screen()
    create_game()
    run_snake()
    screen.exitonclick()


if __name__ == '__main__':
    snake_game()
