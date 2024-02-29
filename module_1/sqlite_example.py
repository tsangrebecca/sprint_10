# step 0
import sqlite3
import queries as q

# step 1
# connect to the database
# triple check spelling of database name otherwise a new database will be created
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - Make the "cursor" as an intermediary, we are not allowed to handle it directly
cursor = connection.cursor()

# step 3 - write a query
# query = 'SELECT character_id, name FROM charactercreator_character;' 
# see queries.py file, will have to import it as a module

# step 4 - Execute query on the cursor and fetch the results
# "pulling the results from the cursor"
# grab the query from the queries.py file with an alias as q
# the results will be in a list of tuples
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__=='__main__':
    print(results[:5])