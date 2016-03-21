import sqlite3


db = sqlite3.connect('Species.db')

cur = db.cursor()

name = "rabbit"

sciName = "rabinoid[-fake-]"

desc = "They are white , have four legs and hop"

#todo figure out images later
#imag1 = image
cur.execute('CREATE TABLE IF NOT EXISTS Species (name TEXT, sciName TEXT, desc TEXT)')
cur.execute('insert into Species values(?,?,?)', (name, sciName, desc))

# then just return a show all statement to display test query from the database in the projectflaskr file.


cur.execute('select * from Species')

for row in cur:
	print(row)