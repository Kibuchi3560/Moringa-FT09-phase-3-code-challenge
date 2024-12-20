import sqlite3

# Specify the database file location
DATABASE_NAME = './database/magazine.db'

class Connection:
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row  
        return conn
