#! python3
"""Pulls last 1000 submissions on /r/getnicknamed and stores username of OP and all
commenters. Each new username added to the database receives a randomly generated nickname. 
This file executes every 2 minutes to check for and add new usernames in /r/getnicknamed."""

from datetime import datetime
import time

import sql.sql_connect as sql_connect
import utils.CreateNickname as CreateNickname
import utils.Reddit_Interface2 as RI
import sql.sql_funcs as sql_funcs

sr = 'getnicknamed'

start = time.time()

r = RI.bot_login() # instantiates reddit praw api

# pulls users from subreddit and adds them to database. Only adds users not yet in db, and sets their nickname value to 'TBD'
RI.add_users_by_comments()
RI.add_users_by_submissions()

# queries database for usernames with nickname values 'TBD' 
users_needing_nickname = sql_funcs.need_nicknames()

for username in users_needing_nickname:
    nickname = CreateNickname.create_nickname()
    sql_funcs.insert_nickname(username,nickname) # updates rows to add nickname and timestamp

current_db = sql_funcs.pull_db()

# to update the hub post on the subreddit. Can be moved to a separate module.
submission_url = "https://www.reddit.com/r/getnicknamed/comments/knm14f/at_this_time/?utm_source=share&utm_medium=web2x&context=3"
submission = r.submission(url=submission_url)

running_user_count = len(current_db)
last_user = [current_db[-1][0]][0]
last_nickname = [current_db[-1][1]][0]

edited_body = (
    f"""This subreddit has given a nickname to {running_user_count} users (and counting!).\n\n\n"""
    f"""The latest user to receive a nickname is u/{last_user}. Their nickname is {last_nickname}.""")

submission.edit(edited_body)

end = time.time()
time_elapsed = end - start
nowtime = datetime.now().strftime("'%m-%d-%Y %H:%M:%SZ')")

print(f"Loop completed at {nowtime}. Time elapsed: {time_elapsed}. Last user added: {last_user}. ")
