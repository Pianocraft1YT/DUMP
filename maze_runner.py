################################################################################
#   a124TR_mazerunner2_move_runner.py
#   Example solution: 
#      The maze runner can now move about the maze.
################################################################################
import turtle as trtl
import random as rand

# maze configuration variables
amount = 20
num_sides = 23
path_width = 25 
wall_color = "blue"
stopped = False
wn = trtl.Screen()
maze_runner = trtl.Turtle()
def draw_door(pos):
  maze_drawer.forward(pos)
  maze_drawer.penup()
  maze_drawer.forward(path_width*2)
  maze_drawer.pendown()

def draw_barrier(pos):
  maze_drawer.forward(pos)
  maze_drawer.left(90)
  maze_drawer.forward(path_width*2)
  maze_drawer.backward(path_width*2)
  maze_drawer.right(90)

def move_runner():
  #TODO: Only move forward if 'stopped' is false
  global stopped
  if stopped == False:
    maze_runner.forward(amount) 
    #Assumes you named this turtle variable maze_runner!
  #TODO: replace the hard-coded value for forward() with a variable, which you set at the top of this file
  
  ############################################################################################
  # The rest of this code takes care of detecting maze_runner turtle "collision" with a wall
  #  Might be useful for you in creating your own game in the future ;)
  ############################################################################################
  wn_canvas = wn.getcanvas()
  x,y  = maze_runner.position() #Assumes you named this turtle variable maze_runner!
  margin = 8
  
  # find_overlappting defines a rectangle returns a list of items drawn within that rectangle
  # Why -y?  Old coordinate system approach where top left corner is origin...Just ignore that for now ;)
  items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)
  
  if (len(items) > 0): # >2 items overlappig
    # get the fill color of the base object - the canvas
    canvas_color = wn_canvas.itemcget(items[0], "fill")
    
    #if the canvas is currently the wall color, the turtle has "collided"
    #TODO: Replace 'False in the 2 'or' statements:  Check if the turtle's position is too close to top, bottom, or sides
    if (canvas_color == wall_color) or (abs(maze_runner.xcor()) > (wn.window_width()/2)) or (abs(maze_runner.ycor()) > (wn.window_height()/2)):
      maze_runner.fillcolor("gray") #Assume you named this turtle variable maze_runner!
      stopped = True
      reset_runner()
      return
      
  #################################################################################################
   
  # automatically move the runner
  wn.ontimer(move_runner, 500) # Every X ms, move_runner again
def reset_runner():
  global stopped
  stopped = False
  maze_runner.fillcolor("green")
  maze_runner.clear()
  maze_runner.penup()
  maze_runner.goto(-50, 0)
  maze_runner.pendown()
def reset_maze_runner():
    global stopped
    stopped = False
    #TODO: set stopped to False
    
    #TODO: set maze_runner green again
    maze_runner.fillcolor("green")

# event handlers for changing direction
def go_up():
  maze_runner.setheading(90) #Assumes you named this turtle variable maze_runner!
  reset_maze_runner()
  
#TODO: implement the other 3 directions (one function each)
def go_down():
  maze_runner.setheading(-90)
  reset_maze_runner
def go_left():
  maze_runner.setheading(180)
  reset_maze_runner
def go_right():
  maze_runner.setheading(0)
  reset_maze_runner

# config the maze
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
#TODO: (Step 25) set maze_drawer turtle speed to top speed 
maze_drawer.speed(0)
maze_drawer.penup()
maze_drawer.goto(path_width*2, -path_width*2)
maze_drawer.pendown()

# config the maze runner
#TODO: create a maze runner turtle, assigned to variable name maze_runner
#On the top of the thing
#TODO: Set color of the maze_runner turtle
maze_runner.fillcolor("orange")
#TODO: Start maze_runner near the center, but not on top of a wall. Don't draw the movement to get there
# Hints: Use the goto() turtle method and your path_width variable. Experiment with multipliers of it, including both positive and negative values.
#       Also, see the maze_drawer part above
maze_runner.penup()
maze_runner.goto(-50, 0)
maze_runner.pendown()

# draw maze from the middle out
wall_len = path_width
for w in range(num_sides): 
  wall_len += path_width

  if (w > 4): 
    maze_drawer.left(90)

    # randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))
    # if a door and barrier would be rendered on top of each other, get a new value
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wall_len - path_width*2))

    if (door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - barrier)
    else: 
      draw_barrier(barrier)
      draw_door(door - barrier)
      # draw the rest of the wall
      maze_drawer.forward(wall_len - door - path_width*2)

maze_drawer.hideturtle()

# listen for events
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
#TODO: Add onkeypress event listers for each of the other arrow keys: Down, Left, Right

#TODO: Add onkeypress event listener for a key of your choice (e.g. 'g') which calls the move_runner function
wn.onkeypress(move_runner, "g")
wn.listen()
wn.mainloop()