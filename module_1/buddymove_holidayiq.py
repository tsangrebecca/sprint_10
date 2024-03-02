import sqlite3
import pandas as pd

# SQLite connection variables
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cursor = conn.cursor()

# load in the CSV to a pandas DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

if __name__ == '__main__':
    # turn the DF into a SQL-friendly table called 'review'
    df.to_sql('review', conn, if_exists='replace')

    # Query table to ensure that the data was truly added
    cursor.execute('''SELECT * FROM review;''')
    # print(cursor.fetchall())

    # Nature and Shopping both >= 100
    NATURE_SHOPPING = '''
    SELECT COUNT(*) AS greater_100
    FROM review
    WHERE Nature >= 100 AND Shopping >= 100;'''

    # stretch goal - avg number of reviews for each category
    AVG_REVIEWS_FOR_SPORTS = '''
    SELECT AVG(Sports) FROM review;'''

    AVG_REVIEWS_FOR_RELIGIOUS = '''
    SELECT AVG(Religious) FROM review;'''

    AVG_REVIEWS_FOR_NATURE = '''
    SELECT AVG(Nature) FROM review;'''

    AVG_REVIEWS_FOR_Theatre = '''
    SELECT AVG(Theatre) FROM review;'''

    AVG_REVIEWS_FOR_SHOPPING = '''
    SELECT AVG(Shopping) FROM review;'''

    AVG_REVIEWS_FOR_PICNIC = '''
    SELECT AVG(Picnic) FROM review;'''