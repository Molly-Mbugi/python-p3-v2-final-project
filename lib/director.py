from config import conn, cursor

class Director:
    def __init__(self, id, name, production):
        self.id = id
        self.name = name
        self.production = production

    def __repr__(self):
        return f"<Director {self.id}: {self.name}, {self.production}>"

    @classmethod
    def create_table(cls):
        """ Create the directors table if it does not exist """
        sql = """
            CREATE TABLE IF NOT EXISTS directors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                production TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the directors table if it exists """
        sql = "DROP TABLE IF EXISTS directors"
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """ Save the director instance to the database """
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO directors (name, production)
                VALUES (?, ?)
            """
            cursor.execute(sql, (self.name, self.production))
            conn.commit()

            self.id = cursor.lastrowid

    def update(self):
        """ Update the director's attributes in the database """
        sql = """
            UPDATE directors
            SET name = ?, production = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.production, self.id))
        conn.commit()

    def delete(self):
        """ Delete the director from the database """
        sql = "DELETE FROM directors WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def find_by_name(cls, name):
        """ Find and return a director by name """
        sql = "SELECT * FROM directors WHERE name = ?"
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        if row:
            return cls(*row)  # Assuming __init__ expects (id, name, production)
        return None

    @classmethod
    def get_all_directors(cls):
        """ Fetch all directors from the database """
        sql = "SELECT * FROM directors"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]