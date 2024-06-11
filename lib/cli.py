import sys
from director import Director  
from movie import Movie  

def print_menu():
    """Prints the main menu options."""
    print("\nPlease select an option:")
    print("1. Manage 1Directors")
    print("2. Manage Movies")
    print("0. Exit")

def list_directors():
    """Lists all directors."""
    directors = Director.get_all_directors()
    if directors:
        for director in directors:
            print(director)
    else:
        print("No directors found.")

def create_director():
    """Creates a new director."""
    name = input("Enter the name of the director: ")
    production = input("Enter the production of the director (optional): ")
    director = Director(name=name, production=production)
    director.save()
    print(f"Director '{director.name}' created successfully with ID {director.id}.")

def list_movies():
    """Lists all movies."""
    movies = Movie.get_all_movies()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found.")

def create_movie():
    """Creates a new movie."""
    title = input("Enter the title of the movie: ")
    genre = input("Enter the genre of the movie: ")
    about = input("Enter a description of the movie (optional): ")
    duration = int(input("Enter the duration of the movie in minutes: "))
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    director_id = int(input("Enter the ID of the director for the movie: "))
    movie = Movie(title=title, genre=genre, about=about, duration=duration, release_date=release_date, director_id=director_id)
    movie.save()
    print(f"Movie '{movie.title}' created successfully with ID {movie.id}.")

def main():
    """Main function to run the CLI."""
    while True:
        print_menu()
        choice = input("> ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            manage_directors()
        elif choice == "2":
            manage_movies()
        else:
            print("Invalid choice. Please select a valid option.")

def manage_directors():
    """Sub-menu for managing directors."""
    while True:
        print("\nDirector Management:")
        print("1. List all directors")
        print("2. Create a new director")
        print("0. Back to main menu")
        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            list_directors()
        elif choice == "2":
            create_director()
        else:
            print("Invalid choice. Please select a valid option.")

def manage_movies():
    """Sub-menu for managing movies."""
    while True:
        print("\nMovie Management:")
        print("1. List all movies")
        print("2. Create a new movie")
        print("0. Back to main menu")
        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            list_movies()
        elif choice == "2":
            create_movie()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()




