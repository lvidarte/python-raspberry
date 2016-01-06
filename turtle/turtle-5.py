import turtle
from random import randint

screen = turtle.getscreen()
screen.screensize(400, 300)

turtles = []
for _ in range(10):
    turtles.append(turtle.Turtle())

for t in turtles:
    t.right(randint(1, 360))
    t.forward(randint(1, 10) * 10)
