"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle

t = turtle.Pen()
t.speed(0)

for x in range(100):
    t.forward(x)
    t.left(90)
