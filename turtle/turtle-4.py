"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle
from random import randint, choice

colors = ('red', 'green', 'blue', 'orange', 'magenta', 'cyan')

turtle.hideturtle()
turtle.speed(0)

def draw(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    rand_circle()
    
def rand_circle():
    color = choice(colors)
    turtle.color(color, color)
    radius = randint(10, 100)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.onscreenclick(draw)
