import sqlite3

with sqlite3.connect('test_database.db')as connection:
    c = connection.cursor()

    personData = (firstName, lastName, age)
    c.execute("INSERT INTO People VALUES(?, ?, ?)",personData)

c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",

(78, 'Harold', 'Lalal'))