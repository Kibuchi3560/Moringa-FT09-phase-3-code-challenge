from database.connection import Connection

class Magazine:
    def __init__(self, id, name):
        if isinstance(id, int):
            self._id = id
        if isinstance(name, str) or (2 <= len(name) <= 16):
             self._name = name
        else:
             raise ValueError("Name must be a string between 2 and 16 characters.")   
        
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if  isinstance(value, str) or (2 <= len(value) <= 16):
            self._name = value

        raise ValueError("Name must be a string between 2 and 16 characters.")

    def get_articles(self):
        query = "SELECT * FROM articles WHERE magazine_id = ?;"
        return Connection.get_db_connection().execute(query, (self.id,)).fetchall()

    def get_contributors(self):
        query = """
            SELECT DISTINCT authors.* 
            FROM authors 
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?;
        """
        return Connection.get_db_connection().execute(query, (self.id,)).fetchall()

    def get_article_titles(self):
        query = "SELECT title FROM articles WHERE magazine_id = ?;"
        titles = Connection.get_db_connection().execute(query, (self.id,)).fetchall()
        return [title[0] for title in titles]

    def get_contributing_authors(self):
        query = """
            SELECT authors.*, COUNT(articles.id) AS article_count 
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2;
        """
        return Connection.get_db_connection().execute(query, (self.id,)).fetchall()
