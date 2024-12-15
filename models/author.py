from database.connection import Connection
from typing import List, Dict

class Author:
    def __init__(self, id, name):
        if isinstance(id, int):
            self._id = id
        else:
            raise TypeError("ID must be an integer / number.")
        if isinstance(name, str) or not name.strip():
            self._name = name
        else:
            raise TypeError("Name must not be an empty string.")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def get_articles(self) :
        connection = Connection.get_db_connection()
        query = "SELECT * FROM articles WHERE author_id = ?;"
        return connection.execute(query, (self.id,)).fetchall()

    def get_magazines(self):
        connection = Connection.get_db_connection()
        query = """
            SELECT DISTINCT m.* 
            FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?;
        """
        return connection.execute(query, (self.id,)).fetchall()

    def __repr__(self) :
        return (f"Author(id={self.id}, name='{self.name}')")
