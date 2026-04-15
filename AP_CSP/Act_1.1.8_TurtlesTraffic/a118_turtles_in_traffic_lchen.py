# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)   
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
collision = False
while collision == False:
  for vt in vert_turtles:
    vt.forward(2)
    xcor = vt.xcor()
    ycor = vt.ycor()
    if ((abs(ht.ycor() - vt.ycor()) < 16) or (abs(ht.xcor() - vt.xcor()) < 6)) and ht.xcor() < -20:
      vt.speed(2)
      vt.backward(3)
      vt.backward(3)
      vt.backward(3)
      vt.backward(2)
      vt.speed(0)
    else:
      vt.forward(2)
  for ht in horiz_turtles:
    ht.forward(2)
wn = trtl.Screen()
wn.mainloop()