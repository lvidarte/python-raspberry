from turtle import *
from random import choice


colors = ('red', 'blue', 'green', 'purple', 'orange')

onscreenclick(goto)
onscreenclick(lambda x, y: pencolor(choice(colors)), btn=3)
