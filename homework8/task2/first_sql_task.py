import sqlite3
from collections import namedtuple


class TableData:
    def __init__(self, **kwargs):
        self.connection = sqlite3.connect(kwargs["database_name"])
        self.table = kwargs["table_name"]
        self.cursor = self.connection.cursor()
        self.execute = \
            self.cursor.execute(f'SELECT * FROM {kwargs["table_name"]}')
        self.columns = [column[0] for column in self.cursor.description]

    def __len__(self):
        return len(self.execute.fetchall())

    def __getitem__(self, item: str):
        query = self.connection.cursor(). \
            execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                return president

    def __contains__(self, item: str):
        query = self.connection.cursor(). \
            execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                print(f'{item} in {self.table}')
                return True

    def __iter__(self):
        query = self.cursor.execute(f"SELECT * from {self.table}")
        name = self.columns[0]
        self.unique_value_column = [name[0] for name in query]
        self.column = namedtuple("Presidents_column", f"{name}")
        self.start = 0
        return self

    def __next__(self):
        if self.start >= len(self.cursor.execute(f"SELECT * FROM {self.table}").fetchall()):
            raise StopIteration
        self.current_row = self.cursor.execute(
            f"SELECT * FROM {self.table} WHERE name=:value",
            {"value": self.unique_value_column[self.start]},
        ).fetchone()
        name = self.current_row
        column = self.column(name)._asdict()
        self.start += 1
        return column
