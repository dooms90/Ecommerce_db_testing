import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="chuja9079", 
        database="ecommerce_db"
    )
    return connection

def close_connection(connection, cursor):
    cursor.close()
    connection.close()