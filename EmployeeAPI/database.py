import mysql.connector

def get_connection():

    connection = mysql.connector.connect(
        host="localhost",   #URL of Database
        user="root",        # Username
        password="root",    # Password  
        database="invesco"  # Schemas
    )

    return connection