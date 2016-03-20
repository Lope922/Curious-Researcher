# all the imports
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

	 

# configuration of the database
DATABASE = 'Species.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# NOTE a cleaner solution would be to create a separate .ini or .py file and load that or import the values from there. -- TODO

# create the instance of the app. 
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
	
# method used to create the DB using the suggested database schema mapped out in seperate file 	
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


# Queries the database for all entries and displays them within the webpage. 
@app.route('/')
def show_entries():
	# here is where python needs to listen for the value to come in and once it recieves that value acknowlege it and make the GBIF request 
	return render_template('Project4HomePageTemplate.html')

@app.route("/",methods=['POST'])
def search_animal_name():	
	# results of text box input from button click. 
	animalName = request.form['animalLookup']
	#processed_text = text.upper()
	print("You have entered " + str(animalName))
	return animalName
	
	# need to import my class that has been written for GBIF application. 
	
	
    #cur = g.db.execute('select title, text from entries order by id desc')
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #return render_template('show_entries.html', entries=entries)

	
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

	
# method that makes a simple animal table ( RUN FROM COMMAND LINE TO CREATE DB ALONG WITH INIT_DB )
def make_db():	

    db = sqlite3.connect("flaskr.db")
    cur = db.cursor()
	#cur.execute('drop table if exists entries')
    cur.execute('create table entries (id INTEGER PRIMARY KEY autoincrement, title text not null, text text not null)')

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

