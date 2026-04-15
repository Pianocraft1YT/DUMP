# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

# ask user for a color (such as red, green, blue, pink, purple)
pencolor2 = input("What Color u want? ")

# ask user for the radius of a circle
meow = int(input("What radius u want? (in numbers, like 12) "))
pensize = int(input("How big would your pen be?"))
time = int(input("how long do you want this to take? (numbers)"))
# draw a circle with the radius and line color entered by the user
painter.color(pencolor2)
painter.pensize(pensize)
painter.circle(meow, 360, time)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()