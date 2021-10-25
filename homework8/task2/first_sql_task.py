import sqlite3


class TableData:
    def __init__(self, **kwargs):
        self.connection = sqlite3.connect(kwargs["database_name"])
        self.table = kwargs["table_name"]
        self.cursor = self.connection.cursor()
        self.execute = \
            self.cursor.execute(f'SELECT * FROM {kwargs["table_name"]}')
        self.columns = [column[0] for column in self.cursor.description]

    def __len__(self) -> int:
        return len(self.execute.fetchall())

    def __getitem__(self, item: str) -> str:
        query = self.cursor.execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                return president

    def __contains__(self, item: str) -> bool:
        query = self.cursor.execute(f'SELECT * FROM {self.table}')
        for president in query:
            if item in president:
                return True

    def __iter__(self) -> iter:
        dict_of_information = {}
        query = self.cursor.execute(f'SELECT * FROM {self.table}')
        for info in query:
            for j in range(len(info)):
                dict_of_information[self.columns[j]] = info[j]
                print(dict_of_information)
            yield dict_of_information
