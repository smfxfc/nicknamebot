# python3

import os
import sqlite3
from datetime import datetime

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '/home/thinky/nicknamebot/data/nicknamedb.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

# con = db_connect()
