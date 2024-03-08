# Just copied & pasted from module2 insert_titanic.py
import psycopg2
from os import getenv
import pandas as pd
from queries import QUERY_LIST

# Grab environment variables from the .env file
DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

# print(DBNAME)
# print(USER)
# print(PASSWORD)
# print(HOST)

# Create a Postgres connection object with pg_conn, opens a connection
#   to a Postgres instance that has already been created on ElephantSQL
#   using specific credentials
# Create a cursor
# Need the conn when I want to commit(), and the curs when I want to modify
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

# Method 1 of writing execute query:
def execute_query_pg(curs, conn, query):
    curs.execute(query)
    return curs.fetchall() # It's a SQLite thing but it also works with PostgreSQL
'''From ChatGPT: In this function, the curs.execute(query) is called to execute the query, 
and then curs.fetchall() is used to retrieve all the rows returned by the query. 
This function is designed to be used when you want to fetch and return the result set of the query.'''

# Method 2 that didn't work here
# # Compare to this way of writing that we used in module2 > insert_titanic.py
# def execute_query_pg(curs, conn, query):
#     results = curs.execute(query)
#     conn.commit()
#     return results
'''In this function, the curs.execute(query) is called to execute the query, 
and then conn.commit() is used to commit the changes made by the query to the database. 
The results variable is then returned. This function is more suitable for queries 
that modify the database (e.g., INSERT, UPDATE, DELETE) 
and don't necessarily return a result set. 
The results variable will typically be the number of affected rows. It's worth noting that 
the second function might not work as expected because 
the curs.execute() method in many Python database APIs returns None 
or the number of affected rows (not the result set). 
If you want to execute a query that modifies the database 
and still get the result set, you should use curs.fetchall() 
after executing the query, similar to the first function.''' 

# Loop over the query list, like in databases > rpg_queries.py
def execute_queries(curs, conn, queries):
    answers_dict = {}
    for index, query in enumerate(queries):
        answers_dict[index] = execute_query_pg(curs, conn, query)
    return answers_dict

if __name__ == "__main__":
    answers_dict = execute_queries(pg_curs, pg_conn, QUERY_LIST)
    for index, value in enumerate(answers_dict.values()):
        print(f'{index}: {value}')