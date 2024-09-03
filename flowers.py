import turtle as trtl
screen = trtl.Screen()
painter = trtl.Turtle()

for i in range(6):
    painter.begin_fill()
    painter.color("pink")
    painter.circle(30)
    painter.right(60)
    painter.penup()
    painter.goto(0,0)
    painter.pendown()
    painter.end_fill()

painter.penup()
painter.goto(0,-30)
painter.pendown()
painter.begin_fill()
painter.color("yellow")
painter.circle(30)
painter.end_fill()

painter.penup()
painter.goto(0,-60)
painter.pendown()
painter.pencolor("Green")
painter.pensize(10)
painter.right(90)
painter.forward(100)

wn = trtl.Screen()
wn.mainloop()
