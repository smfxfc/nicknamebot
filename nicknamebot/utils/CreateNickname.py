#! python3

import random
import json

PREFIXES = "data/prefixes.json"
ADJECTIVES = "data/adjectives.json"

def random_prefix():
    with open(PREFIXES) as r:
        data = json.load(r)
    prefix = random.choice(data)
    return prefix

def random_adjective():
    with open(ADJECTIVES) as r:
        data = json.load(r)
    adj = random.choice(data)
    return adj.capitalize()

def create_nickname():
    prefix = random_prefix()
    adjective = random_adjective()
    nickname = f"{prefix} {adjective}"
    return nickname
