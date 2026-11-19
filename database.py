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
        return False
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`;")
        print("[✓] Database.")
        return True
        
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return None
        
    # Closing
    finally:
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
        return False
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(150) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                category VARCHAR(64) NOT NULL,
                expense_date DATE NOT NULL,
                note TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(query)
        
        print("[✓] Table")
        return True
        
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return None
        
    # Closing 
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
# Insert Expense
def insertExpense(title, price, category, expense_date, note=None):
    # Connection
    conn, err = dbConnection()
    if err:
        print(err)
        return False
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses(
                title, price, category, expense_date, note
            )
            VALUES(
                %s, %s, %s, %s, %s
            )
            """,
            (title, price, category, expense_date, note)
        )
        conn.commit()
        return True
        
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        conn.rollback()
        return None
        
    # Closing
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
# Getting Expenses
def getExpenses():
    # Connection
    conn, err = dbConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses ORDER BY expense_date DESC;")
        expenses = cursor.fetchall()
        
        # Printing
        if not expenses:
            print("[!] No Expenses Found")
        else:
            for expense in expenses:
                print(expense)
                
        return expenses
    
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return None
        
    # Finally
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
# Getting Single Expense
def getExpense(expense_id):
    # Connection
    conn, err = dbConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE expense_id = %s;", (expense_id,))
        expense = cursor.fetchone()
        
        # Printing
        if expense is None:
            print("[!] No Expense Found")
            return None
            
        else:
            print(expense)
            
        return expense
    
    # If Any Error
    except mysql.connector.Error as err:
        print(f"[!] MySQL Error: {err}")
        return None
        
    # Finally
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            
# Updating Expense
def updateExpense(expense_id, title, price, category, expense_date, note=None):
    # Connecting Do Database
    conn, err = dbConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE expenses
                SET
                    title = %s,
                    price = %s,
                    category = %s,
                    expense_date = %s,
                    note = %s
                WHERE expense_id = %s;
            """,
            (title, price, category, expense_date, note, expense_id)
        )
        rowsAffected = cursor.rowcount
        conn.commit()
        
        print(f"[{rowsAffected}] Affected!")
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
            
# Deleting Expense
def deleteExpense(expense_id):
    # Connecting to database
    conn, err = dbConnection()
    if err:
        print(err)
        return None
        
    # Cursor
    cursor = None
    
    # Trying
    try:
        cursor = conn.cursor()
        cursor.execute(
            " DELETE FROM expenses WHERE expense_id = %s;",
            (expense_id,)
        )
        conn.commit()
        
        print("[✓] Deleted.")
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
            
# Checking DB Existence
def isdbCreated():
    pass
