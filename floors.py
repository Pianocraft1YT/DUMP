#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  y = y + 5 # location of next floor
  if floor % 3 == 1:
    painter.color("red")
  elif floor % 3 == 2:
    painter.color("orange")
  else:
    painter.color("yellow")
  #draw the floor
  painter.pendown()
  painter.forward(50)

x = 0
y = -150
for floor in range(num_floors):
  painter.penup()
  painter.goto(x, y)
  painter.color("blue")
  y = y + 5
  if floor % 3 ==1:
    painter.color("green")
  elif floor % 3 ==2:
    painter.color("blue")
  else:
    painter.color("purple")
  painter.pendown()
  painter.forward(50)
  
x = 75
y = -150
for floor in range(num_floors):
  painter.penup()
  painter.goto(x, y)
  painter.color("orange")
  y = y + 5
  if floor % 3 ==1:
    painter.color("pink")
  elif floor % 3 ==2:
    painter.color("black")
  else:
    painter.color("teal")
  painter.pendown()
  painter.forward(50)
wn = trtl.Screen()
wn.mainloop()