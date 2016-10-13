"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle
from random import random, randint, choice

colors = ('blue', 'red', 'yellow', 'green', 'orange', 'brown', 'cyan')
angle = None

#turtle.screensize(200, 200)
turtle.speed(0)

def get_pos(turtle):
    return [round(n) for n in turtle.position()]

def star(size, angle):
    origin = get_pos(turtle)
    while True:
        turtle.forward(size)
        turtle.right(angle)
        if get_pos(turtle) == origin:
            break

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def rand_color():
    turtle.color(choice(colors), choice(colors))

def rand_draw(x, y):
    global angle
    move(x, y)
    size = randint(10, 100)
    angle = randint(91, 179)
    print(size, angle)
    rand_color()
    turtle.begin_fill()
    star(size, angle)
    turtle.end_fill()

def re_draw(x, y):
    move(x, y)
    size = randint(10, 100)
    print(size, angle)
    rand_color()
    turtle.begin_fill()
    star(size, angle)
    turtle.end_fill()

turtle.onscreenclick(rand_draw)
turtle.onscreenclick(re_draw, btn=3)
