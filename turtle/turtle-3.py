import turtle
from random import randint, choice

colors = ('red', 'green', 'blue', 'orange', 'magenta', 'cyan')

turtle.width(2)

def draw(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    rand_poligon()
    
def rand_poligon():
    turtle.color(choice(colors))
    length = randint(10, 100)
    sides = randint(3, 6)
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)

turtle.onscreenclick(draw)

turtle.listen()
