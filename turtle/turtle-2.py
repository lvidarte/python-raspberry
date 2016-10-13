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

turtle.width(2)

def rand_pos():
    turtle.up()
    turtle.right(randint(0, 360))
    turtle.forward(randint(10, 50))
    turtle.down()
    
def poligon(length, sides):
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)

for _ in range(20):
    rand_pos()
    turtle.color(choice(colors))
    length = randint(10, 100)
    sides = randint(3, 6)
    poligon(length, sides)
