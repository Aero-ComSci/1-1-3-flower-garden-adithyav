import turtle as trtl
screen = trtl.Screen()
screen.setup(800, 800)

painter = trtl.Turtle()
painter.shape("turtle")
painter.color("Green")
painter.speed(4)

flowers = ["Daisy", "Lily", "Roses", "Marigold", "Tulip"] #avaiable flowers that the application can draw

def daisy():
    painter.pensize(13)
    painter.penup()
    painter.goto(0, -200) 
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("green")
    painter.color("green")
    painter.right(-90)
    painter.forward(200)
    for i in range (6):
        painter.speed(10)
        painter.begin_fill()
        painter.color("black")
        painter.fillcolor("red")
        painter.pensize(8)
        painter.circle(40)
        painter.right(60)
        painter.end_fill()
        painter.penup()
daisy()

def lily():
    painter.goto(100, -200)
    painter.pendown()
    painter.color("green")
    painter.pensize(13)
    painter.forward(250)
    for i in range (6):
        painter.speed(10)
        painter.begin_fill()
        painter.color("black")
        painter.fillcolor("")
        painter.color("black")
        painter.pensize(8)
        painter.circle(40)
        painter.right(60)
        painter.end_fill()
        painter.penup()

lily()
wn = trtl.Screen()
wn.mainloop()
