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
        password = '1Evil_spaceman', #Not an actual password, dont even bother.
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
    database_cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Junky_junk_junk ( 
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255), 
            address VARCHAR(255) 
        )'''
    )

def table_remove() :
    global database_cursor
    database_cursor.execute('DROP TABLE IF EXISTS Junky_junk_junk')



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

#Remove tables
print('\nremoving tables...\n')
table_remove()
db_show()

test_database.close()