import sqlite3
conn = sqlite3.connect('example.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * FROM presidents ')
data = cursor.fetchall()
print(data)

class TableData:
    def __init__(self, presidents):
        self.presidents = presidents

presidents = TableData
print(len(presidents))
