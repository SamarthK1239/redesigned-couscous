import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

conn = psycopg2.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    port=os.getenv('port')
)
cur = conn.cursor()

cur.execute("SELECT * FROM subjects WHERE Code='AA 100';")
current_course=cur.fetchall()
print(current_course)