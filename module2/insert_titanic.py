import psycopg2
from os import getenv
import pandas as pd

DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

print(DBNAME)
print(USER)
print(PASSWORD)
print(HOST)

# Create a Postgres connection object with pg_conn, opens a connection
#   to a Postgres instance that has already been created on ElephantSQL
#   using specific credentials
# Create a cursor
# I need the conn when I want to commit(), and the curs when I want to modify
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

def execute_query_pg(curs, conn, query):
    results = curs.execute(query) # don't need fetchall() with Postgres
    conn.commit()
    return results
    # This function didn't work for module4 > postgresql_queries.py
    #   but the fetchall() works as in databases > rpg_queries.py
    #   WHY????

# Write a query that will create the table
CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic_table 
    (
    "passenger_id" SERIAL NOT NULL PRIMARY KEY,
    "survived" INT NOT NULL,
    "pclass" INT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "sex" VARCHAR(10) NOT NULL,
    "age" FLOAT NOT NULL,
    "siblings_spouses_aboard" INT NOT NULL,
    "parents_children_aboard" INT NOT NULL,
    "fare" FLOAT NOT NULL
    );
'''
DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic_table
'''
df = pd.read_csv('titanic.csv')

# removing all the ' in Irish names
df['Name'] = df['Name'].str.replace("'", "")

if __name__== "__main__":
    # Drop existing table to prevent too many rows added 
    #   as we kept running the same file
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)

    # Create the table with its associated schema
    execute_query_pg(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

    records = df.values.tolist() # turns df to numpy array using .values,
                                 # then we can apply .tolist() method
                                 # it'll be a list of lists but we want a list
                                 # of tuples!
    for record in records:
        INSERT_STATEMENT = '''
            INSERT INTO titanic_table ("survived", "pclass", "name", "sex", 
            "age", "siblings_spouses_aboard", "parents_children_aboard", "fare")
            VALUES {};
            '''.format(tuple(record))
        execute_query_pg(pg_curs, pg_conn, INSERT_STATEMENT)

    # SHOULD HAVE 887 rows of data