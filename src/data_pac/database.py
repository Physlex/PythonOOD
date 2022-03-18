from cgi import test
import mysql.connector

"""
# Proc globals
"""

test_database = None
database_cursor = None


"""
# Proc methods
"""

def db_connect() :
    global test_database
    test_database = mysql.connector.connect(
        user = 'root',
        host = 'localhost',
        password = 'GAnelarbAFLVJOWIJVGE', #Not an actual password, dont even bother.
        database = 'test'
    )


def db_create() :
    global test_database
    global database_cursor
    database_cursor = test_database.cursor()


def db_show() :
    global database_cursor

    print(f'\nShowing databases:\n')

    #Show databases
    database_cursor.execute('SHOW DATABASES')
    for x in database_cursor :
        print(x)
    
    print(f'\nShowing tables:\n')

    #Show tables
    database_cursor.execute('SHOW TABLES')
    for x in database_cursor :
        print(x)


def table_create() :
    global database_cursor
    database_cursor.execute('''
        CREATE TABLE IF NOT EXISTS Junky_junk_junk ( 
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255), 
            address VARCHAR(255) 
            )
        ''')

def table_remove() :
    global database_cursor
    database_cursor.execute('DROP TABLE IF EXISTS Junky_junk_junk')

id_to_name = {
    0: "raggy",
    1: "the grand",
    2: "the magnanimous",
    3: "the dead",
    4: "the illiterate",
    5: "not actually"
}

def table_insert() :
    global database_cursor
    global test_database
    
    for x in range(1000) :
        database_cursor.execute(f'''
            INSERT INTO Junky_junk_junk (id, name, address) VALUE(0, "{"jhon " +  id_to_name[x % 5]}", "{str(2520) + str(x)}")
        ''')
        test_database.commit()

def table_query() :
    print('\nQuerying table in: test\n')
    database_cursor.execute('''
        SELECT * FROM Junky_junk_junk
    ''')
    for x in database_cursor : 
        print(x)

"""
# main proc globals
"""

insert:bool = False
remove:bool = False

"""
# Code starts here
"""


#Creating Data
db_connect()
db_create()

#Creating tables
print('\ncreating tables...\n')
table_create()
db_show()

#Inserting into tables
print('\ninserting into table: Junky_junk_junk\n')
if insert == True :
    table_insert()

#Querying text
table_query()

#Remove tables
if remove == True :
    print('\nremoving tables...\n')
    table_remove()
    db_show()

test_database.close()