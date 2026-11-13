import os
import mysql.connector 
from dotenv import load_dotenv

#Load database credentials from .env
load_dotenv()

#Connect to MariaDB
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Check whether the connection was successful
if connection.is_connected():
    print("Successfully connected to MariaDB!")
    print("Database:", connection.database)

# Close the connection 
connection.close()

