"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle

colors = ['red', 'purple', 'blue',
          'green', 'yellow', 'orange']

turtle.bgcolor('black')


turtle.speed(0)

for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
