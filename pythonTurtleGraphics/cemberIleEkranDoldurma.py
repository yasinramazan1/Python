import turtle 
from random import randint

t = turtle.Turtle()
maxx=300
maxy=300
t.reset()
t.speed(50)
t.width(4)
turtle.colormode(255)
for i in range(500):
    ycap=randint(10, 100)
    x=randint(-maxx, maxx)
    y=randint(-maxy, maxy)
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    renk=(r, g, b)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color((0, 0, 0), renk)
    t.begin_fill()
    t.circle(ycap)
    t.end_fill()
t.hideturtle()
turtle.mainloop() # turtle'ı sonlandırır.