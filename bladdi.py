import turtle as trtl
painter = trtl.Turtle()
painter.speed(10)

flowers = {
    "flower" : "Daisy",
    "flower" : "Lily", 
    "flower" : "Marigold",
    "flower" : "Rose",
    "flower" : "Tulip"
}

flowers = ["Daisy", "Lily", "Marigold", "Rose", "Tulip"] #available flowers
print("The available flowers are", flowers)

flower_input = ("Give me your prompt: ")
split = flower_input.split()
for i in split:
    if i in flowers:
        flower=i
        print(flower)
    if i.isnumeric() == True:
        numberOfFlowers=i
        print(f"Number of flowers: {numberOfFlowers}")
        

class Flower:
    def __init__(self, num_petals, num_flowers, turtle, flower_type, flower_input, split):
        self.num_petals = num_petals
        self.num_flowers = num_flowers
        self.flower_type = flower_type
        self.turtle = turtle
        self.turtle = trtl.Turtle()
        self.flower_input = flower_input
        self.split = split

    def draw_daisy():
        painter = trtl.Turtle()
        painter.begin_fill()
        painter.color("pink")
        painter.circle(30)
        painter.right(60)
        painter.penup()
        painter.goto(0,0)
        painter.pendown()
        painter.end_fill()
            

    painter.penup()
    painter.goto(0,-60)
    painter.pendown()
    painter.begin_fill()
    painter.color("pink")
    painter.circle(30)
    painter.end_fill()

    painter.penup()
    painter.goto(-30, -30)
    painter.pendown()
    painter.begin_fill()
    painter.color("pink")
    painter.circle(30)
    painter.end_fill()

    painter.penup()
    painter.goto(30, -30)
    painter.pendown()
    painter.begin_fill()
    painter.color("pink")
    painter.circle(30)
    painter.end_fill()

    painter.penup()
    painter.goto(0,-60)
    painter.pendown()
    painter.pencolor("Green")
    painter.pensize(10)
    painter.right(90)
    painter.forward(100)

    painter.penup()
    painter.goto(-10,-5)
    painter.pendown()
    painter.begin_fill()
    painter.color("yellow")
    painter.circle(10)
    painter.end_fill()

    draw_daisy()

wn = trtl.Screen()
wn.mainloop()




