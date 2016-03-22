# all the imports
import sqlite3
from flickr import *
from species_request import *
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration of the database
DATABASE = './Species.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# NOTE a cleaner solution would be to create a separate .ini or .py file and load that or import the values from there. -- TODO

# create the instance of the app.
app = Flask(__name__)
#configureations of the flask environment
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# method used to connect to the database in the location provided above in the DATABASE value
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# method that initializes the database by reading from said file
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('Speciesschema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# before any request can be made server needs to establish a connection with the database
@app.before_request
def before_request():
    g.db = connect_db()


# reads request #Register a function to be run at the end of each request, regardless of whether there was an exception or not. These functions are executed when the request context is popped, even if not an actual request was performed.
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# Displays the mainpage on default web page load
@app.route('/')
def show_entries():
	# here is where python needs to listen for the value to come in and once it recieves that value acknowlege it and make the GBIF request
	return render_template('Project4HomePageTemplate.html')


# This method processes input and sends it onto the database. NOTE: THERE IS NO ERROR CHECKING PRIOR TO THIS.
# experimenting with post and get request types
@app.route("/results", methods=['POST'])
def search_animal_name():

	# results of text box input from button click.
	animalName = request.form['animalLookup']

	# GBIF Portion
	newAnimal = Animal
	newAnimal.name = str(animalName)
	data = search(animalName)
	newAnimal.extraction(newAnimal,data)
	
	#scientificName TODO fix this to take first scientific name in list
	#sn = scientificName[0]
	#print("Here is the one scientific name")
	#print(str(sn))
	#show_descript()
	# need to pull the first element in the scientificName array just to display something 
	
	#####################################
	
	## Flickr portion 
	json_resp = make_flickr_query(animalName)
	# show links for fun. 
	show_links()
	#have this working , but not filtered properly and isn't being stored in db yet 
	#image1url = photoUrl_list[0]
	
	
	# todo try and print links in webpage that way i know they are making it there. 
	db = sqlite3.connect('./Species.db')
	cur = db.cursor()
	for row in cur.execute('Select name, sciName, desc from Species'):
		print(row)
	
	
	#return render_template('test.html',animalName=animalName)
	return render_template('PageTwodiffBG.html')
	#return animalName
	

#TODO write this method to display page 2 with information properly formatted
@app.route("/printitems", methods=['POST'])
def display_results():
	# assign each value to it counterpart on the page prior to loading the page. 
	# may need to render a new template or redirect to this one. For now i am just redirecting from home page. 
	
	db = sqlite3.connect('./Species.db')
	cur = db.cursor()
	for row in cur.execute('Select name, sciName, desc from Species'):
		print(row)
	return print_row()
	
	#cur = g.db.execute('select * from Species')
	#entries = [dict(name=row[0], sciName=row[1], desc=row[3]) for row in cur.fetchall()] 
	#return render_template('test.html', entries=entries)
	
@app.route('/printitems')
def print_row():
	cur = g.db.execute('Select * from Species')
	query = 'SELECT * FROM Species'
	db.row_factory = make_dicts
	return redirect(url_for('display_results'))
# how posts are added to the database using the Post method 	
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

	
#def make_dicts(cursor, row):
#	return dict((cur.description[idx][0], value))
	#for idx, value in enumerate(row)
		
#def query_db(query, args=(), one=False):
#	cur = get_db().execute(query, args)
#	rv = cur.fetchall()
#	cur.close()
#	return (rv[0] if rv else None) if one else rv
	
	
# method that makes a simple animal table ( RUN FROM COMMAND LINE TO CREATE DB ALONG WITH INIT_DB )
def make_db():	

    db = sqlite3.connect("Species.db")
    cur = db.cursor()
	#cur.execute('drop table if exists Species')
    cur.execute('create table Species (id INTEGER PRIMARY KEY autoincrement, Name text not null, Description text not null)')

    #################PSUEDO CODE ############
    #db = sqlite3.connect("flaskrDB.db")
    #cur = db.cursor()

 #cur.execute('create table species (name text, scientificName text, image1 image) ')

    db.commit()
    db.close()
    ########################################################
    # this method creates the database through python commands

		
if __name__ == '__main__':
    app.run()

