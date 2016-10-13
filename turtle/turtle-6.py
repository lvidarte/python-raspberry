"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle
from random import random, randint

#turtle.screensize(200, 200)
turtle.speed(0)

def get_pos(turtle):
    return [int(n) for n in turtle.position()]

def star(size, angle):
    origin = get_pos(turtle)
    while True:
        turtle.forward(size)
        turtle.right(angle)
        if get_pos(turtle) == origin:
            break

def get_rand_axis(offset=150):
    return (random() + .5) * offset

def get_rand_pos():
    return (get_rand_axis(), get_rand_axis())

def rand_move():
    turtle.penup()
    turtle.right(randint(1, 360))
    turtle.forward(randint(100, 150))
    #turtle.goto(*get_rand_pos())
    turtle.pendown()


rand_move()
star(100, 130)
rand_move()
star(200, 175)
rand_move()
star(50, 200)
