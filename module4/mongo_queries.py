# copied from module3 > mongodb.py
import pymongo
# import sqlite3 # won't need sqlite3 this time
from queries import MongoAnswers

PASSWORD = 't2mqBdfXnGvPtf6q'
DBNAME = 'rpg_data' # if we're more thorough, we should use .env
# Make sure to create a collection called the DBNAME 'rpg_data'
#   on mongoDB.com after this and before we try to insert any data

# Not using a function this time
client = pymongo.MongoClient(f'mongodb+srv://tsangyrebecca:{PASSWORD}@cluster0.exltnxc.mongodb.net/{DBNAME}?retryWrites=true&w=majority&appName=Cluster0')
db = client.rpg_data
collection = db['rpg_data']

# Instantiate our class with our characters attribute and query methods
mongo_answers = MongoAnswers(collection)

if __name__ == '__main__':
    print(mongo_answers.show_results())