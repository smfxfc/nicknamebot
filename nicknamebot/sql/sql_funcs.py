#! python3
"""database interaction functions. Will consolidate this with sql_connect in future"""

from datetime import datetime
import pandas as pd
from pprint import pprint
import sql.sql_connect as sql_connect

con = sql_connect.db_connect()
cur = con.cursor()

def pull_db():
    cur.execute("SELECT * FROM user_nicknames ORDER BY time")
    qry_output = cur.fetchall()
    return qry_output

def pull_nicknames():
    cur.execute("SELECT nickname FROM user_nicknames")
    qry_output = cur.fetchall() # annoyingly outputs list of tuples

def last_user():
    output = pull_db()
    latest = [output[-1][0]] # last row, first column of db (returns a single tuple)
    user = latest[0] # selects tuple item. need to improve this
    return user # username string

def need_nicknames():
    # return list of users who don't have a nickname yet
    cur.execute("SELECT username FROM user_nicknames WHERE nickname IS 'TBD'")
    output = cur.fetchall()
    # con.commit()
    tmp = []
    for user in output:
        tmp.append(user[0])
    return tmp

def insert_username(username):
    cur.execute(
        'INSERT OR IGNORE INTO user_nicknames VALUES (?,?,?)',
        (username,'TBD','TBD')) # 'TBD's will be used to identify which usernames need nicknames
    con.commit()

# TBD: ENSURE NO DUPLICATE NICKNAMES
def insert_nickname(username, nickname):
    now_time = datetime.now().strftime("'%m-%d-%Y %H:%M:%S'")
    cur.execute(
        'UPDATE user_nicknames SET nickname=?,time=? WHERE username=?',
        (nickname,now_time,username))
    con.commit()
