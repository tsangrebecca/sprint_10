'''Contains a list of queries that feed into both
mongo_queries.py and postgresql_queries.py'''

# Use ElephantSQL to practice writing queries before writing them here
TOTAL_SURVIVED = '''
    SELECT sum(survived) FROM titanic_table;
    '''
TOTAL_DIED = '''
    SELECT COUNT(*) FROM titanic_table
    WHERE survived = 0;
    '''
TOTAL_EACH_CLASS = '''
    SELECT pclass, COUNT(name)
    FROM titanic_table
    GROUP BY pclass;
'''
SURVIVORS_BY_CLASS = '''
    SELECT pclass, SUM(survived)
    FROM titanic_table
    GROUP BY pclass;
'''
DIED_BY_CLASS = '''
    SELECT pclass, COUNT(name)
    FROM titanic_table
    WHERE survived = 0
    GROUP BY pclass;
'''
AVG_AGE_SURVIVED = '''
    SELECT AVG(age)
    FROM titanic_table
    WHERE survived = 1;
'''
AVG_AGE_DIED = '''
    SELECT AVG(age)
    FROM titanic_table
    WHERE survived = 0;
'''
AVG_AGE_CLASS = '''
    SELECT pclass, AVG(age)
    FROM titanic_table
    GROUP BY pclass;
'''
FARE_PER_CLASS = '''
    SELECT pclass, AVG(fare)
    FROM titanic_table
    GROUP BY pclass;
'''
FARE_PER_OUTCOME = '''
    SELECT survived, AVG(fare)
    FROM titanic_table
    GROUP BY survived;
'''
SIB_SPOUSE_SURVIVAL = '''
    SELECT survived, AVG(siblings_spouses_aboard)
    FROM titanic_table
    GROUP BY survived;
'''
SIB_SPOUSE_CLASS = '''
    SELECT pclass, AVG(siblings_spouses_aboard)
    FROM titanic_table
    GROUP BY pclass;
'''
PARENTS_CHILDREN_CLASS = '''
    SELECT pclass, AVG(parents_children_aboard)
    FROM titanic_table
    GROUP BY pclass;
'''
PARENTS_CHILDREN_SURVIVAL = '''
    SELECT survived, AVG(parents_children_aboard)
    FROM titanic_table
    GROUP BY survived;
'''
PASSENGERS_DIFF_NAMES = '''
    SELECT COUNT(DISTINCT name)
    FROM titanic_table;
'''
# Just like in databases > queries.py file
QUERY_LIST = [TOTAL_SURVIVED, TOTAL_DIED, TOTAL_EACH_CLASS, 
              SURVIVORS_BY_CLASS, DIED_BY_CLASS, AVG_AGE_SURVIVED, 
              AVG_AGE_DIED, AVG_AGE_CLASS, FARE_PER_CLASS,
              FARE_PER_OUTCOME, SIB_SPOUSE_SURVIVAL, SIB_SPOUSE_CLASS,
              PARENTS_CHILDREN_CLASS, PARENTS_CHILDREN_SURVIVAL,
              PASSENGERS_DIFF_NAMES]

#=====================================================================
###################### MongoDB Queries ###############################

# We answer the questions by creating a class and each function
#   answers a specific question in the assignment

class MongoAnswers():
    def __init__(self, collection):
        self.characters = list(collection.find({})) 
        # find({}) is getting all the documents
        # MUST CAST DICTIONARIES AS A LIST!!!!
        
    # How many total Characters are there?
    def total_characters(self):
        return len(self.characters)
    
    # How many total Items?
    # We are going to loop through every single character dictionary
    def total_items(self):
        count = 0
        for character in self.characters:
            count += len(character['items'])
            # To get items list from character dictionary
        return count
    
    # How many of the Items are Weapons? How many are not?
    def total_weapons(self):
        count = 0
        for character in self.characters:
            count += len(character['weapons'])
        return count
    
    def total_non_weapons(self):
        return self.total_items() - self.total_weapons()

    # How many Items does each Character have? (Return first 20 rows)
    def character_items(self):
        items_list = []
        for character in self.characters[:20]: # first 20 characters only
            num_items = len(character['items'])
            items_list.append((character['name'], num_items))
        return items_list
    
    # How many Weapons does each Character have? (Return first 20 rows)
    def character_weapons(self):
        weapons_list = []
        for character in self.characters[:20]: # first 20 characters only
            num_weapons = len(character['weapons'])
            weapons_list.append((character['name'], num_weapons))
        return weapons_list

    # On average, how many Items does each Character have?
    def average_items(self):
        num_items = [] # holds a list of num of items for each character
        for character in self.characters:
            num_items.append(len(character['items']))
        return (sum(num_items)) / len(num_items)

    # On average, how many Weapons does each Character have?
    def average_weapons(self):
        num_weapons = [] # holds a list of num of weapons for each character
        for character in self.characters:
            num_weapons.append(len(character['weapons']))
        return (sum(num_weapons)) / len(num_weapons)

    def show_results(self):
        return f'''
        Total Number of Characters: {self.total_characters()}
        Total Number of Items: {self.total_items()}
        Total Number of Weapons: {self.total_weapons()}
        Total Number of Non-Weapons: {self.total_non_weapons()}
        Number of Items for Each Character: {self.character_items()}
        Number of Weapons for Each Character: {self.character_weapons()}
        Average Number of Items: {self.average_items()}
        Average Number of Weapons: {self.average_weapons()}
        '''
    