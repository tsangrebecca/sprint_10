import psycopg2

# connect to rpg database and to pull data from it
from sqlite_example import connect_to_db, execute_q
from queries_from_lecture import GET_CHARACTERS, DROP_CHARACTER_TABLE, CREATE_CHARACTER_TABLE, INSERT_RYAN

# from queries_from_lecture import CREATE_TEST_TABLE, INSERT_TEST_TABLE, DROP_TEST_TABLE

# PostgreSQL Connection Credentials

# "User & Default database" from ElephantSQL
DBNAME = 'bmxeysmd'
USER = 'bmxeysmd'
# "Password" from ElephantSQL
# BE CAREFUL, don't put passwords in .py but this is just a class example
PASSWORD = 'VnxsYBqgVPcSDpep3thNBMbVPfOluDUH'
# "Server" minus the text in () from ElephantSQL
HOST = 'bubble.db.elephantsql.com'

# Create a Postgres connection object with pg_conn, opens a connection
#   to a Postgres instance that has already been created on ElephantSQL
#   using specific credentials
# I need the conn when I want to commit(), and the curs when I want to modify
def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

# to modify the table
def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()


# # will return a connection object, and is saved to a variable name
# pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
# pg_curs = pg_conn.cursor()
# # replaced by the function above

if __name__== "__main__":
    # Get characters from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    # print(sl_characters[:5])

    # Create destination table within our PostgreSQL database
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    # gotta be careful with dropping tables!!!
    modify_db(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)



    # Loop over characters & insert into PostgreSQL with correct values
    # don't have to grab the ID, so just grabbing the 8 values in each character
    #  so that's why we don't need the first column character[0]
    for character in sl_characters:
        modify_db(pg_conn, pg_curs,
            f'''
            INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
            VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]});
            '''
            )
    
    # The loop got "tuple index out of range" error because GET_CHARACTERS we 
    #  didn't select all the columns. After changing it to SELECT *, it worked!
    # print(sl_characters[:3])
        
    # Got another error. PostgreSQL thought the name with 4 words between
    #  spaces are 4 different names, so to resolve this we need to wrap
    #  the {character[1]} in '' to make it think it's a string.

    # # drop existing test_table if there's one to start fresh
    # pg_curs.execute(DROP_CHARACTER_TABLE)

    # # if we modify table, we have to execute and commit as well
    # # with the IF NOT EXISTS in the queries for creating table,
    # #   it will bypass these two lines if table is already created
    # pg_curs.execute(CREATE_CHARACTER_TABLE)

    # # to add data into rows in the table
    # pg_curs.execute(INSERT_RYAN)
    # pg_conn.commit() # only need one line of commit() at the end

    # we can write a function to replace above repetitive codes


