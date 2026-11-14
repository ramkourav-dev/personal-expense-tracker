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
# Root Connection
def createConnection():
    # Trying
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        return conn, None
        
    # If Any Error
    except mysql.connector.Error as err:
        return None, f"[!] MySQL Error: {err}"

# Creating Database
def createDatabase():
    # Connection & Verification
    conn, err = createConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = conn.cursor()
    
    # Trying
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS %s;", (DB_NAME))
        print("[✓] Database.")
        return True
        
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return False
        
    # Closing
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
        
# Connection To Database
def dbConnection():
    # Trying
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            database=DB_NAME
        )
        
        return conn, None
        
    # If Any Error
    except mysql.connector.Error as err:
        return None, f"[!] MySQL Error: {err}"

# Creating Table
def createTable():
    # Connection & Verification
    conn, err = dbConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = conn.cursor()
    
    # Trying
    try:
        query = """
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(150) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                category VARCHAR(64) NOT NULL,
                date DATE NOT NULL,
                note TEXT,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(query)
        
        print("[✓] Table")
        return True
        
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return False
        
    # Closing 
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
#