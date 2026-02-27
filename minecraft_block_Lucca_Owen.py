#Import random module and turtle
import random
import turtle as trtl
#set speed and start loop
block = trtl.Turtle()
block.speed(1)
repeat = "yes"
#function to adjust speed based on size of cube
def speedfix():
    if size > 350:
        block.speed(0)
    elif size > 300:
        block.speed(6)
    elif size > 250:
        block.speed(5)
    elif size > 200:
        block.speed(4)
    elif size > 150:
        block.speed(3)
    elif size > 100:
        block.speed(2)
    elif size < 50:
        block.speed(1)


#function to randomize size
def randsizefn():
    global size
    size = random.randint(30, 300)
#function to draw it
def drawfn():
    global size
    speedfix()
    block.fillcolor(grasscolor)
    block.begin_fill()
    block.penup()
    blockstart = (-1 * size)
    angles = [150, 30, -30, -150]
    block.begin_fill()
    block.pendown()
    for angle in angles:
        block.setheading(angle)
        block.forward(size)
    block.end_fill()
    block.penup()
    block.setheading(150)
    block.forward(size)
    block.pendown()
    block.setheading(-120)
    block.fillcolor(dirtcolor)
    block.begin_fill()
    block.circle(size, 240, 4)
    block.goto(0,0)
    block.setheading(150)
    block.forward(size)
    block.end_fill()
    block.goto(0,0)
    block.goto(0,blockstart)
    block.penup()
    block.goto(0,0)
    block.pendown()
#function for random colors
def randcolorfn():
    global grasscolor, dirtcolor
    grasscolor = random.choice(turtle_colors)
    dirtcolor = random.choice(turtle_colors)
    block.clear()
#function for user to input size  
def usersize():
    global size
    size = int(input("What size would you like it to be? [30-300] "))
#function for user to input color choices
def usercolors():
    global grasscolor, dirtcolor
    grasscolor = input("What color do you want the GRASS to be? Use valid python turtle color ")
    dirtcolor = input("What color do you want the DIRT to be? Use valid python turtle color ")
    

#set list of possible turtle colors
turtle_colors = [
    "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen",
    "antique white", "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white",
    "moccasin", "cornsilk", "ivory", "lemon chiffon", "seashell", "honeydew", "mint cream",
    "azure", "alice blue", "lavender", "lavender blush", "misty rose", "white",
    "black", "dark slate gray", "dim gray", "slate gray", "light slate gray", "gray",
    "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue", "slate blue",
    "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue", "dodger blue",
    "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue",
    "light blue", "powder blue", "pale turquoise", "dark turquoise", "medium turquoise",
    "turquoise", "cyan", "light cyan", "cadet blue", "medium aquamarine", "aquamarine",
    "dark green", "dark olive green", "dark sea green", "sea green", "medium sea green",
    "light sea green", "pale green", "spring green", "lawn green", "medium spring green",
    "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki",
    "khaki", "pale goldenrod", "light goldenrod yellow", "light yellow", "yellow", "gold",
    "light goldenrod", "goldenrod", "dark goldenrod", "rosy brown", "indian red",
    "saddle brown", "sienna", "peru", "burlywood", "beige", "wheat", "sandy brown",
    "tan", "chocolate", "firebrick", "brown", "dark salmon", "salmon", "light salmon",
    "orange", "dark orange", "coral", "light coral", "tomato", "orange red", "red", "hot pink",
    "deep pink", "pink", "light pink", "pale violet red", "maroon", "medium violet red",
    "violet red", "magenta", "violet", "plum", "orchid", "medium orchid", "dark orchid",
    "dark violet", "blue violet", "purple", "medium purple", "thistle"
]

#set up the loops
if repeat == "yes":
#keep it looping
    while repeat == "yes":
#Ask for random input
        randomsize = input("Would you like a random size? [yes/no] ")
        randomcolor = input("Would you like random colors? [yes/no] ")
#Account for all possible answers
        if randomsize == "yes" and repeat == "yes" and randomcolor == "no":
            block.clear()
            size = random.randint(30, 300)
#Ask the user for color choices
            usercolors()
            drawfn()
#Ask if they want to go again
            repeat = input("Wanna do it again? [yes/no] ")
        elif randomsize == "no" and repeat == "yes" and randomcolor == "no":
            block.clear()
            usersize()
            usercolors()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
        elif randomcolor == "yes" and randomsize == "yes" and repeat == "yes":
            randcolorfn()
            randsizefn()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
        elif randomcolor == "yes" and randomsize == "no" and repeat == "yes":
#Iterate through the list of possible colors
            randcolorfn()
            usersize()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
#If you don't want to, compliments user
        if repeat == "no":
            print("Have a nice day!")
#To prevent from going to else:
        if repeat == "yes":
            print("Let's go!")
#Invalid ansers get rejected
        else:
            print("Something went wrong. Try again.")
wn = block.screen
wn.mainloop()