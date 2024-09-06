import turtle as trtl

flowers_upper = ["Daisies", "Lilies", "Marigolds", "Roses", "Tulips"]
flowers_lower = ["daisies", "lilies", "marigolds", "roses", "tulips"]
print("The available flowers are", flowers_upper)
flower_input = input("Give me your prompt: ").lower()
split = flower_input.split()
index=0
numberOfFlowers=0
numberOfPetals=0
for i in split:
    if i in flowers_lower:
        flower=i
        print(flower)
    if i.isnumeric() == True:
        if split[index+1] in flowers_lower:
            numberOfFlowers=i
            
        else:
            if split[index+1] in ["petal","petals"]:
                numberOfPetals=i
    index+=1
    
if flower in "roses":
    petal_color = "red"
elif flower in "daisies":
    petal_color = "pink"
elif flower in "marigolds":
    petal_color = "yellow"
elif flower in "tulips":
    petal_color = "purple"
elif flower in "lilies":
    petal_color = "purple"




def draw_circle(radius, color):
    painter = trtl.Turtle()
    painter.fillcolor(color)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()

def petal(x, y, num_petals, petal_color):
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

def draw_flower(set_x, set_y, num_petals, petal_color):
    painter = trtl.Turtle()
    x,y=painter.pos()

    x += set_x
    y += set_y

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

    #middle part
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
for n in range(int(numberOfFlowers)):
    draw_flower(x, y, int(numberOfPetals), petal_color)  
    x += 200  
    

wn = trtl.Screen()
wn.mainloop()
