from turtle import *

speed(10)
color('yellow','purple')
width(6)
penup()
goto(-200,0)
pendown()
begin_fill()
for i in range(12):
    forward(300)
    left(150)
end_fill()
mainloop()