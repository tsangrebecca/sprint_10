# step 0
import sqlite3
import queries as q
import pandas as pd

# DB connect function
# takes care of the step 1 below with a function
def connect_to_db(db_name='rpg_db.sqlite3'): 
    # can take any database name, but if none provided, default would be the one listed
    return sqlite3.connect(db_name)

# function to execute that takes care of steps 2, 3, 4
def execute_q(conn, query):
    curs = conn.cursor() # step 2: making the cursor
    curs.execute(query) # step 4a: execute the query
    return curs.fetchall() # step 4b: pull and return the results

# # step 1
# # connect to the database
# # triple check spelling of database name otherwise a new database will be created
# connection = sqlite3.connect('rpg_db.sqlite3')

# # step 2 - Make the "cursor" as an intermediary, we are not allowed to handle it directly
# cursor = connection.cursor()

# step 3 - write a query
# query = 'SELECT character_id, name FROM charactercreator_character;' 
# see queries.py file, will have to import it as a module

# # step 4 - Execute query on the cursor and fetch the results
# # "pulling the results from the cursor"
# # grab the query from the queries.py file with an alias as q
# # the results will be in a list of tuples
# results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__=='__main__':
    conn = connect_to_db()
    # print(execute_q(conn, q.SELECT_ALL)[:5]) # if we just want the 1st 5
    # print(results[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['Name', 'Average_item_weight']

    # from SQL to csv
    df.to_csv('rpg_db.csv', index=False) # don't keep row index as column