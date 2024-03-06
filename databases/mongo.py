'''Transferring data from SQL to NoSQL'''
import pymongo
from sqlite_example import connect_to_db, execute_q
import queries_from_lecture as q

# How our request will return from SQLite
# we get these data from sqlite_example.py file as list of tuples
test_characters = [
    (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), 
    (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)]

# How are data will be stored inside of mongoDB
# still an array which contains 2 dictionaries
character_documents = [
    {
    'character_id': 1, 
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1,
    },
    {
    'character_id': 2, 
    'name': 'Optio dolorem ex a',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1,
    }
]

# Credentials
DBNAME = 'test'
PASSWORD = 'npa1hI0AhHpeXI3x'

'''Connect to the mongoDB'''
# just name the collection_name 'characters'
def mongo_connect(password=PASSWORD, dbname=DBNAME, collection_name='characters'):
    # copy & paste from Colab, but change PASSWORD in URL to password and DBNAME to dbname to parameterize the function
    client = pymongo.MongoClient(f'mongodb+srv://tsangyrebecca:{password}@cluster0.ocpi5a7.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Cluster0')
    db = client[dbname] # in our Colab example, our dbname is 'test'
    collection = db[collection_name]
    # basically there are 3 layers
    # client[dbname][collection_name]
    return collection

if __name__ == '__main__':
    # # Test if we can connect to the mongo database
    # # let's try to overwrite the default collection_name with 'people'
    # collection = mongo_connect(collection_name='people')
    # # see if we can find an object called Ryan
    # result = collection.find_one({'name': 'Ryan'})
    # # show the result in Git Bash
    # print(result)

    # Get characters from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, q.GET_CHARACTERS)
    # print(sl_characters[:3])

    # Connect to a specific mongoDB collection
    collection = mongo_connect(collection_name='characters')

    for character in sl_characters:
        doc = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8],
        }
        collection.insert_one(doc)

        # check the total documents in mongoDB to make sure we have 302
