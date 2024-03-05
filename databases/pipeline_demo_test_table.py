import psycopg2
from queries_from_lecture import CREATE_TEST_TABLE, INSERT_TEST_TABLE, DROP_TEST_TABLE

# PostgreSQL Connection Credentials

# "User & Default database" from ElephantSQL
DBNAME = 'bmxeysmd'
USER = 'bmxeysmd'
# "Password" from ElephantSQL
# BE CAREFUL, don't put passwords in .py but this is just a class example
PASSWORD = 'VnxsYBqgVPcSDpep3thNBMbVPfOluDUH'
# "Server" minus the text in () from ElephantSQL
HOST = 'bubble.db.elephantsql.com'

# will return a connection object, and is saved to a variable name
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

if __name__== "__main__":

    # drop existing test_table if there's one to start fresh
    pg_curs.execute(DROP_TEST_TABLE)

    # if we modify table, we have to execute and commit as well
    # with the IF NOT EXISTS in the queries for creating table,
    #   it will bypass these two lines if table is already created
    pg_curs.execute(CREATE_TEST_TABLE)

    # to add data into rows in the table
    pg_curs.execute(INSERT_TEST_TABLE)
    pg_conn.commit() # only need one line of commit() at the end