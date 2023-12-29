import sqlite3

from config import DB_PATH
from models import Book


class ScndBrainDB:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        # Initialize the tables
        self.create_book_table()
        self.create_shopping_table()

    def __del__(self):
        self.connection.close()

    def create_shopping_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS shopping (
            title TEXT
        )
        """
        self.cursor.execute(query)

    def create_book_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS book (
        title TEXT,
        author TEXT,
        published INTEGER,
        read_times INTEGER
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

    def insert_item(self, item: str) -> None:
        query = """
        INSERT INTO shopping VALUES (?)
        """
        parameters = (item,)
        self.cursor.execute(query, parameters)

    def insert_book(self, book: Book) -> None:
        query = """
        INSERT INTO book VALUES (
            :title, 
            :author, 
            :published, 
            :read_times
            )
        """
        self.cursor.execute(query, book.model_dump())
        self.connection.commit()

    def test_insert(self) -> None:
        query = """
        insert into shopping values
        ("Молоко")
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
        drop table shopping
        """
        self.cursor.execute(query)


if __name__ == "__main__":
    print("Start testing db.py module.")
    db = ScndBrainDB()
    book = Book(title="Little Prince", author="Exuperi", published=1947, read_times=2)
    db.insert_book(book)
    result = db.test_select()
    print(result[0]["title"])
    db.drop_tables()
    print("End testing db.py module.")
