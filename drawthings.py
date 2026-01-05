import turtle as trtl

color1 = "orange"
color2 = "purple"
color3 = "blue"
wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color3)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1
  angle = int(input("angle: (If unsure, I like 120, 45, and 220)"))
  seg = int(360/angle)
# CODE TO ADD
  while painter.ycor() < height: 
    if space % 300 == 0:
      painter.color(color3)
      painter.pencolor(color3)
    elif space % 3 == 1:
      painter.color(color2)
      painter.pencolor(color2)
    elif space % 3 == 2:
      painter.color("green")
      painter.pencolor("green")
    else:
      painter.color(color1)
      painter.pencolor(color1)
    painter.right(angle) 
    painter.forward(2 * space + 10) # experiment 
    painter.begin_fill() 
    painter.circle(3) 
    painter.end_fill() 
    space = space + 1
  answer = input("again? y/n ")




wn.bye()
