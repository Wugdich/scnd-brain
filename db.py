import sqlite3


class SqliteDB:
    DB_NAME = "scnd_brain.db"

    def __init__(self):
        self.con = sqlite3.connect(self.DB_NAME)
        self.cur = self.con.cursor()

        self.create_task_table()

    def create_task_table(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS task (
        id type,
        title type,
        cor3 type,
        )
        """
        self.cur.execute(query)

    def insert_task(self):
        ...

    def get_task(self):
        ...
