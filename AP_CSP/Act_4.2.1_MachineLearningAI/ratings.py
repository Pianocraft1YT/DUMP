#   a421_one_movie_recommender.py
#   A basic movie recommendation code using average for a single user and single movie.
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   It was written by Nikhil22.
#   The code has been modified from its original version.
import numpy as np 

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Trolls", "Black Panther"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]

# TODO 1: changed these values to the names of the students in your group
users = ["Aaron", "Josh", "Avery", "Kareena", "Owen", "Lucca"]

# TODO 2: paste your ratings tables here
# Ratings from the "Movie Ratings" sheet, rows = movies (order as above), columns = users (order as above)
movie_ratings = [
    [8.0, 8.8, 9.1, 9.0, 8.0, 5.0],  # Back to the Future
    [7.0, 7.3, 0.0, 0.0, 9.0, 4.0],  # Guardians of the Galaxy
    [5.0, 10.0, 0.0, 7.0, 4.0, 1.0], # Avatar
    [0.0, 2.1, 5.2, 0.0, 1.0, 0.0],  # Trolls
    [6.0, 7.6, 0.0, 0.0, 0.0, 1.0]   # Black Panther
]

# User preferences from "User Preferences" sheet, rows = users (order as above),
# columns in order of genres list: Action, Adventure, Science Fiction, Comedy
user_preferences = [
    [5.0, 3.0, 5.0, 3.0],  # Aaron
    [3.7, 4.5, 5.0, 3.4],  # Josh
    [4.1, 3.4, 4.5, 4.9],  # Avery
    [3.0, 4.0, 5.0, 4.0],  # Kareena
    [2.5, 3.0, 4.5, 4.5],  # Owen
    [4.0, 5.0, 5.0, 3.0]   # Lucca
]

# Genre profile for each movie (binary: 1 if the movie belongs to the genre, else 0)
# Order of genres: Action, Adventure, Science Fiction, Comedy
movie_genre =  [[0.6, 0.0, 0.3, 0.1], 
                      [0.2, 0.3, 0.3, 0.2], 
                      [0.3, 0.3, 0.4, 0.0], 
                      [0.7, 0.0, 0.0, 0.3], 
                      [0.1, 0.6, 0.3, 0.0]]
def prompt_list_choice(some_list, prompt):
   """ Prints list, prefixing each value with number, starting with 1
       returns choice *after zero-indexing conversion*
   """
   for i, value in enumerate(some_list, start=1):
       print(f"{i}: {value}")
                                       #
   return int(input(f"{prompt} ")) - 1

# Single user's rating 
# change these values to compare the ratings of different users and different movies
rating = 0 # a starting rating
user = 2 # represents the third user in the list of users (Avery)
movie = 3 # represents the fourth movie in the list of movies (Trolls)

# get the estimated rating for a specific movie and a specific user

user = prompt_list_choice(users, "Pick a user (enter number)")
movie = prompt_list_choice(movies, "Pick a movie ")
for genre in range(len(genres)):
    rating += user_preferences[user][genre] * movie_genre[movie][genre]
print(users[user] + "'s", movies[movie], "recommended rating: ", rating)
