import sqlite3

with sqlite3.connect('test_database.db') as connection:

 c=connection.cursor()

c.executescript("""

DROP TABLE IF EXISTS People;

CREATE TABLE People(FirstNam TEXT, LastName TEXT, AgeINT);

INSERT INTO People VALUES('Ron', 'Obvious', '42');

""")
