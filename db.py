import sqlite3

from models import Book


class ScndBrainDB:
    DB_NAME = "scnd_brain.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.DB_NAME)
        self.cursor = self.connection.cursor()

        # Initialize the tables
        self.create_book_table()

    def __del__(self):
        self.connection.close()

    def create_book_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS book (
        title TEXT,
        author TEXT,
        published INTEGER,
        state_id INTEGER
        )
        """
        self.cursor.execute(query)

    def create_state_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS state (
        title TEXT
        )
        """
        self.cursor.execute(query)

    def insert_book(self, book: Book) -> None:
        query = """
        INSERT INTO book ()
        """

    def test_insert(self) -> None:
        query = """
        insert into book values
        ("War and Peace", "Lev Tolstoy", 1869, 1)
        """
        self.cursor.execute(query)

    def test_select(self) -> list[dict]:
        query = """
        select * from book
        """
        result = self.cursor.execute(query).fetchall()
        return result

    def drop_tables(self) -> None:
        query = """
        drop table book
        """
        self.cursor.execute(query)


if __name__ == "__main__":
    db = ScndBrainDB()
    db.test_insert()
    result = db.test_select()
    print(result)
    db.drop_tables()
