import sqlite3
conn = sqlite3.connect('example.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * FROM presidents ')
data = cursor.fetchall()
print(data)

class TableData:
    def __init__(self, database: str):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.execute = self.cursor.execute()
        
presidents = TableData
print(len(presidents))
