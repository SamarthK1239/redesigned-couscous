import praw
from google_reddit_course import *
reddit = praw.Reddit(client_id='FHQQzTYqQxmq_t7P6xx22w', client_secret='6_UZNjC31utMUEh2xUdKV7V2YNBudA', user_agent='hackPSU_spring_2023')

query="cmpsc 131 psu reddit"


def get_comments():
    output=''
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        output+=comment.body
    return output

lst_of_comments=[]
for i in results(query):
    print(i)
    try:
        submission = reddit.submission(url=i)
        lst_of_comments+=[get_comments()]
    except:
        print('not reddit website')

for i in lst_of_comments:
    print(i)