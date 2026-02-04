#   a123_apple_1.py
import turtle as trtl
import random
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
apple = trtl.Turtle()
pear = trtl.Turtle()
apple2 = trtl.Turtle()
pear2 = trtl.Turtle()
drawer = trtl.Turtle()
wn.bgpic("background.gif")
drawer.hideturtle()
drawer.penup()
drawer.color("blue")
drawer.goto(-100,200)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
global unbind
unbind = False
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def move():
  global active_apple
  global randomLetter
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  active_apple.goto(xcor-random.randint(-150,300),ycor-random.randint(-150,200))
  wn.onkeypress(lambda l=randomLetter: move(l), randomLetter)
  onpress()
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()
def onpress():
  if len(letters) == 0:
    drawer.clear()
    drawer.goto(-125, 200)
    drawer.write("You win!", font=("Arial", 50, "bold"))
    return
  global randomLetter
  drawer.clear()
  randomLetterChoice = random.randint(0,len(letters)-1)
  randomLetter = letters[randomLetterChoice]
  choices = [apple, apple2, pear, pear2]
  global active_apple
  randomChoice = random.randint(0, 3)
  active_apple = choices[randomChoice]
  active_apple.penup()  
  
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  if ycor < -150 or ycor > 150:
    active_apple.goto(random.randint(-250, 250), random.randint(-150, 150))
  if xcor < -250 or xcor > 250:
    active_apple.goto(random.randint(-250, 250), random.randint(-150, 150))
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  drawer.goto(xcor-20,ycor-30)
  drawer.write(randomLetter, font=("Arial", 50, "bold"))
  letters.pop(randomLetterChoice)

  wn.onkeypress(move, randomLetter)
#-----function calls-----
draw_apple(apple)
draw_pear(pear)
draw_pear(pear2)
draw_apple(apple2)
wn.listen()
onpress()
wn.mainloop()