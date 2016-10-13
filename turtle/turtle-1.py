"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

from turtle import *
from random import choice


colors = ('red', 'blue', 'green', 'purple', 'orange')

onscreenclick(goto)
onscreenclick(lambda x, y: pencolor(choice(colors)), btn=3)
