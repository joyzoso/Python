import sqlite3

conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE roster
                    (Name text, Species text, IQ Int)
                                   """)

roster = [('Jean-Baptiste Zorg', 'Human', 122),
          ('Korben Dallas', 'Meat Popsicle', 100),
          ('Ak''not', 'Mangalore', -5)]

cursor.executemany("INSERT INTO roster VALUES (?,?,?)", roster)
conn.commit()

print cursor.fetchall()

for row in conn.execute('SELECT * FROM roster ORDER BY name'):
    print row

sql = """
UPDATE roster
SET species = 'Human'
WHERE name = 'Korben Dallas'
"""

cursor.execute(sql)
conn.commit()

for row in conn.execute('SELECT * FROM roster ORDER BY name'):
    print row

sql = "SELECT Name, IQ FROM roster WHERE Species = ?"
cursor.execute(sql, [('Human')])

for row in cursor.fetchall():
    Name, IQ = row
    print row

conn.commit()
