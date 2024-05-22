import sqlite3

sqliteConnection=sqlite3.connect('ql.db')
print("Database created")

cursor=sqliteConnection.cursor()
print("Database Initilized")

sql_read_query="SELECT * FROM emp;"
cursor.execute(sql_read_query)
print(cursor.fetchall())



sqliteConnection.close()




