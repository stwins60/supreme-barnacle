import sqlite3 as sql
from sqlite3 import Error

conn = sql.connect('message_box.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS messages")

QUERY = """CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL) """

c.execute(QUERY)
conn.commit()
print("Table created successfully")

def add_message(email, subject, message):
    try:
        c.execute("INSERT INTO messages (email, subject, message) VALUES (?, ?, ?)", (email, subject, message))
        conn.commit()
    except Error as e:
        print("Error: ", e)

