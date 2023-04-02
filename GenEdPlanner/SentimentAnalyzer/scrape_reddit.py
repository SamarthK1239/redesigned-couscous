import os
from pathlib import Path

import praw
from dotenv import load_dotenv

from google_reddit_course import *

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

reddit = praw.Reddit(client_id=os.getenv('FHQQzTYqQxmq_t7P6xx22w'), client_secret=os.getenv('6_UZNjC31utMUEh2xUdKV7V2YNBudA'),
                     user_agent=os.getenv('hackPSU_spring_2023'))


def get_comments_list(query):
    query = query + "psu reddit"

    def get_comments():
        output = ''
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            output += " " + comment.body
        return output

    lst_of_comments = []
    for i in results(query):
        #print(i)
        try:
            submission = reddit.submission(url=i)
            lst_of_comments += [get_comments()]
        except:
            pass
    return lst_of_comments
