# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
    """Return list of leader names (strings) from leaderboard file."""
    names = []
    try:
        with open(file_name, "r") as leaderboard_file:
            for line in leaderboard_file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 1)
                names.append(parts[0])
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        return []
    return names


# return scores from the leaderboard file
def get_scores(file_name):
    """Return list of leader scores (strings) from leaderboard file."""
    scores = []
    try:
        with open(file_name, "r") as leaderboard_file:
            for line in leaderboard_file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 1)
                if len(parts) > 1:
                    scores.append(parts[1])
    except FileNotFoundError:
        return []
    return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    """
    Insert player_name and player_score into leader_names and leader_scores lists
    at the correct position (descending by score). Keep top 5 only, and write back to file.
    leader_scores is expected to be a list of score strings; player_score may be int.
    """
    # Ensure scores are comparable: convert existing scores to ints for comparison only
    inserted = False
    try:
        pscore_int = int(player_score)
    except Exception:
        # If player_score isn't an int-like, treat as 0
        pscore_int = 0

    # If there are no existing entries, just append
    if not leader_scores:
        leader_names.append(player_name)
        leader_scores.append(str(pscore_int))
        inserted = True
    else:
        for idx, s in enumerate(leader_scores):
            try:
                existing = int(s)
            except Exception:
                existing = 0
            # Insert when player's score is >= existing (so equal scores place above)
            if pscore_int >= existing:
                leader_names.insert(idx, player_name)
                leader_scores.insert(idx, str(pscore_int))
                inserted = True
                break

    # If we didn't insert and there is still space (<5), append at end
    if not inserted and len(leader_names) < 5:
        leader_names.append(player_name)
        leader_scores.append(str(pscore_int))
        inserted = True

    # Keep only top 5
    if len(leader_names) > 5:
        leader_names[:] = leader_names[:5]
        leader_scores[:] = leader_scores[:5]

    # Write back to the file (overwrite)
    with open(file_name, "w") as leaderboard_file:
        for i in range(len(leader_names)):
            leaderboard_file.write(f"{leader_names[i]},{leader_scores[i]}\n")


# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    """
    Draws the leaderboard using turtle_object.
    high_scorer: boolean indicating whether the current player was written into leaderboard already.
    leader_names / leader_scores: lists (parallel).
    player_score: int
    """
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()

    # Display the leaderboard entries
    for index in range(len(leader_names)):
        turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
        turtle_object.down()

    # Move to next line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # Message about making the leaderboard
    if high_scorer:
        turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
    else:
        turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)

    # Move to next line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # Medal message: only show a medal message if earned (otherwise show nothing)
    try:
        pscore_int = int(player_score)
    except Exception:
        pscore_int = 0

    if pscore_int >= gold_score:
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif pscore_int >= silver_score:
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif pscore_int >= bronze_score:
        turtle_object.write("You earned a bronze medal!", font=font_setup)
    # else: show nothing (per instructions)
