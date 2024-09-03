import turtle as trtl

flowers_options = ["Daisy", "Lily", "Roses", "Marigold", "Tulip"] #avaiable flowers that the application can draw
print(flowers_options)

def draw_single_flower():
            flower_type = input("What type of flower do you want me to draw?: ")
            if flower_type in flowers_options and flower_type == "Daisy" or flower_type == "daisy".lower():
                print("Sure, I will draw a daisy")
                turtle = open(trtl)
                screen = trtl.Screen()
                painter = trtl.Turtle()
                #flower petal
                for flower in range(6):
                    painter.pendown()
                    painter.begin_fill()
                    painter.color("pink")
                    painter.circle(30)
                    painter.right(60)
                    painter.penup()
                    painter.goto(0,0)
                    painter.pendown()
                    painter.end_fill()
            #stem of the flower        
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

def draw_multiple_flowers(number_of_flowers):
    for flower in range(number_of_flowers):
        draw_single_flower()
        screen = trtl.Screen()
        painter = trtl.Turtle()

        for i in range(6):
            painter.pendown()
            painter.begin_fill()
            painter.color("pink")
            painter.circle(30)
            painter.right(60)
            painter.penup()
            painter.goto(0,0)
            painter.pendown()
            painter.end_fill()
        
        #stem of the flower        
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

number_of_flowers_to_draw = int(input("How many flowers do you want me to draw?: "))
draw_multiple_flowers(number_of_flowers_to_draw)

trtl.hideturtle()
trtl.done()
wn = trtl.Screen()
wn.mainloop()


