#You have to maximize the entire turtle application to be able to see the flower drawings
#We did this so all the flowers could fit on the screen if the user prompted the program to draw more than 8 flowers
#1.1.3

import turtle as trtl
trtl.bgcolor("lightblue")

flowers_color = {
    "daisy" : "pink",
    "lily" : "orange",
    "marigold" : "yellow",   #corresponding flowers with their respective color
    "rose" : "red",
    "tulips" : "purple"
}

flowers_upper = ["Daisies", "Lilies", "Marigolds", "Roses", "Tulips"] #these are the available flowers that return an uppercase value
flowers_lower = ["daisies", "lilies", "marigolds", "roses", "tulips"] #these are the available flowers that return an lowercase value
print("The available flowers are", flowers_upper)

flower_input = input("Give me your prompt: ").lower()
split = flower_input.split()
index = 0
number_of_flowers = 0 #base number of flowers before a user inputs anything
number_of_petals = 0  #base number of petals before user's preference

for i in split: #this splits the user's input so the program can compile each individual componenent 
    if i in flowers_lower:
        flower = i
        print(flower)
    if i.isnumeric() == True:
        if split[index+1] in flowers_lower:
            number_of_flowers = i
        else:
            if split[index+1] in ["petal","petals"]:
                number_of_petals = i
    index += 1    #increments the petal index by 1 from the starting point of 0 petals
    
if flower in "roses":
    petal_color = "red"
elif flower in "daisies":
    petal_color = "pink"
elif flower in "marigolds":
    petal_color = "yellow"  #conditions that determine whether the flower name is applicable, and if it fits the requirements
elif flower in "tulips":
    petal_color = "purple"
elif flower in "lilies":
    petal_color = "orange"

def draw_circle(radius, color):  #sets the initial guidelines for the flower
    painter = trtl.Turtle()
    painter.fillcolor(color)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()

def petal(x, y, num_petals, petal_color):  #function that draws the flowers' petals
    painter = trtl.Turtle()
    painter.penup()
    painter.goto(-315+x,50+y)
    painter.pendown()
    painter.color(petal_color)

    for i in range(num_petals):
        painter.begin_fill()
        painter.circle(75 - i, 90)
        painter.lt(20)
        painter.lt(90)
        painter.circle(75 - i, 90)
        painter.rt(80)
        painter.end_fill()

def draw_flower(set_x, set_y, num_petals, petal_color):  #main function that draws the flower
    painter = trtl.Turtle()
    x,y=painter.pos()

    x += set_x  #x coordinate
    y += set_y  #y coordinate

    #stem
    painter.penup()
    painter.goto(-300+x,-100+y)
    painter.pendown()
    painter.pensize(10)
    painter.left(90)
    painter.color("green")
    painter.forward(100)

    #petals
    petal(x, y, num_petals, petal_color)

    #bud (yellow circle in the center)
    painter.pensize(2)
    painter.penup()
    painter.goto(-270+x,30+y)
    painter.pendown()
    painter.begin_fill()
    painter.color("yellow")
    painter.circle(30)
    painter.end_fill()

x = -300
y = 0
for n in range(int(number_of_flowers)):
    draw_flower(x, y, int(number_of_petals), petal_color)  #draws the final flower with the number of petals, and the color of the petals
    x += 200  

trtl.done()
wn = trtl.Screen()  #ends the turtle program to avoid it from closing the window
wn.mainloop()
