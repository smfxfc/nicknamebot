#! python3

import praw

from credentials import config
import sql.sql_connect
import sql.sql_funcs as sql_funcs

sr = 'getnicknamed'

def bot_login():
    # creates a Reddit instance - to-do: create praw.ini file in order to keep authentication information separate from rest of code
    r = praw.Reddit(
        username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "getmeright11's nickname bot v0.1")
    return r

r = bot_login()

def add_users_by_comments(): # function calls subreddit name
    for comment in r.subreddit(sr).comments(limit=1000):
        user = comment.author
        if user==None:
            continue
        else:
            user = str(user)
            sql_funcs.insert_username(user)

def add_users_by_submissions(): # function calls subreddit name
    for submission in r.subreddit(sr).new(limit=1000):
        if not submission.author:
            continue
        else:
            user = submission.author.name
            sql_funcs.insert_username(user)

def create_flair(username, nickname): # take username input and generate a flair based on their key-value pair nickname
    random_color = "\"%03x\" % random.randint(0, 0xFFF)"
    # Add flair template for this nickname
    user_flair_template = r.subreddit(sr).flair.templates.add(nickname,background_color=random_color, text_color=random_color, css_class=nickname)
    r.subreddit(sr).flair.set(username, text=nickname, css_class=nickname)
    print(f"Set {user_flair_template} flair for {username}")
