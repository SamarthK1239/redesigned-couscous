from pathlib import Path

import pandas as pd
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

cursor=mydb.cursor()

stmt="desc subjects;"
cursor.execute(stmt)

#df_arts=pd.read_csv('arts_gened.csv')

#for i in df_arts.iterrows():

