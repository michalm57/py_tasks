import sqlite3

# Connect to a (new) database
conn = sqlite3.connect("alpha.db")

# Create a cursor
# Or also execute on connection, connection create the cursor for data access
cur = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)''')

names_list = [
    ("John", "Doe"),
    ("Jane", "Smith"),
    ("David", "Brown"),
    ("Emily", "Johnson"),
    ("Michael", "Williams")
]

cur.executemany('''
                INSERT INTO people (first_name, last_name) VALUES (?, ?)
                ''', names_list)



# Insert data into database

conn.commit()

# Close connection
conn.close()