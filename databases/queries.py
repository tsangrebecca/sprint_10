TOTAL_CHARACTERS = '''
SELECT COUNT(*) FROM charactercreator_character;'''
# : How many total Characters are there?

TOTAL_SUBCLASS = '''
SELECT COUNT(*) FROM charactercreator_necromancer;'''
#: How many of each specific subclass (the necromancer table)?

TOTAL_ITEMS = '''
SELECT COUNT(*) FROM armory_item;'''
#: How many total (armory) Items?

WEAPONS = '''
SELECT COUNT(*) FROM armory_weapon;'''
# : How many of the armory items are weapons?

NON_WEAPONS = '''
SELECT COUNT(*)
FROM armory_item as ai
LEFT JOIN armory_weapon as aw
ON ai.item_id = aw.item_ptr_id
WHERE aw.item_ptr_id IS NULL;'''
# : How many of the armory items are not weapons?

CHARACTER_ITEMS = '''
SELECT character_id, COUNT(item_id) AS number_of_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;'''
 # : How many Items does each character have? (Return first 20 rows)

CHARACTER_WEAPONS = '''
SELECT character_id, COUNT(item_ptr_id) AS number_of_weapons
FROM charactercreator_character_inventory as cc_inv
JOIN armory_item as ai
ON ai.item_id = cc_inv.item_id
JOIN armory_weapon as aw
ON aw.item_ptr_id = ai.item_id
GROUP BY character_id
LIMIT 20;'''
# : How many Weapons does each character have? (Return first 20 rows)

AVG_CHARACTER_ITEMS = '''
SELECT AVG(number_of_items) AS average_items 
FROM(SELECT character_id, COUNT(item_id) AS number_of_items
FROM charactercreator_character_inventory
GROUP BY character_id);'''
# : On average, how many Items does each Character have?

AVG_CHARACTER_WEAPONS = '''
SELECT AVG(number_of_weapons) AS average_weapons
FROM(SELECT character_id, COUNT(item_ptr_id) AS number_of_weapons
FROM charactercreator_character_inventory as cc_inv
JOIN armory_item as ai
ON ai.item_id = cc_inv.item_id
JOIN armory_weapon as aw
ON aw.item_ptr_id = ai.item_id
GROUP BY character_id);'''
# : On average, how many Weapons does each character have?

QUERY_LIST = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS,
              WEAPONS, NON_WEAPONS, CHARACTER_ITEMS, CHARACTER_WEAPONS,
              AVG_CHARACTER_ITEMS, AVG_CHARACTER_WEAPONS]