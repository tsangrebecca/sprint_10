import sqlite3
from queries import QUERY_LIST

conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()

'''For a single query'''
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

'''Use above function as a helper function (function within function
Loop over all queries that I'm importing once it gets called and use
dictionary to save all our answers '''
def execute_queries(cursor, queries):
    answers = {}
    for index, query in enumerate(queries):
        answers[index] = execute_query(cursor, query) # prev function
    return answers

if __name__== '__main__':
    answers = execute_queries(cursor, QUERY_LIST)
    for key, value in enumerate(answers.values()):
        print(f"{key}: {value}")

