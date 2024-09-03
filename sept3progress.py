#Fix: after each flower is drawn, make it so that they get separated instead of stacking on top of each other

import turtle as trtl

options = ["daisy", "rose", "lily", "tulip", "marigold"]

def daisy():
    numDaisy = int(input("How many daisies would you like me to draw?"))
    rangeDaisy = numDaisy + 1
    for i in range(1,rangeDaisy):
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

screen = trtl.Screen()
painter = trtl.Turtle()

prompt = input("Give me your prompt >:)")
if "daisy" in prompt or "daisies" in prompt:
    daisy()

wn = trtl.Screen()
wn.mainloop()
