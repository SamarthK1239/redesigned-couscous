import pymysql
from course_recommender import *


conn=pymysql.connect(host='localhost',user='root',password='Mayank.123')
cur=conn.cursor()
cur.execute("use hackathonPSU;")



def databaseToLst(types):
    cur.execute("select code,course from subjects where"+types+"=1 ;")
    rows=cur.fetchall()
    lst=[]
    for i in rows:
        dict={}
        dict['title']=i[0]
        dict['description']=i[1]
        lst+=[dict]
    conn.close()
    return lst


for i in ['GA','GH','GS','GHW','GN']:
    lst=databaseToLst(i)
    output=recommender(lst)
