"""
    @Program: Personal Expense Tracker
    @Verion: 1.0
    @Author: Ram Kourav
"""

# ---- Importing Modules ---- #
from database import *

# ----- Welcoming Users ----- #
print(
    """
        +———————————————————————————————————————+
        |██▓▒­░⡷⠂𝙿𝚎𝚛𝚜𝚘𝚗𝚊𝚕 𝙴𝚡𝚙𝚎𝚗𝚜𝚎 𝚃𝚛𝚊𝚌𝚔𝚎𝚛⠐⢾░▒▓██|
        +———————————————————————————————————————+
    """
)

# ---- Check & Create DB ---- #
if not(isdbCreated()):
    # Showing Error
    print("[!] Database Not Created.")
    
    # Showing Solution
    print("\n\n[*] Database Not Created.")
    
    #Creating
    createDatabase()
    
    #Creating Tables
    createTable()
    
#If Created
else:
    print("[✓] Database Already Created.")
    
# ----- Expense Tracker ----- #
# Showing Menu Items###################