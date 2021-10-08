import sqlite3


class TableData:
    def __init__(self, **kwargs):
        self.connection = sqlite3.connect(kwargs["database_name"])
        self.table = kwargs["table_name"]
        self.cursor = self.connection.cursor()
        self.execute = self.cursor.execute(f'SELECT * FROM {kwargs["table_name"]}')
        self.data = self.execute.fetchall()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] == item:
                    return self.data[i]

    def __contains__(self, item):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] == item:
                    print(f'{item} in {self.table}')
                    return True


if __name__ == '__main__':
    presidents = TableData(database_name='example.sqlite', table_name='presidents')
    print(presidents.connection)
    print(presidents.cursor)
    print(presidents.execute)
    print(presidents.data)
    print(len(presidents))
    print(presidents['Yeltsin'])
    print(presidents['Big Man Tyrone'])
    print("Yeltsin" in presidents)
