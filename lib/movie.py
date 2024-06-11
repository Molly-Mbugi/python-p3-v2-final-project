from config import conn, cursor

class Movie:
    def __init__(self, id=None, title=None, about=None, genre=None, duration=None, release_date=None, director_id=None):
        self.id = id
        self.title = title
        self.about = about
        self.genre = genre
        self.duration = duration
        self.release_date = release_date
        self.director_id = director_id

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}, {self.genre}, {self.release_date}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not value:
            raise ValueError("Genre cannot be empty")
        self._genre = value

    @classmethod
    def create_table(cls):
        """ Create the movies table if it does not exist """
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                about TEXT,
                genre TEXT,
                duration INTEGER,
                release_date TEXT,
                director_id INTEGER,
                FOREIGN KEY (director_id) REFERENCES directors(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the movies table if it exists """
        sql = "DROP TABLE IF EXISTS movies"
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """ Save the movie instance to the database """
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO movies (title, about, genre, duration, release_date, director_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (self.title, self.about, self.genre, self.duration, self.release_date, self.director_id))
            conn.commit()
            self.id = cursor.lastrowid

    def update(self):
        """ Update the movie's attributes in the database """
        sql = """
            UPDATE movies
            SET title = ?, about = ?, genre = ?, duration = ?, release_date = ?, director_id = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.title, self.about, self.genre, self.duration, self.release_date, self.director_id, self.id))
        conn.commit()

    def delete(self):
        """ Delete the movie from the database """
        sql = "DELETE FROM movies WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def find_by_title(cls, title):
        """ Find and return a movie by title """
        sql = "SELECT * FROM movies WHERE title = ?"
        cursor.execute(sql, (title,))
        row = cursor.fetchone()
        if row:
            return cls(*row)  # Assuming __init__ expects (id, title, about, genre, duration, release_date, director_id)
        return None

    @classmethod
    def get_all_movies(cls):
        """ Fetch all movies from the database """
        sql = "SELECT * FROM movies"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]


