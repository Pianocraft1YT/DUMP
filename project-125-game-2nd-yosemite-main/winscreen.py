import turtle
import random as rand

def winFunction():
    colors = ["red","green","blue","pink","purple","salmon","yellow","black","orange","cyan","magenta"]

    Winor = turtle.Turtle()
    Winor.hideturtle()
    Winor.shapesize(500)
    
    # backround
    wn = turtle.Screen()
    wn.bgcolor('black')# backround color
    wn.tracer(0)
    num = 0
    def flash():
        randomColor = rand.randint(0, 10)
        wn.bgcolor(colors[randomColor])
        wn.ontimer(flash, 100)
    # first drawing Turtle fuction
    Turtle1 = turtle.Turtle()
    Turtle1.speed(0)
    Turtle1.color('navy')# pen color
    Turtle1.hideturtle()
    rotate=int(360)
    def drawCircles(t,size):# definition
    # circle size
        for i in range(90):
            t.circle(size)
            size=size-90
    def drawSpecial(t,size,repeat):# definition
    # second turtle drawing function
        for i in range(repeat):
            drawCircles(t,size)
            t.right(360/repeat)
    drawSpecial(Turtle1,100,10)
    Turtle2 = turtle.Turtle()
    Turtle2.speed(0)
    Turtle2.hideturtle()
    Turtle2.color('white')# pen color
    rotate=int(90)
    def drawCircles(t,size):# definition
    # second circle size
        for i in range(10):
            t.circle(size)
            size=size-10
    def drawSpecial(t,size,repeat):# definition
    # third turtle function
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
    drawSpecial(Turtle2,200,20)
    Turtle3 = turtle.Turtle()
    Turtle3.hideturtle()
    Turtle3.speed(0)
    Turtle3.color('darkblue')# pen color
    rotate=int(80)
    def drawCircles(t,size):# definition
        for i in range(4):
            t.circle(size)
            size=size-5
    def drawSpecial(t,size,repeat):# definition
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
    wn.addshape("Frogdance2.gif")
    wn.addshape("Frogdance1.gif")
    Win_Loop = 0
    while Win_Loop < 1000:
        wn.update()
        Winor.shape("Frogdance2.gif")
        Winor.showturtle()
        wn.update()
        Winor.shape("Frogdance1.gif")
        wn.update()
        Win_Loop += 1
        wn.ontimer(flash, 50)


          






