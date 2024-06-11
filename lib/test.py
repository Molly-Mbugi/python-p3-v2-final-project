from movie import Movie
from director import Director

# Drop and recreate tables (for testing purposes)
Movie.drop_table()
Movie.create_table()

Director.drop_table()
Director.create_table()

# Create instances of Movie and Director
movie1 = Movie(None, "The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "Drama", 142, "1994-09-23")
movie1.save()

movie2 = Movie(None, "The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "Crime", 175, "1972-03-24")
movie2.save()

director1 = Director(None, "Frank Darabont", "Castle Rock Entertainment")
director1.save()

director2 = Director(None, "Francis Ford Coppola", "Paramount Pictures")
director2.save()

# Update a movie and a director
movie1.title = "The Shawshank Redemption (1994)"
movie1.update()

director2.production = "Paramount Pictures, American Zoetrope"
director2.update()

# Delete a movie and a director
#movie2.delete()
#director1.delete()

# Find by name examples
found_movie = Movie.find_by_name("The Shawshank Redemption (1994)")
if found_movie:
    print("Found Movie:", found_movie)
else:
    print("Movie not found")

found_director = Director.find_by_name("Francis Ford Coppola")
if found_director:
    print("Found Director:", found_director)
else:
    print("Director not found")

# Fetch all movies and directors
print("\nMovies:")
for movie in Movie.get_all_movies():
    print(movie)

print("\nDirectors:")
for director in Director.get_all_directors():
    print(director)