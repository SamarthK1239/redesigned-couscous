from pathlib import Path

import psycopg2

import main
from course_recommender import *
from dotenv import load_dotenv
import os

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


def databaseToLst(types):
    cur.execute("select code,course from subjects where " + types + "=1 ;")
    rows = cur.fetchall()
    lst = []
    for i in rows:
        dict = {}
        dict['title'] = i[0]
        dict['description'] = i[1]
        lst += [dict]
    return lst


def coursesPerArea(user_input):
    final_list = []
    for i in ['GA', 'GHW', 'GH', 'GN', 'GS', 'GQ', 'GWS']:
        lst = databaseToLst(i)
        output = recommender(lst, user_input)

        mean_list = []
        for out in output:
            reco = main.scaledRecommendation(out)
            if reco is not None:
                mean_list.append([main.scaledRecommendation(out), out])
        mean_list.sort(reverse=True)
        final_list.append(mean_list)
    return final_list
