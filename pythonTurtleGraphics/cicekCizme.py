from turtle import *

def kenarCiz(x, y, n, renk):
    penup()
    goto(x,y)
    pendown()
    color("blue", renk)
    begin_fill()
    for aci in range(0, 360, n):
        seth(aci)
        circle(360/n+10, 200)
    end_fill()
title("Çiçek Çizme")
speed(0)
kenarCiz(170, 20, 18, "yellow")
kenarCiz(140, 10, 20, "red")
kenarCiz(100, 0, 24, "magenta")
penup()
goto(-20, 60)
pendown()
color("purple", "green")
begin_fill()
circle(50)
end_fill()
hideturtle() # Kaplumbağayı gizleme 
done()

