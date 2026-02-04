# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name spider is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
loop = 4
forward = 100
angle = 180 / loop
spider.pensize(5)
counter = 0
while (counter < loop):
  spider.goto(0,15)
  spider.setheading(25*counter)
  spider.forward(forward)
  counter = counter + 1
for i in range(4):
  spider.penup()
  spider.goto(0,10)
  spider.pendown()
  spider.setheading(-25*i-75)
  spider.forward(forward)
  counter = counter + 1
  i = i + 1

spider.penup()
spider.goto(-20, 30)
spider.pendown()
spider.pencolor("red")
spider.circle(10)
spider.penup()
spider.goto(13,30)
spider.pendown()
spider.circle(10)
spider.penup()

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
