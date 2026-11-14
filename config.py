"""
    @Use: This File Manages All Database Configurations
"""

# ---- Importing Modules ---- #
import os
from dotenv import load_dotenv

# Calling Environment Variables
load_dotenv()

# ------- Credentials ------- #
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# --- Config Verification --- #
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Missing Required Database Configuration In Environment Variables")
    
