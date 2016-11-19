'''Week 2 Assignment
Author: Emmanuel Sibanda
'''
#create database and cursor to connect to DB
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
#open mbox.txt, extract organization from email, store in DB, count times organization appears and sort DB by number of organization appearances (Descending order)
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
filename = ('mbox.txt')
openfile = open(filename)
for line in openfile:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count = count+1 WHERE org =?', (org, ))
    except:
        cur.execute('''INSERT INTO Counts(org,count)
        VALUES (?,1)''', (org, ))
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
conn.commit()
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]
cur.close()
