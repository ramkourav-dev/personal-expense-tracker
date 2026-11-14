"""
    @Use: All Stuffs Related Database, Like:
        Connection With Database
        Creating Database If Not Exists
        Creating Table If Not Exists etc.
"""

# ---- Importing Modules ---- #
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

# -------- Functions -------- #
# For Connection
def createConnection():
    # Trying
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        return conn
        
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
