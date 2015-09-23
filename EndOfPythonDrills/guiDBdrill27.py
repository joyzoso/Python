import sqlite3
import time

conn = sqlite3.connect('ftpDrill.db')
c = conn.cursor()


def createtable():
    c.execute("CREATE TABLE boo(ID INT, date TEXT, time TEXT, filename TEXT)")


def lasttransfer():
    timeran = time.clock()
    print(timeran)

createtable()
lasttransfer()

#need to be able to retrieve the data and record date and time (using datetime.time)
#and display data.
