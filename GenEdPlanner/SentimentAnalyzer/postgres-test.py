from pathlib import Path

import pymysql
import pandas as pd
import psycopg2 as psycopg2
from dotenv import load_dotenv
import os
'''
dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

mydb = psycopg2.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    port=os.getenv('port')
)
'''
conn=pymysql.connect(host='localhost',user='root',password='Mayank.123')
cur=conn.cursor()




cur.execute("create database if not exists hackathonPSU;")
cur.execute("use hackathonPSU;")
cur.execute("drop table subjects;")
cur.execute("CREATE TABLE IF NOT EXISTS subjects(Course VARCHAR(255), Code VARCHAR(10), Credits INT, GA INT, GHW INT, GH INT, GN INT, GS INT, Rating VARCHAR(15), ABSRating INT);")


def insert(filename,types,lst):
    df_arts=pd.read_csv(filename)
    print(df_arts)
    for i in range(len(df_arts)):
        print(df_arts.loc[i].at["Code"])
        cur.execute('select * from subjects where code="'+df_arts.loc[i].at["Code"]+'";')
        r=cur.rowcount
        if r==0:
            cur.execute("insert into subjects values('"+df_arts.loc[i].at['Course']+"','"+df_arts.loc[i].at['Code']+"','"+str(df_arts.loc[i].at['Credits'])+"',%s,%s,%s,%s,%s,NULL,NULL);",(lst[0],lst[1],lst[2],lst[3],lst[4]))
            conn.commit()
        else:
            cur.execute("update subjects set "+types+"=1 where Code='"+df_arts.loc[i].at["Code"]+"';")  
            conn.commit()

lst=[["arts_gened.csv","GA",[1,0,0,0,0]],["humanities.csv","GH",[0,1,0,0,0]],["health_wellness.csv","GHW",[0,0,1,0,0]],["nat_sci.csv","GN",[0,0,0,1,0]],["social_behavior.csv","GS",[0,0,0,0,1]]]
for i in lst:
    insert(i[0],i[1],i[2])