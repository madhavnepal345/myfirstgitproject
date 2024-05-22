import sqlite3
sqliteConnection=sqlite3.connect('ql.db')
print("Database created")

cursor=sqliteConnection.cursor()
print("Database Initilized")

create_table_query="""
CREATE  TABLE IF NOT EXISTS emp(id integer primary key AUTOINCREMENT, name text, address text);
"""
cursor.execute(create_table_query)



