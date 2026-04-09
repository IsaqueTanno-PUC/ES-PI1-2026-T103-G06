import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar ():
    return mysql.connector.connect(
        host=os.getenv("BD_HOST"),
        user=os.getenv("BD_USER"),
        password=os.getenv("BD_PASSWORD"),
        database=os.getenv("BD_NOME")
    )