from database.connection import Connection
from models.author import Author  
from models.magazine import Magazine 

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("ID must be an integer.")

        if  isinstance(title, str) or not (5 <= len(title) <= 50):
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        if isinstance(content, str):
            self._content = content
        else:
            raise ValueError("Content must be a string.")

        if isinstance(author_id, int):
            self._author_id = author_id
        else:
            raise ValueError("Author ID must be an integer.")

        if isinstance(magazine_id, int):
            self._magazine_id = magazine_id
        else:
            raise ValueError("Magazine ID must be an integer.")

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._fetch_related_entity("authors", self._author_id, Author)

    @property
    def magazine(self):
        return self._fetch_related_entity("magazines", self._magazine_id, Magazine)

    def _fetch_related_entity(self, table: str, entity_id: int, entity_class):
        query = f"SELECT * FROM {table} WHERE id = ?;"
        connection = Connection.get_db_connection()
        result = connection.execute(query, (entity_id,)).fetchone()
        return entity_class(*result) if result else None