import turtle as trtl
import random
import leaderboard as lb
leaderboard_file_name = "leaderboard.txt"
player_name = input("What is your name?")
spot = trtl.Turtle()
spot.shape("circle")
spot.shapesize(1)
spot.fillcolor("cyan")
loop = "true"
wn = trtl.Screen() 
scorewriter = trtl.Turtle()
font_default = ("Arial", 20, "normal")
scorewriter.speed(0)
scorewriter.penup()
scorewriter.goto(200, 300)
scorewriter.hideturtle()
wn.bgcolor("orange")
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
turtle_colors = [
    "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen",
    "antique white", "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white",
    "moccasin", "cornsilk", "ivory", "lemon chiffon", "seashell", "honeydew", "mint cream",
    "azure", "alice blue", "lavender", "lavender blush", "misty rose", "white",
    "black", "dark slate gray", "dim gray", "slate gray", "light slate gray", "gray",
    "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue", "slate blue",
    "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue", "dodger blue",
    "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue",
    "light blue", "powder blue", "pale turquoise", "dark turquoise", "medium turquoise",
    "turquoise", "cyan", "light cyan", "cadet blue", "medium aquamarine", "aquamarine",
    "dark green", "dark olive green", "dark sea green", "sea green", "medium sea green",
    "light sea green", "pale green", "spring green", "lawn green", "medium spring green",
    "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki",
    "khaki", "pale goldenrod", "light goldenrod yellow", "light yellow", "yellow", "gold",
    "light goldenrod", "goldenrod", "dark goldenrod", "rosy brown", "indian red",
    "saddle brown", "sienna", "peru", "burlywood", "beige", "wheat", "sandy brown",
    "tan", "chocolate", "firebrick", "brown", "dark salmon", "salmon", "light salmon",
    "orange", "dark orange", "coral", "light coral", "tomato", "orange red", "red", "hot pink",
    "deep pink", "pink", "light pink", "pale violet red", "maroon", "medium violet red",
    "violet red", "magenta", "violet", "plum", "orchid", "medium orchid", "dark orchid",
    "dark violet", "blue violet", "purple", "medium purple", "thistle"
]
basic_sizes = [ 1, 2, 3 ,0.75, 4
]

#-----countdown writer-----
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-200, 300)
#-----game functions-----
# CODE TO ADD
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= int(leader_scores_list[4])):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up! Thanks for playing.", font=font_default)
    timer_up = True
    spot.hideturtle()
    manage_leaderboard()
  else:

    counter.write("Timer: " + str(timer), font=font_default)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def xy(x, y):
    if timer_up == False:
        global score
        randomX = random.randint(-300, 300)
        randomY = random.randint(-200, 300)
        spot.penup()
        spot.speed(0)
        spot.hideturtle()
        global colorstime 
        colorstime = random.choice(turtle_colors)
        spot.fillcolor(colorstime)
        global randomsize
        randomsize = random.choice(basic_sizes)
        spot.shapesize(randomsize)
        spot.showturtle()
        spot.goto(randomX, randomY)
        score += 1
        scorewriter.clear()
        scorewriter.write(score, font=font_default)
        

    else:
       spot.hideturtle()
       
spot.onclick(xy)
wn.ontimer(countdown, counter_interval)

wn.mainloop()
