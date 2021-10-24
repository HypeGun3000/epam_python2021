import sqlite3


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
        query = self.cursor.execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                return president

    def __contains__(self, item: str):
        query = self.cursor.execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                print(f'{item} in {self.table}')
                return True


