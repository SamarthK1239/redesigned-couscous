from pathlib import Path

import psycopg2 as psycopg2
from dotenv import load_dotenv
import os

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

mydb = psycopg2.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    port=os.getenv('port')
)


