"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle
from random import randint, choice, random

colors = ('red', 'yellow', 'blue', 'green', 'brown')
turns = (turtle.right, turtle.left)
moves = (turtle.forward, turtle.backward)

turtle.screensize(200, 200)


def square(size):
    turtle.color(choice(colors), choice(colors))
    turtle.begin_fill()
    turn = choice(turns)
    move = choice(moves)
    for _ in range(4):
        move(size)
        turn(90)
    turtle.end_fill()

def get_rand_pos():
    return (random() - .5) * randint(50, 300)

def draw(total):
    for i in range(total):
        turtle.penup()
        x = get_rand_pos()
        y = get_rand_pos()
        print(x, y)
        turtle.goto(x, y)
        turtle.pendown()
        square(randint(10, 300))

draw(10)
    
