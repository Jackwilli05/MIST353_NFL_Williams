import os
import pymssql
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_LOGIN")
    password = os.getenv("DB_PASSWORD")
    
    # Remove 'tcp:' and ',1433' from server for pymssql
    server = server.replace('tcp:', '').replace(',1433', '')
    
    conn = pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database
    )
    return conn