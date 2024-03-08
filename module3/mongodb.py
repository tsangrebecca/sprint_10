import pymongo
import sqlite3

PASSWORD = 't2mqBdfXnGvPtf6q'
DBNAME = 'rpg_data'
# Make sure to create a collection called the DBNAME 'rpg_data'
#   on mongoDB.com after this and before we try to insert any data

def create_mdb_connection(password, dbname):
    # cannot do multi-line for URL
    client = pymongo.MongoClient(f'mongodb+srv://tsangyrebecca:{password}@cluster0.exltnxc.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Cluster0')
    return client

def create_sl_connection(dbname='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(dbname)
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()

# Querying from SQLite
def doc_creation(db, sl_curs, character_table_query, item_table_query, weapon_table_query):
    weapons = execute_query(sl_curs, weapon_table_query)
    characters = execute_query(sl_curs, character_table_query)
    for character in characters:
        item_character_query = item_table_query.format("\'%s\'" % character[1])
        # %s is where we insert some item in a tuple, and after the second %
        #   sign it's the item that we wanna insert
        #   character[1] is the name of the character, the id being character[0]
        item_names = execute_query(sl_curs, item_character_query) # will create an array of items and each item has a name
        weapon_names = []
        for item in item_names:
            if item in weapons:
                weapon_names.append(item[0])

        # We need to insert data into mongoDB as dictionaries
        document = {
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8],
            'items': item_names,
            'weapons': weapon_names
        }

        db.insert_one(document)

# It's like the SELECT * FROM in SQLite, but this is for mongoDB
# We use list(db.find()) to query from MongoDB
# Don't forget to cast it as a list!
def show_all(db):
    all_docs = list(db.find())
    return all_docs

# Get the character names and their stats
GET_CHARACTER_TABLE = '''SELECT * FROM charactercreator_character;'''

# Get just the armory item names
GET_ITEM_TABLE = '''
    SELECT ai.name as item_name
    FROM (SELECT *
    FROM charactercreator_character as cc_char
    JOIN charactercreator_character_inventory as cc_inv
    WHERE cc_char.character_id = cc_inv.character_id) as char_inv
    JOIN armory_item as ai
    WHERE ai.item_id = char_inv.item_id
    AND char_inv.name = {};'''

# Get just the weapon names
GET_WEAPON_TABLE = '''
    SELECT ai.name
    FROM charactercreator_character as cc_char
    JOIN charactercreator_character_inventory as cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item as ai
    ON ai.item_id = cc_inv.item_id
    JOIN armory_weapon as aw
    ON ai.item_id = aw.item_ptr_id;'''

if __name__ == '__main__':
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(PASSWORD, DBNAME)

    # print(execute_query(sl_curs, GET_CHARACTER_TABLE))

    # Connect to the collection that we want to add the documents to
    # Just like the mongo.py file in Module2, remember the 3 layers? It
    #   was written and wrapped in one function, here it's written in 
    #   in the __name__ code block
    # Querying from MongoDB
    db = client.rpg_data
    collection = db['rpg_data']

    # Drop anything that is already in the collection
    # collection.drop({})

    doc_creation(collection, sl_curs, GET_CHARACTER_TABLE, GET_ITEM_TABLE, GET_WEAPON_TABLE)
    print(show_all(collection))