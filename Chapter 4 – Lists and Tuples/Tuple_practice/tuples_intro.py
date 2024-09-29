favorite_movies = ("The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction","Forrest Gump")

first_movie = favorite_movies[0]
print("First movie ->",first_movie)
last_movie = favorite_movies[-1]
print("Last movie ->",last_movie)

length_of_tuple = len(favorite_movies)
print(length_of_tuple)


# 4. Check if a Specific Movie is in the Tuple
specific_movie = "Forrest Gump"
is_in_tuple = specific_movie in favorite_movies
print(is_in_tuple)
print(type(is_in_tuple))

print(f"The {specific_movie} is there in the tuple" if is_in_tuple else f"The {specific_movie} movie is not there in the tuple")


