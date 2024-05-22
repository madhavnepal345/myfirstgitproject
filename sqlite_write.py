import sqlite3
sqliteConnection=sqlite3.connect('ql.db')
print("Database created")

cursor=sqliteConnection.cursor()
print("Database Initilized")

insert_table_query="""
INSERT INTO emp(name,address) VALUES("arjun","ktm")
"""
insert_table_query="""
INSERT INTO emp(name,address) VALUES("arjun","ktm")
"""
insert_table_query="""
INSERT INTO emp(name,address) VALUES("ram","baneshwor")
"""
insert_table_query="""
INSERT INTO emp(name,address) VALUES("krishna","koteshwor")
"""

cursor.execute(insert_table_query)
sqliteConnection.commit()

sqliteConnection.close()