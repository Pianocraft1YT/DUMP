# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
import random
# create an empty list of turtles
my_turtles = []
screen = trtl.Screen()
screen.register_shape("piano.gif")
screen.register_shape("anchor.gif")
screen.register_shape("bird.gif")
screen.register_shape("dog.gif")
screen.register_shape("joker.gif")
screen.register_shape("minecraft.gif")
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "minecraft.gif", "piano.gif", "anchor.gif", "bird.gif", "dog.gif", "joker.gif"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "yellow", "pink", "cyan", "gray", "magenta", "violet", "black"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#reset starting values
direction = 76
c= "true" 
startx = random.randint(-10, 10) +  random.randint(1, 100)
starty = random.randint(-10,10) + random.randint(1, 100)
#turns to make the lines
for t in my_turtles:
  t.pendown()
  newdirection = random.randint(1, 360) * 1.4
  t.setheading(newdirection)
  t.right(45)     
  t.forward(50)
  c="true"
  startx = startx + t.xcor()
  starty = starty + t.ycor()
  t.goto(startx, starty)
  while c == "true":
    popcolor = turtle_colors.pop()
    turtle_colors = turtle_colors.copy()
    print(popcolor)
    c= "false"
  t.color(popcolor)
wn = trtl.Screen()
wn.mainloop()