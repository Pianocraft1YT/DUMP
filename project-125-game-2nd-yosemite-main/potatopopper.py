#Put actual code here because we need a python file
#----------Import---------
#place to import turtle and rand and such
import turtle as trtl
import random as rand
import winscreen as win1
#----------Variables------
mainpotatoimage1 = "mainpotatoimage14.gif" 
mainpotatoimage2 = "mainpotatoimage1.gif"
mainpotatoimage3 = "mainpotatoimage2.gif"
mainpotatoimage4 = "mainpotatoimage3.gif"
mainpotatoimage5 = "mainpotatoimage4.gif"
mainpotatoimage6 = "mainpotatoimage5.gif"
mainpotatoimage7 = "mainpotatoimage6.gif"
mainpotatoimage8 = "mainpotatoimage7.gif"
mainpotatoimage9 = "mainpotatoimage8.gif"
mainpotatoimage10 = "mainpotatoimage9.gif"
mainpotatoimage11 = "mainpotatoimage10.gif"
mainpotatoimage12 = "mainpotatoimage11.gif"
mainpotatoimage13 = "mainpotatoimage12.gif"
mainpotatoimage14 = "mainpotatoimage13.gif"

goldenpotatoimage1 = "goldenpotatoimage1.gif"
goldenpotatoimage2 = "goldenpotatoimage2.gif"
mainpotatoimage_list = [mainpotatoimage1, mainpotatoimage2, mainpotatoimage3, mainpotatoimage4, mainpotatoimage5, mainpotatoimage6, mainpotatoimage7, mainpotatoimage8, mainpotatoimage9, mainpotatoimage10, mainpotatoimage11, mainpotatoimage12, mainpotatoimage13, mainpotatoimage14]
goldenpotatoimage_list = [goldenpotatoimage1, goldenpotatoimage2]
FrogD = "Frogdance1.gif"
FrodD2 = "Frogdance2.gif"
milestone1 = 100
milestone2 = 1000
milestone3 = 10000
milestone4 = 25000
win = 100000
Total_potato_count = 0
Current_potato_modifer = 1
currentMilestone = milestone1
clickCount = 0
loop = False
boost = 0
randx = 0
randy = 0
#----------Screen Init----------
wn = trtl.Screen()
wn.bgcolor("black")
wn.addshape(mainpotatoimage1)
wn.tracer(0)
#----------Turtle Init----------
#turtle setup
Potato_main = trtl.Turtle()
Potato_main.shape(mainpotatoimage1)
Potato_main.penup()

Potato_count_writer = trtl.Turtle()
Potato_count_writer.hideturtle()
Potato_count_writer.penup()
Potato_count_writer.color("orange")
Potato_count_writer.goto(0, -250)
Potato_count_writer.hideturtle()

Potato_status_writer = trtl.Turtle()
Potato_status_writer.color("orange")
Potato_status_writer.penup()
Potato_status_writer.goto(0, 200)
Potato_status_writer.hideturtle()

Potato_nextupgrade_writer = trtl.Turtle()
Potato_nextupgrade_writer.penup()
Potato_nextupgrade_writer.color("orange")
Potato_nextupgrade_writer.goto(0, -300)
Potato_nextupgrade_writer.hideturtle()

Potato_welcome_writer = trtl.Turtle()
Potato_welcome_writer.penup()
Potato_welcome_writer.color("orange")
Potato_welcome_writer.hideturtle()
Potato_welcome_writer.goto(0, 165)

Potato_golden = trtl.Turtle()
Potato_golden.penup()
Potato_golden.hideturtle()
Potato_golden.color("orange")

Potato_nextboost_writer = trtl.Turtle()
Potato_nextboost_writer.penup()
Potato_nextboost_writer.color("orange")
Potato_nextboost_writer.hideturtle()
Potato_nextboost_writer.goto(0, 260)

Potato_point_tag_writer = trtl.Turtle()
Potato_point_tag_writer.penup()
Potato_point_tag_writer.color("orange")
Potato_point_tag_writer.hideturtle()

Winor = trtl.Turtle()
Winor.hideturtle()
You_win1 = False
#----------Functions------------
# #make def statements
def Write_potatoes():
    global You_win1
    global Total_potato_count
    if loop == True:
        Potato_count_writer.clear()
        Potato_count_writer.write("You have " + str(Total_potato_count) + " potatoes.", False, "center", ("Arial", 30, "normal"))
        if You_win1 == False:
            if Total_potato_count >= 25000:
                Potato_nextupgrade_writer.write("You need " + str((currentMilestone - Total_potato_count)) + " more potatoes to WIN!", False, "center", ("Arial", 30, "normal"))
            else:
                Potato_nextupgrade_writer.write("You need " + str((currentMilestone - Total_potato_count)) + " more potatoes for the next upgrade.", False, "center", ("Arial", 30, "normal"))
def On_potato_click(x,y):
    #based off of catch a turtle
    Potato_status_writer.clear()
    Potato_nextboost_writer.clear()
    Potato_welcome_writer.clear()
    global Current_potato_modifer
    global Total_potato_count
    global mainpotatoimage_list
    global currentMilestone
    global clickCount
    global boost
    global You_win1
    global loop
    Potato_nextupgrade_writer.clear()
    clickCount +=1
    if clickCount % 100 == 0:
        Spawn_golden_potato()
    else:
        Potato_golden.clear()
    if Total_potato_count >= 100000:
        loop = False
        You_win1 = True
        Potato_golden.hideturtle()
        Potato_main.hideturtle()
        Potato_count_writer.clear()
        Potato_nextboost_writer.clear()
        Potato_nextupgrade_writer.clear()
        Potato_status_writer.clear()
        Potato_status_writer.hideturtle()
        Potato_welcome_writer.clear()
        Potato_main.clear()
        Potato_main.hideturtle()
        Potato_count_writer.clear()
        Potato_count_writer.hideturtle()
        Potato_welcome_writer.pendown()
        Potato_welcome_writer.pensize(1000000)
        Potato_welcome_writer.color("White")
        Potato_welcome_writer.hideturtle()
        wn.clear()
        wn.tracer(0)
        wn.bgcolor("black")
        wn.update()
        win1.winFunction()
    elif Total_potato_count >= 25000:
        loop = True
        Current_potato_modifer = 100
        currentMilestone = win
        Potato_status_writer.clear()
        Potato_status_writer.write("Gaining " + str(Current_potato_modifer) + " potatoes a click!", False, "center",("Arial", 30, "normal"))
        Potato_nextboost_writer.clear()
        Potato_nextboost_writer.write("Gaining " + str(boost) + " potatoes/sec", False, "center", ("Times", 30, "normal"))
    elif Total_potato_count >= 10000:
        loop = True
        Current_potato_modifer = 50
        currentMilestone = milestone4
        Potato_status_writer.clear()
        Potato_status_writer.write("Gaining " + str(Current_potato_modifer) + " potatoes a click!", False, "center",("Arial", 30, "normal"))
        Potato_nextboost_writer.clear()
        Potato_nextboost_writer.write("Gaining " + str(boost) + " potatoes/sec", False, "center", ("Times", 30, "normal"))
    elif Total_potato_count >= 1000:
        loop = True
        Current_potato_modifer = 10
        currentMilestone = milestone3
        Potato_status_writer.clear()
        Potato_nextboost_writer.clear()
        Potato_nextboost_writer.write("Gaining " + str(boost) + " potatoes/sec", False, "center", ("Times", 30, "normal"))
        Potato_status_writer.write("Gaining " + str(Current_potato_modifer) + " potatoes a click!", False, "center",("Arial", 30, "normal"))
    elif Total_potato_count >= 100:
        loop = True
        Current_potato_modifer = 2
        currentMilestone = milestone2
        Potato_status_writer.clear()
        Potato_status_writer.write("Gaining " + str(Current_potato_modifer) + " potatoes a click!", False, "center",("Arial", 30, "normal"))
        Potato_nextboost_writer.clear()
        Potato_nextboost_writer.write("Gaining " + str(boost) + " potatoes/sec", False, "center", ("Times", 30, "normal"))
    elif Total_potato_count < 100:
        loop = True
        currentMilestone = milestone1
        Potato_status_writer.write("Click the potato!", False, "center", ("Arial", 30, "normal"))
        Current_potato_modifer = 1
        Potato_nextboost_writer.write("Gaining " + str(boost) + " potatoes/sec", False, "center", ("Times", 30, "normal"))
        
    Total_potato_count = Total_potato_count + Current_potato_modifer
    Write_potatoes()
    mainpotatoimage_random = rand.randint(0,13)
    Current_mainpotato_photo = mainpotatoimage_list[mainpotatoimage_random]
    wn.addshape(Current_mainpotato_photo)
    Potato_main.shape(Current_mainpotato_photo)
    wn.update()
def welcome():
    global loop
    Potato_main.onclick(On_potato_click)
    loop = True
    Potato_welcome_writer.clear()
    potato_boost()
    update_potato_display()
def Spawn_golden_potato():
    global goldenpotatorandom
    global Current_goldenpotato_photo
    goldenpotatorandom = rand.randint(0,1)
    Current_goldenpotato_photo = goldenpotatoimage_list[goldenpotatorandom]
    wn.addshape(Current_goldenpotato_photo)
    Potato_golden.shape(Current_goldenpotato_photo)
    Potato_golden.goto(rand.randint(-250,250), rand.randint(-200,130))
    Potato_golden.showturtle()
    Potato_golden.onclick(golden_potato_bonus)
    wn.update()
def golden_potato_bonus(x,y):
    global Total_potato_count
    bonus = Current_potato_modifer * rand.randint(2,15)
    Total_potato_count += bonus
    Potato_golden.write("+" + str(bonus) + " potatoes!", False, "center", ("Arial", 25, "bold"))
    Potato_golden.hideturtle()
    wn.update()
def potato_boost():
    global loop
    global Total_potato_count
    global currentMilestone
    global boost
    if loop == True:
        if currentMilestone == milestone2:
            boost = 1
            Total_potato_count+=1
            wn.update()
        elif currentMilestone == milestone3:
            boost = 7
            Total_potato_count+=7
            wn.update()
        elif currentMilestone == milestone4:
            boost = 28
            Total_potato_count+=28
            wn.update()
        elif currentMilestone == win:
            boost = 43
            Total_potato_count+=43
            wn.update()
        else:
            boost = 0
            Total_potato_count+=0
            wn.update()
        Potato_nextupgrade_writer.clear()
        Write_potatoes()
        wn.ontimer(potato_boost, 1000)

def update_potato_display():
    global loop
    if loop == True:
        Potato_nextupgrade_writer.clear()
        Write_potatoes()
        get_random_position()
        
def clear_tag_text():
    Potato_point_tag_writer.clear()

def get_random_xcor():
    global randx
    valid = False
    while not valid:
        randx = rand.randint(-300, 300)
        if -75 < randx < 75:
            valid = False
        else:
            valid = True

def get_random_ycor():
    global randy
    valid = False
    while not valid:
        randy = rand.randint(-200, 150)
        if -75 < randy < 55:
            valid = False
        else:
            valid = True

def get_random_position():
    if loop:
        if boost != 0:
            global randx, randy
            get_random_xcor()
            get_random_ycor()
            Potato_point_tag_writer.goto(randx, randy)
            Potato_point_tag_writer.write("+" + str(boost), False, "center", ("Arial", 20, "normal"))
            wn.ontimer(clear_tag_text, 1000)
    wn.ontimer(get_random_position, 1000)

def You_Win():
    win1.winFunction()
    
def Cheat():
    global Total_potato_count
    Total_potato_count += 33300
#----------Execution------

Potato_welcome_writer.write("Welcome to Potato Popper! \nIn this game, you click potato. That's it. \nFor now, you win at 100k potatoes!\nPress SPACE to start, then CLICK!\nHave fun!", False, "center", ("Times", 30, "normal"))
#execute actual code
wn.onkeypress(Cheat, "G")
wn.onkeypress(welcome, "space")
wn.listen()
wn.update()
wn.mainloop()