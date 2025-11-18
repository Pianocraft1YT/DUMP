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
    ht.speed(0)  # Set to fastest speed

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)
    vt.speed(0)  # Set to fastest speed
    
    tloc += 50

# Move turtles across and down screen, stopping for collisions
step_size = 5
collision_distance = 20

# Keep track of which turtles are still moving
active_horiz = [True] * len(horiz_turtles)
active_vert = [True] * len(vert_turtles)

# Move turtles one after another
for step in range(100):
    for i in range(len(horiz_turtles)):
        # Move horizontal turtle if it's still active
        if active_horiz[i]:
            horiz_turtles[i].forward(step_size)
            
            # Check for collisions with all vertical turtles
            for j in range(len(vert_turtles)):
                if active_vert[j] and horiz_turtles[i].distance(vert_turtles[j]) < collision_distance:
                    active_horiz[i] = False
                    active_vert[j] = False
                    break
        
        # Move vertical turtle if it's still active
        if active_vert[i]:
            vert_turtles[i].forward(step_size)
            
            # Check for collisions with all horizontal turtles
            for j in range(len(horiz_turtles)):
                if active_horiz[j] and vert_turtles[i].distance(horiz_turtles[j]) < collision_distance:
                    active_vert[i] = False
                    active_horiz[j] = False
                    break

wn = trtl.Screen()
wn.mainloop()