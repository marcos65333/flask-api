import mysql.connector 
import os


def connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except Exception as e:
        print("Error connecting to database: ", e)