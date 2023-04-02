import os
from pathlib import Path

import praw
from dotenv import load_dotenv

from google_reddit_course import *

dotenv_path = Path('Environment Variables/.env')
load_dotenv(dotenv_path=dotenv_path)

reddit = praw.Reddit(client_id=os.getenv('client_id'), client_secret=os.getenv('client_secret'),
                     user_agent=os.getenv('user_agent'))

query = "egee 101 psu reddit"


def get_comments_list():
    def get_comments():
        output = ''
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            output += " " + comment.body
        return output

    lst_of_comments = []
    for i in results(query):
        print(i)
        try:
            submission = reddit.submission(url=i)
            lst_of_comments += [get_comments()]
        except:
            print('not reddit website')
    return lst_of_comments
