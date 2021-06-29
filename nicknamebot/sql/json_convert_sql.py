#! python3
"""Convert data stored in JSON file to sqlite3 database to 
improve program efficiency.
The sql db will contain a table with columns username, nickname, time_added"""

import json
import os
import sqlite3
from datetime import datetime

import sql_connect

# user nickname info from previous program version, stored in json 
JSONDATA_PATH = "/home/thinky/nicknames_prototype/User_dict.json"

with open(JSONDATA_PATH, 'r') as jsonfile:
    user_nickname_dict = json.load(jsonfile)

con = sql_connect.db_connect()
cur = con.cursor()

# create table with 3 columns: username, nickname, and time added to db
create_tbl = """
CREATE TABLE user_nicknames (
    username text PRIMARY KEY,
    nickname text,
    time text
    )"""

cur.execute(create_tbl)
con.commit()


# when adding new users to datebase, time_now will be the time the user received a nickname. All usernames
# converted from previous json file will have the same timestamp (when I converted them to sql)
time_now = datetime.now().strftime("'%m-%d-%Y %H:%M:%S'")

for username, nickname in user_nickname_dict.items():
    cur.execute('INSERT OR IGNORE INTO user_nicknames VALUES (?,?,?)',
    (username, nickname, time_now))
con.commit()

