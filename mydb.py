import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'wildan',
    passwd = 'wildan123',
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE djangocrm")

print('All Done!')