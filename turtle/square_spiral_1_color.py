import turtle

colors = ['red', 'orange', 'blue', 'green']

turtle.bgcolor('black')

t = turtle.Pen()
t.speed(0)

for x in range(100):
    t.pencolor(colors[x % 4])
    t.forward(x)
    t.left(90)
