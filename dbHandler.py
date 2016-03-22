import sqlite3


# connection to use. Replace with path to the database.
db = sqlite3.connect('C:/Users/Lope/Desktop/Project4Temp/ProjectFlask/Species.db')
entries = {}


def db_connec(db):
    cur = db.cursor()
    return cur

# use this to test that the database is actually populated.
def show_all(cur):
    for row in cur.execute(('SELECT * FROM Species')):
        print(row)

# this method asks the questions and returns the response as a list
def getinput():
    name = input("Enter the name of the species")
    sciName = input("enter a scientific name")
    desc = input("enter a brief description")

    #print(name, sciName, desc)
    # think of this as our animal object attributes
    obj = [name, sciName,desc]
    return obj

def add_Entry(cur, obj):

    #cur.execute('insert into Species values (?,?,?)', (name, sciName, desc))
    cur.execute('insert into Species values (?,?,?)', (obj[0], obj[1], obj[2]))

    db.commit()
    #todo if loop somewhere to check if connection is open
    #db.close()

# pass in the cursor declared previously.
def prettify(cursor):
    # connect to the database
    db_connec(db)
    # query the whole table
    #thiscursor = the_cursor.execute('select * from species')
    thiscursor = the_cursor.execute('select name, sciName, desc from species')
    #for r in thiscursor:
        # print("this is how i fetch each individual item" )
        # print("name: %s \t sciname: %s\t desc: %s ".format(name=row[0], sciName=row[1], desc=

    # good for storing when i have a primary key , but as of now i don't have one.
    entries = [dict(name=row[0], sciName=row[1], desc=row[2]) for row in thiscursor.fetchall()]

    print("\n\n Here are the dictionary entries")
    for v in range(0, 4):
        print(entries[v])
    print("Here is the entry at location 1")
    print(entries[1])
    print("Here is the entry at location 2")
    print(entries[2])
    return entries
        #print ('here is the name: % \nsciName: %  \nDescription: %'.format(entries['name'], entries['sciname'].values(), entries['desc'].values()))
        #cur = g.db.execute('select name, sciName, desc from species')

# with the name of the animal passed in get its description
def get_description(key):
    the_cursor.execute("Select * from species where name={0}".format(key)).fetchone()
    for row in the_cursor:
        print(row)

def get_by_animal_name():
    the_cursor.execute("select * from species where name='turtle'").fetchone()
    print("Here is the animal by name ")
    for row in the_cursor:
        print(row)

# retrieves the description and scientific name for the animal in question
def get_animal_description():
    # parameterieze term needs to be passed in as a tuple , hence the space after comma
    the_cursor.execute("select name, desc from species where name=?", (term, ))
    for row in the_cursor:
        print(row)

# method to retrieve the animal sci name from db
def get_sci_name(term):
    the_cursor.execute('select name, sciname from species where name=?', (term, ))
    for row in the_cursor:
        print(row)
# use the cursor to communicate with the database
the_cursor = db_connec(db)

# using the cursor show all the entries within the database
#show_all(the_cursor)

#todo create a delete entry method by term or primary key. Once primary key has been implemented into db.
# create a list object to recieve the results of input
info = []
# add user for input. This will be provided in the app through web responses.
info = getinput()

#todo read each row into a dict and manipulate the data to make it easier to format for the webpage

# then add the entry. todo this we will need the cursor connection , and the info provided
add_Entry(the_cursor, info)

# lets see if we can show all if it automatically opens the connection again
show_all(the_cursor)

#testing out new method
prettify(the_cursor)

term = input("enter a key to get the description")
# get_description
str(term)
print("This is what the term looks like  " + str(term))
get_animal_description()
get_sci_name(term)
# print("Here is the info by animal name ")
# get_by_animal_name()

# finally terminate the connection with the database.
db_connec(db).close()

