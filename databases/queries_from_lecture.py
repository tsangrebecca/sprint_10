GET_CHARACTERS = 'SELECT * FROM charactercreator_character;' 
# all caps for a variable is a constant

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight 
FROM charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
JOIN armory_item AS ai
ON ai.item_id = cc_inv.item_id
GROUP BY cc_char.character_id
'''

# create a table using PostgreSQL and write in the schema
# "" is only for column header, '' is for strings in SQL
# in SQLite it's AUTOINCREMENT, in PostgreSQL it's SERIAL, aka 1, 2, 3, etc.
# set "id" as primary key
# in SQL, a string is called varchar(200) means max 200 characters long
CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
    '''

# remember, strings are single ''
# can automatically convert a string to an integer
INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Ryan Allred', 30, 'USA');'''


DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table
    '''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
    '''
INSERT_RYAN = '''
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('Ryan Allred', 50, 100, 1000, 9000, 4, -5, 12)
    '''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters
    '''