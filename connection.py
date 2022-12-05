import mysql.connector
from mysql.connector import Error

def connect_db():
    connection = mysql.connector.connect(
        host='localhost',
        database='crypto_python',
        user='root',
        password=''
    )
    return connection
